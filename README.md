# Manage Skills

一组给 AI agent 用的 **Skill**（可复用任务指令集）。符合 Anthropic 的 Skill 文件规范。

- **作者**：pingdior
- **技能数量**：46 个
- **许可**：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## 快速开始

### 1. 装到你的 agent 里

Skill 就是文件夹。把需要的目录复制到 agent 的 skill 目录即可：

```bash
git clone https://github.com/pingdior/usingSkills /tmp/usingSkills

# 按你用的 agent 选一个目标目录
cp -R /tmp/usingSkills/seed-convergence ~/.dsh/skills/      # DeepSeek Harness
cp -R /tmp/usingSkills/seed-convergence ~/.claude/skills/   # Claude Code
```

> 带 `references/` 的 skill（下表标 ✅）**必须整个文件夹一起复制**，只拷 `SKILL.md` 会丢参考资料。

### 2. 从哪开始

| 你想做的事 | 从这里开始 | 然后 |
|---|---|---|
| 做新产品 / 新业务 | `seed-extraction` | → `seed-convergence` → `digital-life-service-design` |
| 设计 AI Agent 产品 | `digital-life-service-design` | → `harness-design` → `retention-diagnosis-loop` |
| Agent 老是空转 / 烧钱 / 管不住 | `harness-design` | — |
| 把提示词写好 | `prompt-best-practices` | → `how-to-write-excellent-prompts` → `prompt-mother` |
| 一个复杂事想不清楚 | `multi-angle-evidence-analysis` | — |
| 要出小红书 / 视频号内容 | `xiaohongshu-trending-content-script` | → `xiaohongshu-platform-card-output` |

---

## Skill 是怎么工作的（三条硬规矩）

这一节是踩过坑之后总结的，**自己写 skill 时请务必遵守**。

### 1. 触发词必须写在 `description` 里

Agent 决定要不要加载一个 skill 时，**只能看到 `name` 和 `description`**。自定义字段（如 `whenToUse`）通常**不参与路由**，也不会被渲染给模型。

> 我们踩过这个坑：曾经把"什么时候该用我"写得很详细地放在一个自定义字段里，结果模型完全看不到——**等于把消歧规则写在了选择发生之后**。

所以：**要在什么场景被用上，就把那些话写进 `description`。**

### 2. `SKILL.md` 保持聚焦，细节按需加载

入口保留用途、关键决策、必要约束与交付要求；仅在特定场景需要的问法、契约与实现细节放入 `references/`，并说明何时读取。
没有「超过某个行数，后面必然失效」的通用阈值。以真实任务中的遵守情况、信息完整性和成本验证效果，避免重复或互相冲突的规则。

### 3. 一个 skill 只解决一件事

两个 skill 的触发词重叠，agent 就会选错。**重叠时必须有一方在 `description` 里写清分工**（"本 skill 只负责 X，Y 见 `other-skill`"）。

---

## 技能列表（46 个）

### 一、Agent / 系统设计（5 个）

给"做产品的人、做 Agent 的人"用。这一组共享交接契约，按任务和证据缺口选用，不要求每次串行运行全部技能。

| 技能 | 说明 | 参考资料 |
|---|---|:---:|
| `seed-extraction` | 种子提炼：条目类型、四部件、证据与版本化交接契约 | ✅ |
| `seed-convergence` | 交互收敛：按缺口提问、反例检查与下一步信息充分度 | ✅ |
| `digital-life-service-design` | 服务设计：Seed / Harness / Memory、目标取舍与数据流 |  |
| `harness-design` | 运行设计：架构选择、长期运行机制、证据分类与恢复 | ✅ |
| `retention-diagnosis-loop` | 价值与留存诊断：测量、实验、分类型记忆及策略发布 | ✅ |

#### Agent 设计技能 v2 的交接与验证

配套使用时，把这五个文件夹放在同一技能目录，保留各自 `references/`。单独安装仍可分析和出草稿；引用契约不可用时需标记交接缺口，不能假定生产批准。

