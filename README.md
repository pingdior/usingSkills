# Manage Skills

技能管理项目，包含符合 Anthropic 官方标准的 Claude Skill 文件集合。

- **作者**：woodgaya@gmail.com
- **技能数量**：36 个

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

## 技能列表（36 个）

| 技能名称 | 描述 |
|---------|------|
| universal-system-prompt | 量子织锦认知引擎框架 |
| efficient-prompt-template-gemini | 六要素高效提示词模版 |
| reading-summary | 超可读写作标准 |
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
| role-prompt-mother | CRISPE 提示词工程师 |
| role-structural-prompt-scorer | 结构提示词评分专家 |
| role-prd-design-expert | 产品需求规格说明书专家 |
| role-resume-expert | 简历专家 |
| role-psychological-insight-partner | 心理洞察伙伴 |
| role-business-project-predictor | 商业项目预判 |
| role-enterprise-insight-report | 企业洞察报告 |
| ming-dynasty-game-prompt | 明朝历史模拟游戏 |
| text-to-image-prompt-gen3-runway | Gen-3 Alpha Runway 视频提示 |
| how-to-write-prompts-claude-engineer | Claude 工程师提示词技巧 |
| how-to-write-excellent-prompts | 优秀提示词法则 |
| coze-prompt-writing | Coze 平台提示词 |
| animal-life-prompt-claude | 动物生命周期 SVG |
| internal-thinking-ai-framework | 内部思考与 AI 结构框架 |
| key-prompt-best-practices | 提示词最佳实践 |
| chatgpt-voice-agent | ChatGPT 语音代理 |
| chatgpt-tasks-design | ChatGPT 定时任务设计 |
| lisp-core-syntax | Lisp 核心语法 |
| key-ai-communication-methods | 4 种 AI 交流方式 |
| ai-native-lean-company | 精益 AI 原生公司 |
| four-deep-thinking-methods | 4 个深入思考方法 |

## 使用方式

将需要的技能文件夹复制到 Cursor/Claude 的技能目录，或直接引用 `usingSkills/[skill-name]/SKILL.md` 作为提示词模板。

## 参考

- 创建新技能：参考 `usingSkills/create-skill-file.md`
- Cursor Skill 规范：`~/.cursor/skills-cursor/create-skill/SKILL.md`
