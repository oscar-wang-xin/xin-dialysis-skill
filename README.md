# xin-dialysis

透析患者与家属用的 WorkBuddy Skill。**Skill 名 `xin-dialysis`**，独立仓库：https://github.com/oscar-wang-xin/xin-dialysis-skill.git

配套工具包（六张离线 HTML 页面）：https://github.com/oscar-wang-xin/dialysis.git —— 两边可以分开装、分开更新。工具负责把数据记下来，这个 Skill 负责 AI 「怎么说话、什么时候闭嘴」。只查知识索引时，不装工具包也能用。

## 这个 Skill 干什么

- 解读工具包导出的 JSON 备份或文本记录：只念事实与变化，不诊断、不推测病因、不解释化验单。
- 按症状核对红 / 黄 / 绿分级与常见情况速查：命中急症第一句就是拨号三步，不排队分析。
- **检索 60 条知识索引**：22 条健康宣教 + 38 条常用口服药名，回编号、标题、链接。
- 生成就诊摘要一页纸、记录台账、待问医生清单。

红线写死：不诊断、不调药、不建议剂量、不调整透析参数、不拿「应该没事」糊弄人。完整规矩见 [SKILL.md](SKILL.md)。

## 知识内容

从工具包知识页原样搬来，编号与工具页一致：

| 文件 | 内容 |
| --- | --- |
| `references/care-cards.md` | 9 张护理常识卡全文 |
| `references/triage.md` | 红 / 黄 / 绿分级措施模板、禁止措辞清单 |
| `references/checklists.md` | 三级排查完整表、5 条常见情况速查、导出数据字典 |
| `references/knowledge-index.md` | **60 条知识索引**（22 宣教 + 38 药名，含链接） |
| `references/templates.md` | 三种输出模板 |
| `references/examples.md` | 四个端到端示例：家属原话 → 虚构输入 → 完整回复 → 逐条对照规则 |

60 条链接指向第三方原文，本仓库只收录海报上二维码解码得到的地址与标题文字，**没有抓取正文、不解释内容、不补写剂量与用法**。链接打不开时给三条兜底：微信内打开、复制后换设备打开、扫海报原图。

## 安装

```bash
git clone https://github.com/oscar-wang-xin/xin-dialysis-skill.git ~/.workbuddy/skills/xin-dialysis
```

或者把整个目录复制到 `~/.workbuddy/skills/xin-dialysis/`（**建真实目录，不要用软链**），重启会话后按触发词调用。`SKILL.md` 第 7 节是完整帮助，第 8 节有一个最短例子。

四句能直接抄的话：

- 「看看这几天的记录，哪些没记全」
- 「把最近几次血糖整理一下」
- 「刚下机人有点迷糊，要不要紧」
- 「有没有讲内瘘的宣教」

## 自检

```bash
python tools/check.py
```

检查 60 条索引的条数与 URL、SKILL.md 的 `name`、以及全仓是否混入真实患者信息或机构联系方式。只需 Python 3，无第三方依赖。

## 隐私与边界

- 仓库里没有任何真实姓名、病历、健康数值或联系方式；示例数据全部虚构、一眼可辨。
- Skill 不读取本机浏览器存储，只处理使用者主动导出的备份；健康数据只留在使用者自己手里。
- 这个 Skill 用于家庭照护的记录整理与就诊沟通，**不构成医疗建议、不用于诊断或治疗决策**，也不是医疗器械。出现急症请立即联系透析中心或拨打 120。

## 许可证

本仓库自己写的代码与文档采用 [MIT](LICENSE) · Copyright (c) 2026 oscar-wang-xin。

MIT 只覆盖本仓库的文档与脚本，不覆盖第三方内容：60 条外链指向的宣教原文、海报原图，版权归各原作者，默认不入库。要引用请回到原文，按原作者的要求来。
