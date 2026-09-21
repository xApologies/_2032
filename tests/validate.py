"""Validate bootstrap artifacts; no network access or architecture outcome claims."""
from pathlib import Path
import copy
import hashlib
import json
import re
from urllib.parse import unquote, urlsplit
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
errors = []

def check(condition, message):
    if not condition:
        errors.append(message)

def anchors(path):
    counts, result = {}, set()
    for line in path.read_text(encoding='utf-8').splitlines():
        if not re.match(r'^#{1,6} ', line):
            continue
        name = re.sub(r'[^\w\- ]', '', re.sub(r'^#+ ', '', line).lower()).replace(' ', '-')
        count = counts.get(name, 0)
        counts[name] = count + 1
        result.add(name if not count else f'{name}-{count}')
    return result

link_count = 0
for path in ROOT.rglob('*.md'):
    if '.git' in path.parts or '.venv' in path.parts:
        continue
    text = path.read_text(encoding='utf-8')
    for href in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
        uri = urlsplit(href.strip('<>'))
        if uri.scheme or uri.netloc:
            continue
        link_count += 1
        target = (path.parent / unquote(uri.path)).resolve() if uri.path else path
        check(target.is_relative_to(ROOT), f'{path}: link escapes repository: {href}')
        check(target.exists(), f'{path}: broken link: {href}')
        if target.is_file() and uri.fragment and target.suffix == '.md':
            check(unquote(uri.fragment) in anchors(target), f'{path}: missing anchor: {href}')

kinds = ('claims', 'sources', 'decisions', 'assumptions', 'uncertainties', 'workstreams', 'tests')
validators, records, ids = {}, {}, {}
for kind in kinds:
    definition = json.loads((ROOT / f'schemas/{kind}.schema.json').read_text())
    Draft202012Validator.check_schema(definition)
    validators[kind] = Draft202012Validator(definition, format_checker=FormatChecker())
    records[kind] = json.loads((ROOT / f'PROVENANCE/records/{kind}.json').read_text())
    check(isinstance(records[kind], list), f'{kind}: expected record array')
    for item in records[kind]:
        for error in validators[kind].iter_errors(item):
            errors.append(f'{kind}/{item.get("id")}: {error.message}')
        check(item['id'] not in ids, f'Duplicate ID: {item["id"]}')
        ids[item['id']] = kind

for kind, items in records.items():
    for item in items:
        for ref in item['source_ids']:
            check(ids.get(ref) == 'sources', f'{item["id"]}: invalid source {ref}')
        for field, expected in [('supporting_claim_ids', 'claims'), ('supersedes_ids', 'decisions'), ('dependency_ids', 'workstreams')]:
            for ref in item.get(field, []):
                check(ids.get(ref) == expected, f'{item["id"]}: invalid {field}: {ref}')
        if kind == 'workstreams':
            check((ROOT / item['path']).is_file(), f'{item["id"]}: missing workstream file')
        if kind == 'sources':
            source = ROOT / item['locator']
            check(source.is_file(), f'{item["id"]}: missing evidence file')
            if source.is_file():
                check(hashlib.sha256(source.read_bytes()).hexdigest() == item['sha256'], f'{item["id"]}: evidence hash mismatch')

for kind, field in [('claims', 'supporting_claim_ids'), ('workstreams', 'dependency_ids'), ('decisions', 'supersedes_ids')]:
    graph = {item['id']: item[field] for item in records[kind]}
    def visit(node, trail):
        if node in trail:
            errors.append(f'{kind}: cyclic lineage at {node}')
            return
        for child in graph.get(node, []):
            visit(child, trail | {node})
    for node in graph:
        visit(node, set())

negative_count = 0
for kind in kinds:
    for mutate in ('missing_id', 'bad_date', 'unknown_status', 'extra_field'):
        item = copy.deepcopy(records[kind][0])
        if mutate == 'missing_id':
            del item['id']
        elif mutate == 'bad_date':
            item['recorded_on'] = '2026-02-30'
        elif mutate == 'unknown_status':
            item['epistemic_status'] = 'PROVEN BY AI'
        else:
            item['unrecognized'] = True
        check(not validators[kind].is_valid(item), f'{kind}: accepted negative fixture {mutate}')
        negative_count += 1

specials = [
    ('claims', {'epistemic_status': 'EXTERNALLY VERIFIED FACT'}),
    ('decisions', {'authority': None}),
    ('tests', {'state': 'complete'}),
    ('sources', {'sha256': 'not-a-hash'}),
]
for kind, patch in specials:
    item = copy.deepcopy(records[kind][0])
    item.update(patch)
    check(not validators[kind].is_valid(item), f'{kind}: accepted invalid semantic fixture {patch}')
    negative_count += 1

if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {link_count} local links, {len(kinds)} schemas, {len(ids)} records, '
      f'{negative_count} negative fixtures; references, cycles, and evidence hashes valid.')
