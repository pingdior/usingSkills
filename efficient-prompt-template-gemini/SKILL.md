---
name: efficient-prompt-template-gemini
description: Defines a six-element efficient prompt structure (Role, Background, Task, Requirements, Example, Reflection) for Gemini and similar LLMs. Use when writing prompts, optimizing AI outputs, or teaching prompt engineering. Trigger phrases: "提示词结构", "高效提示词", "prompt模版", "六要素"
metadata:
  author: woodgaya@gmail.com
  version: 1.0.0
---

# Efficient Prompt Template (Gemini)

## Overview

An efficient prompt structure contains six core elements that maximize AI output quality.

## Six Core Elements

### 1. Role
- **Purpose**: Assign the AI a specific identity or expert perspective
- **Example**: "你是一个资深文案"、"你是一位某领域专家"

### 2. Background
- **Purpose**: Provide task context, scenario, target audience
- **Example**: "我正在某个场景下，需要……"、"我的受众是某类人群"

### 3. Task
- **Purpose**: Clearly state the core action the AI must perform
- **Example**: "我希望你执行一个动作，如分析、撰写、总结"

### 4. Requirements
- **Purpose**: Define output constraints (most critical for refinement)
  - Style: formal, informal, humorous, professional
  - Format: list, table, JSON, code block
  - Structure: introduction, body, conclusion
  - Perspective: first person, third person
  - Language: Chinese, English, mixed
  - Length: 500 words, three paragraphs
  - Citations:是否需要引用来源、数据支持
  - Others: bold key points, code highlighting

### 5. Example
- **Purpose**: Provide positive or negative examples for quick understanding
- **Example**: "例如：(提供一个具体例子)"

### 6. Reflection
- **Purpose**: Guide AI self-optimization or追问
- **Example**: "请对我刚才的提问进行评分"、"你需要我提供更多信息吗？"

## Complete Structure Template

> "你是一个 **[角色]**，我正在 **[背景]** 下，需要你执行 **[任务]**。请你按照 **[要求]**（包括风格、格式、长度等）来完成，这里有一个 **[示例]** 供你参考。最后，请 **[反思]** 你的输出是否满足要求。"

## Usage Example

**User input**: "帮我写一个产品介绍的提示词"
**AI action**: Applies six-element structure, generates complete prompt
**Expected result**: Structured prompt with Role, Background, Task, Requirements, Example, Reflection
