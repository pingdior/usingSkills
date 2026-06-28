# Manage Skills

技能管理项目，包含符合 Anthropic 官方标准的 Claude Skill 文件集合。

- **作者**：woodgaya@gmail.com
- **技能数量**：37 个

## 项目结构

```
manage-skills/
├── README.md
└── usingSkills/
    ├── create-skill-file.md    # 技能文件创建标准与模板
    └── [skill-name]/           # 各技能文件夹（kebab-case 命名）
        └── SKILL.md            # 技能核心文件
```

## 技能格式规范

每个技能遵循 `create-skill-file.md` 中定义的标准：

- **文件夹命名**：kebab-case，无空格/下划线/大写
- **核心文件**：`SKILL.md`（大小写敏感）
- **YAML Frontmatter**：包含 `name`、`description`，可选 `metadata`（author、version）
- **metadata.author**：统一为 `woodgaya@gmail.com`
- **无 README.md**：技能文件夹内不包含 README

## 技能列表（37 个）

| 技能名称 | 描述 |
|---------|------|
| universal-system-prompt | 量子织锦认知引擎框架 |
| efficient-prompt-template-gemini | 六要素高效提示词模版 |
| reading-summary | 超可读写作标准 |
| summary-for-week | 周报整理与复盘总结 |
| prohibited-words-detection | 违禁词/合规检测 |
| software-app-development-core-prompt | 软件项目开发核心宪法 |
| claude-enhanced-logic-thinking | Claude 深度思考协议 |
| visual-model-card-designer | 视觉模型卡片设计 |
| game-design-prompt-rpg-framework | RPG 游戏框架设计 |
| insight-prompt-investment-analysis | 洞见发现 |
| enhance-llm-logic-analysis | LLM 逻辑分析增强 |
| reasoning-model-prompt-checker | O1/O3-mini 提示词质检 |
| thinking-navigation-assistant | 思维导航助手 |
| wechat-video-trending-content-script | 微信视频号爆款脚本 |
| xiaohongshu-platform-card-output | 小红书风格卡片 |
| xiaohongshu-trending-content-script | 小红书爆款文案 |
| prompt-mother | CRISPE 提示词工程师 |
| structural-prompt-scorer | 结构提示词评分专家 |
| prd-design-expert | 产品需求规格说明书专家 |
| resume-expert | 简历专家 |
| psychological-insight-partner | 心理洞察伙伴 |
| business-project-predictor | 商业项目预判 |
| enterprise-insight-report | 企业洞察报告 |
| ming-dynasty-game-prompt | 明朝历史模拟游戏 |
| text-to-image-prompt-gen3-runway | Gen-3 Alpha Runway 视频提示 |
| how-to-write-prompts-claude-engineer | Claude 工程师提示词技巧 |
| how-to-write-excellent-prompts | 优秀提示词法则 |
| animal-life-prompt-claude | 动物生命周期 SVG |
| internal-thinking-ai-framework | 内部思考与 AI 结构框架 |
| prompt-best-practices | 提示词最佳实践 |
| chatgpt-voice-agent | ChatGPT 语音代理 |
| chatgpt-tasks-design | ChatGPT 定时任务设计 |
| lisp-core-syntax | Lisp 核心语法 |
| ai-communication-methods | 4 种 AI 交流方式 |
| ai-native-lean-company | 精益 AI 原生公司 |
| lovart-word2videostory | 文字→视频故事板生成技能 — 输入任意视频脚本/文案，自动产出角色资产+分镜拆解+画面提示词+专业排版故事板 |
| four-deep-thinking-methods | 4 个深入思考方法 |

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
- `mindring-growth-system` — MINDRING 增长体系
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

## 参考

- 创建新技能：参考 `usingSkills/create-skill-file.md`
- Cursor Skill 规范：`~/.cursor/skills-cursor/create-skill/SKILL.md`
