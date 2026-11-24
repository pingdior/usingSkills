# usingSkills

日常在用的 AI Agent **Skill**（可复用任务指令集）合集，遵循 Anthropic Agent Skills 文件规范，可直接放进 Claude Code、Cursor、DeepSeek Harness、WorkBuddy 等支持 Skill 的 agent。

- **作者**：pingdior
- **技能数量**：47 个，分 7 类
- **许可**：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)（可自由使用和修改，需署名）

> 🆕 **最近更新**：新增 [`rapid-learn`](#七学习1-个)，一个限时快速学习教练，支持两种模式：成人自学一个方向，或者孩子学高中课程的某个单元。

---

## 目录

- [快速开始](#快速开始)
- [按需求找 Skill](#按需求找-skill)
- [技能列表](#技能列表)
- [怎么跟 Skill 对话](#怎么跟-skill-对话)
- [自己写 Skill 的三条硬规矩](#自己写-skill-的三条硬规矩)
- [仓库结构与文件规范](#仓库结构与文件规范)

---

## 快速开始

Skill 就是一个文件夹，**把整个文件夹**复制到 agent 的 skill 目录即可：

```bash
git clone https://github.com/pingdior/usingSkills /tmp/usingSkills

# 按你用的 agent 选一个目标目录
cp -R /tmp/usingSkills/rapid-learn ~/.claude/skills/      # Claude Code
cp -R /tmp/usingSkills/rapid-learn ~/.dsh/skills/         # DeepSeek Harness
cp -R /tmp/usingSkills/rapid-learn ~/.workbuddy/skills/   # WorkBuddy
```

装好后直接用自然语言提需求，agent 会根据 `description` 自动选择要加载的 Skill，不需要记命令。

> ⚠️ 下表「附带资料」列标 ✅ 的 Skill 带有 `references/` 或 `assets/` 子目录，**必须整个文件夹一起复制**。只拷 `SKILL.md` 会丢失模式说明、模板等内容。

---

## 按需求找 Skill

| 你想做的事 | 从这里开始 | 然后 |
|---|---|---|
| 几小时内快速入门一个方向、项目、论文或代码仓库 | `rapid-learn`（domain 模式） | 学完把 🟡 待补清单交给它，生成 7 天补漏计划 |
| 孩子复习高中某个单元（数学、语文等） | `rapid-learn`（course 模式） | 用附带的错题本和家长报告模板 |
| 做新产品或新业务 | `seed-extraction` | → `seed-convergence` → `digital-life-service-design` |
| 设计 AI Agent 产品 | `digital-life-service-design` | → `harness-design` → `retention-diagnosis-loop` |
| Agent 空转、烧钱或失控 | `harness-design` | — |
| 写好提示词 | `prompt-best-practices` | → `how-to-write-excellent-prompts` → `prompt-mother` |
| 一件复杂的事想不清楚 | `multi-angle-evidence-analysis` | — |
| 出小红书或视频号内容 | `xiaohongshu-trending-content-script` | → `xiaohongshu-platform-card-output` |
| 用 AI 编码 agent 开发产品 | `create-vibe-project` | → `cto-for-videcoding` |

---

## 技能列表

### 一、Agent / 系统设计（5 个）

适合做产品和做 Agent 的人。这一组共用交接契约，按任务和证据缺口选用，不要求每次把五个全部串起来跑。

| 技能 | 说明 | 附带资料 |
|---|---|:---:|
| `seed-extraction` | 种子提炼：条目类型、四部件、证据与版本化交接契约 | ✅ |
| `seed-convergence` | 交互收敛：按缺口提问、反例检查、判断下一步信息是否充分 | ✅ |
| `digital-life-service-design` | 服务设计：Seed / Harness / Memory、目标取舍与数据流 |  |
| `harness-design` | 运行设计：架构选择、长期运行机制、证据分类与恢复 | ✅ |
| `retention-diagnosis-loop` | 价值与留存诊断：测量、实验、分类型记忆和策略发布 | ✅ |

<details>
<summary><b>Agent 设计技能 v2：交接契约、版本与验证方法（点击展开）</b></summary>

配套使用时，把这五个文件夹放在同一个技能目录下，各自的 `references/` 都要保留。单独安装也能做分析、出草稿；引用的契约不可用时，需要标出交接缺口，不能假定已获生产批准。

- [种子契约](seed-extraction/references/seed-contract.md)：种子字段、状态、版本和批准范围，以这里为唯一维护来源。
- [运行契约](harness-design/references/runtime-contract.md)：任务状态、工具权限、幂等与恢复。
- [长期运行机制](harness-design/references/long-running-runtime.md)：按需选用上下文工作集、持久重派预算、写入隔离、依赖调度、配额准入、事件索引和告警生命周期。
- [机制证据记录](harness-design/references/mechanism-evidence.json)：27 条机制逐项区分源码行为、已有测试说明和待验证的运行收益，另附访谈充分度记录和 8 篇参考来源。
- [测量与实验](retention-diagnosis-loop/references/measurement.md)：事件关联、成熟窗口、基线和实验口径。
- [记忆生命周期](retention-diagnosis-loop/references/memory-lifecycle.md)：个人偏好、推断、经验和策略各自的生效路径。

从 v1 迁移时，要补齐类型、范围、证据状态和有效的批准记录；不能只改版本号就宣布旧产物已获批准。Harness 统一指运行时外壳，环境接入是其中的工具/适配部分。

长期运行增补之后，`harness-design` 与 `seed-convergence` 为 2.1.0，其余三个为 2.0.0；交接协议仍为 `seed/v2`。

这些是设计类技能，不是底层 Harness 实现。证据记录里的 `article_reported` 只表示来自文章转述，不表示本仓库直接复核过源码提交或复跑过测试；运行收益目前全部是 `unmeasured`，不能根据结构校验推算生产效果。

本地一致性检查与检查器测试（Python 3.10+，只用标准库）：

```bash
python3 scripts/check_agent_design_skills.py
python3 -m unittest discover -s tests/agent_design -v
```

行为回归场景和执行方法见 [评测说明](evals/agent-design/README.md)。一致性检查通过不等于模型行为已经验证；没有跑过模型评测时，不能报告行为通过率。

</details>

### 二、思考方法（6 个）

需要把问题想清楚时用。这一类不产出交付物，作用是调整思路。

| 技能 | 说明 | 附带资料 |
|---|---|:---:|
| `multi-angle-evidence-analysis` | 把六顶思考帽和证据检验结合起来，扩展视角并追踪问题背后的机制 | ✅ |
| `claude-enhanced-logic-thinking` | Claude 深度思考协议 |  |
| `four-deep-thinking-methods` | 4 种深入思考方法 |  |
| `thinking-navigation-assistant` | 思维导航助手 |  |
| `internal-thinking-ai-framework` | 内部思考与 AI 结构框架 |  |
| `enhance-llm-logic-analysis` | 增强 LLM 的逻辑分析 |  |

### 三、分析与洞察（6 个）

需要从材料中得出结论时用。

| 技能 | 说明 | 附带资料 |
|---|---|:---:|
| `business-project-predictor` | 商业项目预判 |  |
| `enterprise-insight-report` | 企业洞察报告 |  |
| `psychological-insight-partner` | 心理洞察伙伴 |  |
| `insight-prompt-investment-analysis` | 投资方向的洞见发现 |  |
| `structural-prompt-scorer` | 结构化提示词评分 |  |
| `reasoning-model-prompt-checker` | 推理模型（O1 / O3-mini）提示词质检 |  |

### 四、提示词工程（8 个）

写、改、评提示词时用。

| 技能 | 说明 | 附带资料 |
|---|---|:---:|
| `prompt-best-practices` | 提示词最佳实践 |  |
| `how-to-write-excellent-prompts` | 优秀提示词的写法 |  |
| `how-to-write-prompts-claude-engineer` | Claude 工程师的提示词技巧 |  |
| `prompt-mother` | CRISPE 框架提示词工程师 |  |
| `efficient-prompt-template-gemini` | 六要素高效提示词模板 |  |
| `universal-system-prompt` | 量子织锦认知引擎框架 |  |
| `chatgpt-tasks-design` | ChatGPT 定时任务设计 |  |
| `chatgpt-voice-agent` | ChatGPT 语音代理 |  |

### 五、内容与创意生产（9 个）

产出可以直接发布的图文、视频、游戏内容时用。

| 技能 | 说明 | 附带资料 |
|---|---|:---:|
| `xiaohongshu-trending-content-script` | 小红书爆款文案 |  |
| `xiaohongshu-platform-card-output` | 小红书风格卡片 |  |
| `wechat-video-trending-content-script` | 微信视频号爆款脚本 |  |
| `lovart-word2videostory` | 把文字脚本转成视频故事板：角色资产、分镜拆解、画面提示词和排版好的故事板 |  |
| `text-to-image-prompt-gen3-runway` | Runway Gen-3 Alpha 视频提示词 |  |
| `visual-model-card-designer` | 视觉模型卡片设计 |  |
| `animal-life-prompt-claude` | 用 SVG 画动物的生命周期 |  |
| `game-design-prompt-rpg-framework` | RPG 游戏框架设计 |  |
| `ming-dynasty-game-prompt` | 明朝历史模拟游戏 |  |

### 六、工作与写作（12 个）

日常交付物：文档、简历、周报、项目规则。

| 技能 | 说明 | 附带资料 |
|---|---|:---:|
| `prd-design-expert` | 产品需求规格说明书（PRD） |  |
| `resume-expert` | 简历优化 |  |
| `reading-summary` | 超可读写作标准：结论先行、倒金字塔 |  |
| `summary-for-week` | 周报整理与复盘总结 |  |
| `software-app-development-core-prompt` | 软件项目开发的核心规则 |  |
| `create-vibe-project` | Vibe Coding 的 8 条工程纪律，用于开新项目或给 AI 编码 agent 立规矩 |  |
| `cto-for-videcoding` | 指导 AI 编码 agent 开发多端数字服务（多角色、合规、支付、AI 集成）。也可作为 `AGENTS.md` 或 `.cursor/rules/` 加载 |  |
| `prohibited-words-detection` | 违禁词和合规检测 |  |
| `ai-communication-methods` | 和 AI 交流的 4 种方式 |  |
| `ai-native-lean-company` | 精益 AI 原生公司 |  |
| `ai-solo-entrepreneur-5phase` | AI 独立创业者的 5 阶段打法：市场洞察、战略落地、执行管理、极速开发、冷启动与全球化验证 |  |
| `lisp-core-syntax` | Lisp 核心语法 |  |

### 七、学习（1 个）

在有限时间内学会一样东西。

| 技能 | 说明 | 附带资料 |
|---|---|:---:|
| `rapid-learn` | 限时快速学习教练，分 6 个阶段：定标 → 地图 → 拆核心 → 实战 → 压力测试 → 沉淀。包含 **domain 模式**（成人学方向、项目、论文、代码仓库）和 **course 模式**（孩子学高中单元：4 节 × 45 分钟、三级提示不直接给答案、出题必验算、不代写作业） | ✅ |

`rapid-learn` 的几个设计要点：

- **先定可检验的交付物**，不追求"4 小时精通"。4 小时现实能拿到的是一张全局地图、一个小产出，并且清楚自己哪里还不懂。
- **防编造**：事实性结论要标来源或标"待核实"；健康医学类内容要标明证据等级。
- **卡关有出口**：同一个点 2 次都没过，就标成 🟡 先往下走，最后统一补。
- **学完能留下东西**：Obsidian 友好的学习笔记、错题本、家长报告，以及第 1/3/7 天的复习题。
- **不用 agent 也能用**：[`assets/prompts/`](rapid-learn/assets/prompts/) 里有可直接粘贴到 ChatGPT、豆包、Kimi 的单条提示词，分[成人版](rapid-learn/assets/prompts/domain-prompt.md)和[孩子版](rapid-learn/assets/prompts/course-kid-prompt.md)。

---

## 怎么跟 Skill 对话

所有 Skill 都是写给 AI 的指令，**不需要学命令或 API**，像平时聊天一样说出需求就行。按使用方式大致分三类：

| 类型 | 你需要提供什么 | 代表技能 | 示例 |
|---|---|---|---|
| 🗣️ 对话型 | 直接说出需求 | `claude-enhanced-logic-thinking`、`prompt-mother`、`psychological-insight-partner` | "帮我分析这个产品定位的逻辑漏洞" |
| 📝 内容生成型 | 主题加素材 | `lovart-word2videostory`、`xiaohongshu-trending-content-script`、`summary-for-week` | "根据下面这段视频脚本生成故事板：……" |
| 🛠️ 工作流型 | 领域上下文和参数 | `prd-design-expert`、`rapid-learn`、`prohibited-words-detection` | "孩子要复习高二数学导数单元，人教 A 版，下周月考" |

内容生成型的通用输入格式（复制后替换内容即可）：

```markdown
[主题/需求：一句话说清楚]
[风格/调性：可选，比如温暖治愈 / 专业严谨 / 幽默轻松]

【核心内容】
- 素材 1：...
- 素材 2：...
- 参考方向：...
```

<details>
<summary><b>完整示例：lovart-word2videostory（点击展开）</b></summary>

**你只需要说：**

```
请根据以下视频脚本，帮我生成一个故事板。
[时长：30秒 | 核心：从"完美的机器"回归"活着的自己"]

【00:00-00:05】
- 画面：日本电车疲惫侧脸 → 办公室鞠躬道歉 → 联络簿评语眉头紧锁
- 视觉大字：害怕不称职，害怕被批评，你多久没有呼吸了？
...
```

**AI 自动产出：**

```
📂 输出目录/
├── 01_项目初始化书.md       ← 时长 / 格式 / 分镜数 / 情绪曲线
├── 02_角色资产库.md         ← 角色描述卡 / 道具清单 / 品牌色
├── 03_分镜拆解.md           ← 每个镜头的时间轴、叙事功能、情绪基调
├── 04_画面提示词.md         ← 10 个维度的标准化生成提示词
└── 06_故事板排版.html       ← 排版好的故事板，浏览器直接打开
```

</details>

---

## 自己写 Skill 的三条硬规矩

都是踩过坑之后总结出来的。

### 1. 触发词必须写在 `description` 里

Agent 决定要不要加载一个 Skill 时，**只能看到 `name` 和 `description`**。自定义字段（比如 `whenToUse`）通常不参与路由，也不会展示给模型。

> 踩过的坑：曾经把"什么时候该用我"写得很详细，但放在了一个自定义字段里，结果模型完全看不到。这相当于把消歧规则写在了选择发生之后。

所以，**希望在哪些场景被用上，就把那些说法写进 `description`**。

### 2. `SKILL.md` 保持聚焦，细节按需加载

入口文件只保留用途、关键决策、必要约束和交付要求。只在特定场景才用到的问法、契约和实现细节，放进 `references/`，并在入口里写明什么时候读取（`rapid-learn` 就是这样把两种模式拆成两个文件的）。

不存在"超过多少行后面就会失效"这种通用阈值。效果要用真实任务中的遵守情况、信息完整度和成本来验证，同时避免规则重复或互相冲突。

### 3. 一个 Skill 只解决一件事

两个 Skill 的触发词重叠，agent 就容易选错。**如果有重叠，至少一方要在 `description` 里写清分工**，比如"本 Skill 只负责 X，Y 请用 `other-skill`"。

---

## 仓库结构与文件规范

```
usingSkills/
├── README.md
├── LICENSE
├── create-skill-file.md          # 技能创建标准与模板
├── <skill-name>/
│   ├── SKILL.md                  # 必需：YAML frontmatter + 指令正文
│   ├── references/               # 可选：按需加载的长参考资料
│   └── assets/                   # 可选：模板、可复制提示词等产出用文件
├── scripts/                      # Agent 设计技能的一致性检查脚本
├── tests/agent_design/           # 检查器单元测试
└── evals/agent-design/           # 行为回归评测场景
```

详细标准见 [`create-skill-file.md`](create-skill-file.md)，要点如下：

- **文件夹命名**：kebab-case，不用空格、下划线或大写字母
- **核心文件**：`SKILL.md`（文件名区分大小写）
- **YAML frontmatter**：必须包含 `name` 和 `description`；可选 `metadata`（`author` 统一为 `pingdior`，另有 `version`）
- **技能文件夹里不放 README**

## 参考

- [Anthropic Agent Skills 官方文档](https://docs.claude.com/en/docs/agents-and-tools/agent-skills)
- 创建新技能：[`create-skill-file.md`](create-skill-file.md)
