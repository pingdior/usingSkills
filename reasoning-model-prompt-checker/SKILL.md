---
name: reasoning-model-prompt-checker
description: Quality-checks prompts for O1/O3-mini reasoning models. Use when optimizing prompts for OpenAI O1, O3-mini, or similar deep-reasoning models. Trigger phrases: "推理模型", "O1", "O3-mini", "提示词质检"
metadata:
  author: woodgaya@gmail.com
  version: 1.0.0
---

# Reasoning Model Prompt Checker

## Overview

Professional prompt quality checker for models with built-in deep reasoning (OpenAI O1, O3-mini). Ensures prompts have clear goals, sufficient context, and proper model-specific optimization.

## Workflow

### 1. Receive Prompt
- Diagnose clarity of user's prompt/requirements
- Guide user to clarify intent if vague
- Example questions: What specific problem? Expected output type? Target audience? Requirements?

### 2. Task Complexity and Model Selection
- **Simple (≤3 steps)**: O3-mini, concise prompts
- **Medium (3-5 steps)**: Adjust description and context
- **Complex (≥5 steps)**: O1, full background and constraints
- **Data volume**: ≤128k either; 128k-200k must use O3-mini; >200k requires preprocessing

### 3. Multi-Dimensional Analysis
- **Goal**: Clear, specific, SMART
- **Return Format**: Clear, parseable (JSON, list, table)
- **Constraints**: Necessary, reasonable (avoid over-restriction)
- **Context**: Sufficient, relevant, avoid redundancy
- **Model fit**: Remove chain-of-thought prompts like "let's think step by step"

### 4. Output Report
- Prompt ID
- Overall assessment (priority: high/medium/low)
- Detailed analysis: structure, content quality, model fit
- Optimization suggestions with examples

## Parameter Suggestions

- **reasoning_effort**: low/medium/high by task complexity
- **max_completion_tokens**: 500-25000
- **temperature**: ≤0.3 for stability

## Key Notes

1. Avoid redundant chain prompts ("let's think step by step") - they interfere with built-in reasoning
2. Adjust for task type (legal, math, coding)
3. Maintain consistent output format

## Usage Example

**User input**: "帮我检查这个给O1用的提示词"
**AI action**: Analyzes structure, content, model fit; outputs report with optimization suggestions
**Expected result**: Quality report with prioritized issues and improvement examples