- [种子契约](seed-extraction/references/seed-contract.md)：种子字段、状态、版本和批准范围的唯一维护来源。
- [运行契约](harness-design/references/runtime-contract.md)：任务状态、工具权限、幂等与恢复。
- [长期运行机制](harness-design/references/long-running-runtime.md)：按需选择上下文工作集、持久重派预算、写入隔离、依赖调度、配额准入、事件索引和告警生命周期。
- [机制证据记录](harness-design/references/mechanism-evidence.json)：27 条机制逐项区分源码行为、已有测试说明与待验证运行收益，另附访谈充分度记录及 8 篇参考来源。
- [测量与实验](retention-diagnosis-loop/references/measurement.md)：事件关联、成熟窗口、基线和实验口径。
- [记忆生命周期](retention-diagnosis-loop/references/memory-lifecycle.md)：个人偏好、推断、经验和策略的不同生效路径。

v1 迁移时补齐类型、范围、证据状态和有效批准记录；不能只升级版本号就宣布旧产物获批。Harness 统一指运行时外壳，环境接入是其工具 / 适配子部分。

长期运行增补后，`harness-design` 与 `seed-convergence` 为 2.1.0，其余三项为 2.0.0；交接协议仍为 `seed/v2`。
这些是设计技能，不是底层 Harness 实现。证据记录中的 `article_reported` 只表示文章转述，不表示本仓库直接复核源码提交或复跑测试；运行收益目前均为 `unmeasured`，不得从结构校验推算生产效果。

本地一致性检查与检查器测试（Python 3.10+，仅标准库）：

```bash
python3 scripts/check_agent_design_skills.py
python3 -m unittest discover -s tests/agent_design -v
```

行为回归场景与执行方法见 [评测说明](evals/agent-design/README.md)。一致性检查通过不等于模型行为已验证；未运行模型评测时不得报告行为通过率。

### 二、思考方法（6 个）

需要"想清楚"时用。这些不产出交付物，只改变你的思路。

| 技能 | 说明 | 参考资料 |
|---|---|:---:|
| `multi-angle-evidence-analysis` | 融合六顶思考帽与证据检验，扩展视角并追踪问题机制 | ✅ |
| `claude-enhanced-logic-thinking` | Claude 深度思考协议 |  |
| `four-deep-thinking-methods` | 4 个深入思考方法 |  |
| `thinking-navigation-assistant` | 思维导航助手 |  |
| `internal-thinking-ai-framework` | 内部思考与 AI 结构框架 |  |
| `enhance-llm-logic-analysis` | LLM 逻辑分析增强 |  |

### 三、分析与洞察（6 个）

需要从材料里得出结论时用。

| 技能 | 说明 | 参考资料 |
|---|---|:---:|
| `business-project-predictor` | 商业项目预判 |  |
| `enterprise-insight-report` | 企业洞察报告 |  |
| `psychological-insight-partner` | 心理洞察伙伴 |  |
| `insight-prompt-investment-analysis` | 洞见发现 |  |
| `structural-prompt-scorer` | 结构提示词评分专家 |  |
| `reasoning-model-prompt-checker` | O1/O3-mini 提示词质检 |  |

### 四、提示词工程（8 个）

写、改、评提示词时用。

| 技能 | 说明 | 参考资料 |
|---|---|:---:|
| `prompt-best-practices` | 提示词最佳实践 |  |
| `how-to-write-excellent-prompts` | 优秀提示词法则 |  |
| `how-to-write-prompts-claude-engineer` | Claude 工程师提示词技巧 |  |
| `prompt-mother` | CRISPE 提示词工程师 |  |
| `efficient-prompt-template-gemini` | 六要素高效提示词模版 |  |
| `universal-system-prompt` | 量子织锦认知引擎框架 |  |
| `chatgpt-tasks-design` | ChatGPT 定时任务设计 |  |
| `chatgpt-voice-agent` | ChatGPT 语音代理 |  |

