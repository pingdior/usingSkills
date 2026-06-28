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

将需要的技能文件夹复制到 Cursor/Claude 的技能目录，或直接引用 `usingSkills/[skill-name]/SKILL.md` 作为提示词模板。

### 💡 用户需要提供什么？

每个技能要求不同的输入，请阅读对应 SKILL.md 中的**触发条件**（Trigger Conditions）部分。

以 `lovart-word2videostory`（视频故事板生成）为例，你需要提供以下几种格式之一：

| 输入类型 | 示例 |
|---------|------|
| **完整视频脚本**（包含时间轴、画面、旁白、音效的完整分镜级脚本） | 见下方参考 |
| **文案/旁白稿**（只有文字，需要 AI 帮你拆解分镜） | 一段30秒广告旁白稿，描述产品功能 |
| **产品/品牌需求**（只有描述，需要从零生成整个创意） | "为冥想App做一个15秒宣传视频" |
| **参考脚本** | 一段YouTube视频文字记录，转化为故事板 |

**参考输入格式（复制以下结构直接使用）：**

```markdown
[时长：30秒 | 风格：温暖治愈 | 格式：9:16竖屏]
[核心信息：一句话说清楚要传达什么]

【00:00-00:05】场景1描述...
- 画面：...
- 旁白：...
- 声音/音效：...

【00:05-00:12】场景2描述...
...
```

> 💡 如果输入不完整（如只有文案没有时间分配），AI 会自动补齐缺失信息。

## 参考

- 创建新技能：参考 `usingSkills/create-skill-file.md`
- Cursor Skill 规范：`~/.cursor/skills-cursor/create-skill/SKILL.md`
