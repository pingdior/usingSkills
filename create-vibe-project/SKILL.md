---
name: create-vibe-project
description: Vibe Engineering Discipline v1.0 — 8 principles for disciplined AI-assisted "Vibe Coding". Use this skill when starting a new vibe-coding project, setting ground rules with an AI coding agent, or onboarding a team to structured AI collaboration.
metadata:
  author: woodgaya@gmail.com
  version: 1.0.0
---

# Vibe Engineering Discipline v1.0

## When to Use

- Starting a new project where AI will do most of the coding
- Setting up guardrails for an AI coding agent (Claude Code, Codex, Cursor, etc.)
- Onboarding a team to structured, disciplined vibe coding
- Reviewing if a project's AI collaboration setup is missing key disciplines

## The 8 Principles

### 原则 1: Think Before Coding

> **若需求模糊，先列出至少 2 种假设，询问用户后再编码。不得擅自猜测业务逻辑。**

- 面对模糊需求时，AI 必须主动提出 2+ 种可能的解释
- 用户确认方向后，才能开始实现
- 禁止"我认为用户想要的是 X……"的猜测式开发

**Checklist:**
- [ ] 需求文档是否明确？是否有歧义点？
- [ ] 已列出至少 2 种假设供用户选择？
- [ ] 用户已明确确认方向？

---

### 原则 2: Simplicity First

> **禁用 speculative features。单次逻辑无需抽象，除非已有 3 处重复。优先用语言内置特性，不引入额外库。**

- 不写"将来可能会用到"的代码
- 重复 3 次以下不要提取抽象（不要过早抽象）
- 优先用标准库/语言原生特性，第三方库要有充分理由

**Checklist:**
- [ ] 每个新增依赖都有明确必要性？
- [ ] 没有"万一以后要用"的预留代码？
- [ ] 抽象是否真的有 3+ 处重复支撑？

---

### 原则 3: Surgical Changes

> **单次修改 ≤3 文件。不改未涉及的代码格式、注释、空行。任何重构需用户明确批准。**

- 一次提交/一次对话，只改核心逻辑涉及的文件
- 不要顺手格式化、重命名、删注释
- 重构 = 用户说"重构"才算

**Checklist:**
- [ ] 本次修改涉及几个文件？（≤3）
- [ ] 是否有不在 scope 内的代码被误改？
- [ ] 如果有重构，用户批准了吗？

---

### 原则 4: Goal-Driven + Verify

> **提交前必须运行 `npm test` 并附结果。提供测试通过的证据（截图/日志）。**

- 修改实现后必须跑测试
- 测试结果必须可见（终端输出日志）
- 如果测试失败，先修复再提交

**Checklist:**
- [ ] `npm test` 已运行？
- [ ] 结果是 pass 还是 fail？
- [ ] 测试日志/截图已保留？

---

### 原则 5: Dogfooding (Human Verification)

> **修改后，用户必须手动走一遍核心流程。AI 应输出「需要人工验证的核心路径清单」。**

- AI 完成修改后，输出一份人工验证清单
- 用户必须亲自走一遍核心流程来确认
- 未经验证不得合并/部署

**核心路径清单模板：**

```markdown
## 需要人工验证的核心路径
1. [ ] 打开首页，确认页面正常加载
2. [ ] 点击 [功能 X]，确认流程走通
3. [ ] 输入 [异常值]，确认边界处理符合预期
4. [ ] 检查控制台无报错
5. [ ] 其他：___________
```

**Checklist:**
- [ ] 已输出人工验证清单？
- [ ] 用户已手动验证？
- [ ] 验证结果确认通过？

---

### 原则 6: Context Freshness

> **每次新对话开始时，自动读取 `ARCHITECTURE_GUIDE.md`。若上下文超限，主动总结并保存至 `session-summary.md`。**

- 每次新对话自动加载架构文档
- 当 token 使用接近限制时，主动总结当前进度
- 将总结写入 `session-summary.md` 供下次对话使用

**Checklist:**
- [ ] `ARCHITECTURE_GUIDE.md` 已读取？
- [ ] 上下文长度是否健康？
- [ ] 是否需要写 `session-summary.md`？

---

### 原则 7: Contract as Test