### 五、内容与创意生产（9 个）

产出可直接发布的图文/视频/游戏内容时用。

| 技能 | 说明 | 参考资料 |
|---|---|:---:|
| `xiaohongshu-trending-content-script` | 小红书爆款文案 |  |
| `xiaohongshu-platform-card-output` | 小红书风格卡片 |  |
| `wechat-video-trending-content-script` | 微信视频号爆款脚本 |  |
| `text-to-image-prompt-gen3-runway` | Gen-3 Alpha Runway 视频提示 |  |
| `visual-model-card-designer` | 视觉模型卡片设计 |  |
| `lovart-word2videostory` | 文字→视频故事板生成技能 — 输入任意视频脚本/文案，自动产出角色资产+分镜拆解+画面提示词+专业排版故事板 |  |
| `animal-life-prompt-claude` | 动物生命周期 SVG |  |
| `game-design-prompt-rpg-framework` | RPG 游戏框架设计 |  |
| `ming-dynasty-game-prompt` | 明朝历史模拟游戏 |  |

### 六、工作与写作（12 个）

日常交付物：文档、简历、周报、项目宪法。

| 技能 | 说明 | 参考资料 |
|---|---|:---:|
| `prd-design-expert` | 产品需求规格说明书专家 |  |
| `resume-expert` | 简历专家 |  |
| `reading-summary` | 超可读写作标准 |  |
| `summary-for-week` | 周报整理与复盘总结 |  |
| `software-app-development-core-prompt` | 软件项目开发核心宪法 |  |
| `cto-for-videcoding` | (无 description) |  |
| `prohibited-words-detection` | 违禁词/合规检测 |  |
| `ai-communication-methods` | 4 种 AI 交流方式 |  |
| `ai-native-lean-company` | 精益 AI 原生公司 |  |
| `ai-solo-entrepreneur-5phase` | AI赋能独立创业者的5阶段作战体系 — 市场洞察、战略落地、执行管理、极速开发、冷启动与… |  |
| `create-vibe-project` | Vibe Engineering Discipline v1.0 — 8 princip… |  |
| `lisp-core-syntax` | Lisp 核心语法 |  |

## 使用方式

### 两步上手

```
① 把需要的 skill 文件夹复制到 Claude/Cursor 的 skills 目录
② 直接对话，AI 会自动识别并激活对应技能
```

> 所有 skill 文件都是 AI 指令，**不需要学习命令或 API**。直接像聊天一样说你的需求即可。

---

### 按类型查看使用说明

这里的 40+ 个技能分三类，每类的使用方式略有不同：

#### 🗣️ 对话型技能 — 直接聊就行

> 不需要特定输入格式，在日常对话中表达需求即可触发。

**典型技能：**
- `claude-enhanced-logic-thinking` — 深度逻辑推理
- `prompt-mother` — CRISPE 提示词优化
- `psychological-insight-partner` — 心理洞察对话
- `structural-prompt-scorer` — 提示词评分
- `enhance-llm-logic-analysis` — 逻辑分析增强
- `how-to-write-excellent-prompts` — 提示词技巧

**使用示例：**
```
用户："帮我分析一下这个产品定位的逻辑漏洞"
→ AI 自动激活 claude-enhanced-logic-thinking 进行深度推理

用户："帮我优化一下这个提示词，让它更结构化和高效"
→ AI 自动激活 prompt-mother 进行 CRISPE 转换
```

> 📌 这些技能在 SKILL.md 中写明了触发短语。你不需要记住它们——AI 会判断是否匹配。

---

#### 📝 内容生成型技能 — 给出主题/素材

> 需要提供具体的内容主题、文案或参考材料。AI 会用结构化管线生成完整输出。

