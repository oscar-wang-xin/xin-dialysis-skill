# -*- coding: utf-8 -*-
"""xin-dialysis 自检：索引条数、URL、Skill 名、隐私与机构关键词。

用法： python tools/check.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANNED = [
    '王一平', '77 岁', '67 kg', '干体重 67', '剩约 40 分钟',
    '85323591', '药学部', '血液净化科',
]


def main():
    problems = []
    idx = (ROOT / 'references/knowledge-index.md').read_text(encoding='utf-8')
    try:
        tree = idx.split('## 一、健康宣教')[1].split('## 二、常用口服药')[0]
        drug = idx.split('## 二、常用口服药')[1].split('\n---')[0]
    except IndexError:
        print('构建中止：知识索引缺少分组标题')
        return 1
    ntree = len(re.findall(r'^- \*\*\d+\*\*', tree, re.M))
    ndrug = len(re.findall(r'^- \*\*\d+\*\*', drug, re.M))
    urls = re.findall(r'<(https?://[^>]+)>', idx)
    if ntree != 22:
        problems.append('健康宣教应为 22 条，实际 %d' % ntree)
    if ndrug != 38:
        problems.append('常用口服药应为 38 条，实际 %d' % ndrug)
    if len(urls) != 60:
        problems.append('链接应为 60 条，实际 %d' % len(urls))

    skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
    if not re.search(r'^name: xin-dialysis$', skill, re.M):
        problems.append('SKILL.md 的 name 不是 xin-dialysis')
    for ref in ['care-cards.md', 'triage.md', 'checklists.md',
                'knowledge-index.md', 'templates.md', 'examples.md']:
        if not (ROOT / 'references' / ref).is_file():
            problems.append('缺少 references/' + ref)

    for p in sorted(ROOT.rglob('*')):
        if not p.is_file() or p.name == 'check.py':
            continue
        if '.git' in p.parts or '__pycache__' in p.parts:
            continue
        if p.suffix.lower() not in ('.md', '.json', '.py', '.txt', ''):
            continue
        try:
            txt = p.read_text(encoding='utf-8')
        except (UnicodeDecodeError, OSError):
            continue
        for word in BANNED:
            if word in txt:
                problems.append('%s 含禁用词：%s' % (p.relative_to(ROOT), word))

    if problems:
        print('自检未通过：')
        for x in problems:
            print('  - ' + x)
        return 1
    print('自检通过：宣教 %d 条 / 药名 %d 条 / 链接 %d 条 / Skill 名 xin-dialysis / 隐私与机构关键词 0 命中' %
          (ntree, ndrug, len(urls)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
