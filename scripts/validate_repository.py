#!/usr/bin/env python3
"""Check repository structure and public-content boundaries, not musical correctness."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check_repository() -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    required = [
        'SKILL.md', 'README.md', 'README.en.md', 'README.ru.md', 'LICENSE',
        'THIRD_PARTY_NOTICES.md', 'CONTRIBUTING.md', 'CHANGELOG.md',
        'COPYRIGHT_AND_DISCLAIMER.md', 'PRIVACY.md',
        'agents/openai.yaml', 'glossary.md', 'patterns.md', 'cheatsheet.md',
        'references/source-map.md', 'references/source-index.json',
        'references/differences.md', 'references/ocr-quality.md',
    ]
    for rel in required:
        if not (ROOT / rel).is_file():
            errors.append(f'Missing required file: {rel}')
    if errors:
        return errors, {}

    license_text = (ROOT / 'LICENSE').read_text(encoding='utf-8')
    if 'Attribution-NonCommercial 4.0 International' not in license_text:
        errors.append('Expected the official CC BY-NC 4.0 license text')

    skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
    match = re.match(r'\A---\n(.*?)\n---\n', skill, re.S)
    if not match:
        errors.append('SKILL.md must start with YAML frontmatter')
    else:
        header = match.group(1)
        if not re.search(r'^name:\s*russian-harmony\s*$', header, re.M):
            errors.append('Skill name must remain russian-harmony')
        if not re.search(r'^description:\s*\S', header, re.M):
            errors.append('Skill description is missing')

    markdown = [p for p in ROOT.rglob('*.md') if '.git' not in p.parts]
    for path in markdown:
        text = path.read_text(encoding='utf-8')
        if re.search(r'\[TODO\]|\bFIXME\b', text):
            errors.append(f'Unfinished placeholder: {path.relative_to(ROOT)}')
        for target in re.findall(r'\]\(([^\s)]+)\)', text):
            if target.startswith(('#', 'mailto:')) or '://' in target:
                continue
            destination = (path.parent / target.split('#')[0]).resolve()
            if not destination.is_relative_to(ROOT):
                errors.append(f'Link leaves repository: {path.relative_to(ROOT)} -> {target}')
            elif not destination.exists():
                errors.append(f'Broken link: {path.relative_to(ROOT)} -> {target}')

    index = json.loads((ROOT / 'references/source-index.json').read_text(encoding='utf-8'))
    mapping = index['mapping']
    if [item['a_topic'] for item in mapping] != list(range(42)):
        errors.append('Expected A introduction plus topics 1–41 in order')
    b_topics = {int(item[0]) for item in index['b_topics']}
    covered = {n for item in mapping for n in item['b_topics']}
    supplements = {
        59: 'references/b-tonal-plan.md',
        60: 'references/b-analysis.md',
    }
    for topic, rel in supplements.items():
        if (ROOT / rel).is_file():
            covered.add(topic)
    if not b_topics.issubset(covered):
        errors.append(f'Unmapped B topics: {sorted(b_topics-covered)}')
    for item in mapping:
        if not (ROOT / item['file']).is_file():
            errors.append(f'Missing topic file: {item["file"]}')

    def check_private_keys(value: object, location: str = '') -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if key in {'library_file_id', 'file_id', 'local_path'}:
                    errors.append(f'Private source key: {location}/{key}')
                check_private_keys(child, f'{location}/{key}')
        elif isinstance(value, list):
            for number, child in enumerate(value):
                check_private_keys(child, f'{location}/{number}')

    check_private_keys(index)
    private_patterns = [
        re.compile(r'libfile_[0-9a-f]{20,}'),
        re.compile(r'file_[0-9a-f]{24,}'),
        re.compile(r'/(?:Users|home|root|workspace)/[^\s\"<>]+'),
        re.compile(r'(?:ghp|github_pat)_[A-Za-z0-9_]{20,}'),
        re.compile(r'[A-Za-z0-9._%+-]+@(?:gmail|outlook|hotmail|icloud|qq)\.[A-Za-z]+'),
    ]
    files = [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts]
    forbidden_suffixes = {'.pdf', '.epub', '.traineddata', '.dylib'}
    forbidden_directories = {'sources', 'ocr', 'raw-ocr', 'harmony-work', 'deliverables'}
    for path in files:
        rel = path.relative_to(ROOT)
        if '__pycache__' in rel.parts or path.suffix == '.pyc':
            continue
        if path.suffix.lower() in forbidden_suffixes or any(part in forbidden_directories for part in rel.parts):
            errors.append(f'Non-public source/runtime artifact: {rel}')
        if path.name == '.DS_Store' or path.name == '.env' or path.name.startswith('.env.'):
            errors.append(f'Local-only file: {rel}')
        if path.stat().st_size > 2 * 1024 * 1024:
            errors.append(f'Unexpectedly large public file: {rel}')
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            errors.append(f'Unexpected binary file: {rel}')
            continue
        if any(pattern.search(text) for pattern in private_patterns):
            errors.append(f'Private identifier, local path or credential pattern: {rel}')

    for rel in ['README.md', 'README.en.md', 'README.ru.md']:
        text = (ROOT / rel).read_text(encoding='utf-8')
        if 'CC BY-NC 4.0' not in text or '[MIT' in text or '[Лицензия MIT' in text:
            errors.append(f'Non-commercial licensing notice is missing or inconsistent: {rel}')
        for link in ['README.md', 'README.en.md', 'README.ru.md']:
            if f']({link})' not in text:
                errors.append(f'Missing language navigation in {rel}: {link}')
    stats = {'markdown_files': len(markdown), 'A_entries': len(mapping), 'B_topics_mapped': len(b_topics & covered)}
    return errors, stats


if __name__ == '__main__':
    problems, statistics = check_repository()
    for problem in problems:
        print('ERROR:', problem)
    if problems:
        sys.exit(1)
    print('Repository checks passed:', json.dumps(statistics, ensure_ascii=False))
    print('These checks do not establish musical correctness, OCR accuracy or third-party rights.')