> **使用 TypeScript 严格模式 + Zod schema。修改公共接口时，同步更新对应的 OpenAPI spec。契约变更必须通过 `scripts/verify-contracts.sh`。**

- TypeScript `strict: true`
- 运行时数据验证用 Zod
- 公开 API 接口变更必须同步更新 OpenAPI 文档
- 契约验证脚本必须通过

**Checklist:**
- [ ] `tsconfig.json` 中 `strict: true`？
- [ ] 外部接口有 Zod schema 验证？
- [ ] OpenAPI spec 与实现一致？
- [ ] `scripts/verify-contracts.sh` 通过？

---

### 原则 8: Reversibility & Rollback Anchors

> **每次独立功能修改后，执行 `git tag vibe-$(date +%Y%m%d)-<feature-name>`。所有修改必须能在单个 `git revert <tag>` 内完全撤销。**

- 每个功能点完成后打 tag
- tag 命名格式：`vibe-YYYYMMDD-<feature-name>`
- 确保一次 revert 就能完全回退，不需要逐个文件处理

**Checklist:**
- [ ] 当前功能已打 tag？（格式：`vibe-20260101-feature-name`）
- [ ] `git revert <tag>` 是否能干净回退？
- [ ] 该 tag 范围内是否混入了无关修改？

---

## 项目初始化模板

在项目根目录创建 `VIBE_DISCIPLINE.md`，写入以下内容：

```markdown
# Vibe Engineering Discipline v1.0

本项目的 AI 编程遵循以下原则：

| # | 原则 | 核心要求 |
|---|------|---------|
| 1 | Think Before Coding | 模糊需求先列假设，不猜测 |
| 2 | Simplicity First | 禁用 speculative features |
| 3 | Surgical Changes | 单次改 ≤3 文件 |
| 4 | Goal-Driven + Verify | 提交前跑测试 |
| 5 | Dogfooding | 人工验证核心路径 |
| 6 | Context Freshness | 每次读 ARCHITECTURE_GUIDE.md |
| 7 | Contract as Test | TypeScript strict + Zod |
| 8 | Reversibility & Rollback Anchors | 每个功能打 tag |
```

同时创建 `scripts/verify-vibe.sh`：

```bash
#!/bin/bash
# Vibe Engineering 合规检查
set -euo pipefail

echo "=== Vibe Compliance Check ==="

# 检查 ARCHITECTURE_GUIDE.md
if [ ! -f "ARCHITECTURE_GUIDE.md" ]; then
  echo "[WARN] ARCHITECTURE_GUIDE.md 不存在"
fi

# 检查 TypeScript strict mode
if [ -f "tsconfig.json" ]; then
  if grep -q '"strict": true' tsconfig.json 2>/dev/null; then
    echo "[OK] TypeScript strict mode enabled"
  else
    echo "[FAIL] TypeScript strict mode not enabled"
  fi
fi

# 检查最近是否有 tag
latest_tag=$(git tag -l 'vibe-*' --sort=-version:refname 2>/dev/null | head -1)
if [ -n "$latest_tag" ]; then
  echo "[OK] Latest vibe tag: $latest_tag"
else
  echo "[WARN] No vibe-* tags found"
fi

echo "=== Done ==="
```

## 与 AI Agent 的交互提示

使用 Claude Code / Codex / Cursor 等 AI 编程工具时，在 `.claude.md` 或项目 prompt 中声明：

```
This project follows Vibe Engineering Discipline v1.0. 
Before each code change, read the 8 principles from VIBE_DISCIPLINE.md.
```

## 常见陷阱

1. **原则 1 最容易被忽略** — AI 倾向于直接干活而不是先问清楚。需要项目 prompt 中特别强调。
2. **原则 2 & 3 相辅相成** — 简单 + 精准修改，两者一起做效果最好。
3. **原则 4 容易被跳过** — 如果测试很慢或不稳定，AI 倾向于找借口不跑。可以拆成快慢测试。
4. **原则 5 不是可选项** — 这是人类保持对项目控制权的最低保障。跳过此原则 = 失去项目所有权。
5. **原则 8 在多人协作时更重要** — 清晰的回滚锚点让整个团队敢于更快地实验。