**典型技能：**
- `lovart-word2videostory` — 视频故事板生成（演示示例👇）
- `wechat-video-trending-content-script` — 视频号爆款脚本
- `xiaohongshu-trending-content-script` — 小红书爆款文案
- `xiaohongshu-platform-card-output` — 小红书风格卡片
- `text-to-image-prompt-gen3-runway` — Runway 视频提示词
- `reading-summary` — 结构化阅读摘要
- `summary-for-week` — 周报生成

**通用输入格式示例（复制后替换内容即可）：**

```markdown
[主题/需求：一句话说清楚]
[风格/调性：可选，如温暖治愈/专业严谨/幽默轻松]

【核心内容】
- 素材 1：...
- 素材 2：...
- 参考方向：...
```

> 💡 输入不完整也没关系，AI 会自动补充分镜、时间分配、结构等缺失信息。

---

#### 🛠️ 工作流型技能 — 提供上下文/参数

> 需要提供特定领域的上下文信息，AI 会按预设 SOP 执行。

**典型技能：**
- `prd-design-expert` — 产品需求文档生成
- `enterprise-insight-report` — 企业洞察报告
- `insight-prompt-investment-analysis` — 投资分析
- `business-project-predictor` — 商业项目预判
- `resume-expert` — 简历优化
- `game-design-prompt-rpg-framework` — RPG 游戏设计
- `ming-dynasty-game-prompt` — 明朝历史模拟游戏
- `prohibited-words-detection` — 违禁词检测
- `visual-model-card-designer` — 视觉卡片设计

**使用示例：**
```
用户："帮我写一份 AI 陪伴类产品的 PRD，目标用户是高压职场人"
→ AI 按 PRD 模板生成完整文档

用户："帮我看一下这段文案有没有违禁词和合规风险"
→ AI 启动违禁词检测流程
```

> 📌 每步该做什么不需要你操心——AI 会按 SKILL.md 中的 SOP 自动推进。

---

### 🎯 最佳实践示例：lovart-word2videostory

以这个技能为例，展示内容生成型的完整使用路径：

**你只需要说：**

```
请根据以下视频脚本，帮我生成一个故事板。
[时长：30秒 | 核心：从"完美的机器"回归"活着的自己"]

【00:00-00:05】
- 画面：日本电车疲惫侧脸 → 办公室鞠躬道歉 → 联络簿评语眉头紧锁
- 视觉大字：害怕不称职，害怕被批评，你多久没有呼吸了？
...
```

**AI 全自动产出：**

```
📂 输出目录/
├── 01_项目初始化书.md       ← 时长/格式/分镜数/情绪曲线
├── 02_角色资产库.md         ← 角色描述卡/道具清单/品牌色
├── 03_分镜拆解.md           ← 每镜时间轴+叙事功能+情绪基调
├── 04_画面提示词.md         ← 10维度标准化生成提示词
└── 06_故事板排版.html       ← 专业排版(浏览器直接打开)
```

---

---

## Skill 文件规范

遵循 `create-skill-file.md` 中定义的标准：

- **文件夹命名**：kebab-case，无空格 / 下划线 / 大写
- **核心文件**：`SKILL.md`（大小写敏感）
- **YAML Frontmatter**：必须含 `name`、`description`；可选 `metadata`（author、version）
- **metadata.author**：统一为 `pingdior`
- **可选 `references/`**：放长参考资料，按需加载
- **无 README.md**：技能文件夹内不放 README

## 项目结构

```
manage-skills/
├── README.md
└── usingSkills/
    ├── create-skill-file.md    # 技能创建标准与模板
    └── [skill-name]/
        ├── SKILL.md            # 技能核心文件
        └── references/         # 可选：长参考资料
```

---

## 参考

- 创建新技能：`create-skill-file.md`
- Cursor Skill 规范：`~/.cursor/skills-cursor/create-skill/SKILL.md`
- Anthropic Agent Skills 官方文档：https://docs.claude.com/en/docs/agents-and-tools/agent-skills
