# 更新记录

## v1.0.0 · 2026-11-08

从 `dialysis` 工具包拆出的首个独立版本。

- Skill 名定为 `xin-dialysis`，独立仓库 https://github.com/oscar-wang-xin/xin-dialysis-skill.git；配套工具包 https://github.com/oscar-wang-xin/dialysis.git 仍在原仓库，两者分开维护、可分别安装。
- 搬入原有内容：`SKILL.md` 的红线与数据契约、帮助与四个端到端示例、分级措辞模板、三种输出模板、9 张护理常识卡。
- **补入工具包知识页的全部结构化内容**：新建 `references/knowledge-index.md`（22 宣教 + 38 药名，含编号、标题、链接）与 `references/checklists.md`（三级排查完整表、5 条常见情况速查、导出数据字典）。
- `SKILL.md` 第 5 节扩成「回答护理常识与查知识列表」，帮助表格增加第五类任务，安装路径改为 `~/.workbuddy/skills/xin-dialysis/`。
- 新增 `tools/check.py` 自检：索引条数、URL 完整性、Skill 名、隐私与机构关键词。
- 许可证 MIT。
