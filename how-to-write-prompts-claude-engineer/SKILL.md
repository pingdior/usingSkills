---
name: how-to-write-prompts-claude-engineer
description: Anthropic engineers' best practices for prompt writing. Use when improving prompts, teaching prompt engineering, or understanding model interaction. Trigger phrases: "Claude工程师", "提示词技巧", "不要角色扮演", "实话实说"
metadata:
  author: woodgaya@gmail.com
  version: 1.0.0
---

# How to Write Prompts - Claude Engineer Insights

## Overview

Anthropic prompt engineers' key principles: clear communication, iteration, honesty with models, no unnecessary role-play.

## Core Principles

### 1. Clear Communication
- Write very clear task descriptions, not abstract constructs
- Articulate clearly so model understands the task
- Organize everything you know but model doesn't, then write it down

### 2. Iteration
- Prompt engineering = trial and error process
- Willingness to iterate and observe is critical
- Test edge cases: empty input, unusual data, boundary conditions
- When model errs: ask "Why did you get this wrong? Can you help fix my prompt?"

### 3. No Role-Play Needed
- As models improve, no need to lie to them
- Don't pretend "I'm a teacher giving a quiz" - say "I'm building an LLM evaluation dataset"
- Imagine a capable temp worker with little context - describe your task directly
- Record yourself explaining the task, transcribe, paste into prompt - often works better

### 4. Trust Model Capability
- Don't treat model like a child; don't over-simplify
- Models can understand complex information
- Give papers directly instead of simplified "baby version"
- Respect model's ability to handle context

### 5. When to Give Up
- Some tasks: every adjustment pushes result further from goal → abandon
- Better to wait for next model than spend months on unsolvable prompt

## Research vs Consumer Prompts

- **Research**: Fewer examples, seek diversity, explore model boundaries
- **Consumer**: Many examples, prioritize stability and consistency
- **Enterprise**: Must handle millions of uses, consider all edge cases

## Usage Example

**User input**: "我的提示词效果不好，怎么改进？"
**AI action**: Applies principles - clarify task, test edge cases, try transcribing verbal explanation, avoid role-play shortcuts
**Expected result**: Improved prompt with clear task description and edge case handling
