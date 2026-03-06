---
name: coze-prompt-writing
description: Coze.cn platform prompt writing guidelines. Use when building Coze agents, defining input/output variables, or aligning JSON output with database schema. Trigger phrases: "coze", "Coze提示词", "智能体", "输出变量"
metadata:
  author: woodgaya@gmail.com
  version: 1.0.0
---

# Coze.cn Prompt Writing

## Overview

Guidelines for writing prompts in Coze platform. Focus on variable format alignment between agent output and final output.

## Key Rules

1. **Variable Output**: Must use JSON format for variable operations
2. **Agent Description**: Describe JSON format in agent; one-to-one match with output variables
3. **Alignment**: Agent-defined output format must align with output variable format
4. **Database**: If data cannot be stored in DB, output variable format should still match DB schema
5. **User Prompt Module**: Define input variable format, output variable format, and usage

## Usage Example

**User input**: "在Coze里怎么设置智能体的输出变量？"
**AI action**: Explains JSON format requirement, variable matching, alignment with DB schema
**Expected result**: Clear Coze prompt/variable configuration guidance
