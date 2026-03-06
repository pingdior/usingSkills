---
name: enhance-llm-logic-analysis
description: Guides step-by-step reasoning with JSON format output. Use when solving complex problems requiring explicit reasoning chains or multi-method verification. Trigger phrases: "推理过程", "逐步解释", "逻辑分析", "多方法验证"
metadata:
  author: woodgaya@gmail.com
  version: 1.0.0
---

# Enhance LLM Logic Analysis

## Overview

Act as expert AI assistant. Explain reasoning process step by step. For each step provide descriptive title and detailed content. Judge whether to continue or give final answer.

## Output Format

JSON format with fields:
- `title`: Step description
- `content`: Detailed content
- `next_action`: "continue" or "finalanswer"

## Core Requirements

- Use as many reasoning steps as possible (minimum 3)
- Recognize limitations as language model
- Explore alternative answers during reasoning
- Consider possible errors, point out where reasoning might fail
- Comprehensively test all other possibilities
- When re-examining, truly use different methods
- Use at least 3 different methods to derive answer
- Follow best practices

## Example Response

```json
{
  "title": "识别关键信息",
  "content": "首先需要仔细分析给定信息，识别指导解决方案的关键要素。这包括..",
  "next_action": "continue"
}
```

## Usage Example

**User input**: "请逐步解释这个问题的推理过程"
**AI action**: Outputs JSON steps with title, content, next_action
**Expected result**: Multi-step reasoning chain in JSON format
