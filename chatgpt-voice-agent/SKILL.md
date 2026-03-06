---
name: chatgpt-voice-agent
description: Creates prompts for ChatGPT voice agents with personality, tone, and state machine. Use when building voice agents, defining conversation flows, or OpenAI Realtime API. Trigger phrases: "语音代理", "voice agent", "ChatGPT语音", "state machine"
metadata:
  author: woodgaya@gmail.com
  version: 1.0.0
---

# ChatGPT Voice Agent Prompt

## Overview

Creates LLM prompts for high-quality voice agents. Follows OpenAI Realtime Agents format with Personality/Tone and Conversation State Machine.

## Output Format

### Personality and Tone
- Identity, Task, Demeanor, Tone
- Level of Enthusiasm, Formality, Emotion
- Filler Words (none/occasionally/often/very often)
- Pacing, Other details

### Instructions
- Follow Conversation States
- Repeat back name/phone for confirmation
- Acknowledge corrections straightforwardly

### Conversation States
State machine with: id, description, instructions, examples, transitions (next_step, condition)

## Workflow

1. **Step 1** (optional): Ask clarifying questions for unspecified Personality/Tone qualities. Offer 3 options per quality.
2. **Step 2**: Output full prompt. State machine based ONLY on explicit user steps. No code block around state_machine.

## State Machine Schema

```json
{
  "id": "unique_step_id",
  "description": "step purpose",
  "instructions": ["what agent does"],
  "examples": ["example utterances"],
  "transitions": [{"next_step": "id", "condition": "when"}]
}
```

## Usage Example

**User input**: "创建一个客服语音代理，需要收集姓名和验证信息"
**AI action**: Asks personality questions if needed, outputs full prompt with state machine (greeting → get first name → get last name → verify → next steps)
**Expected result**: Complete voice agent prompt ready for ChatGPT/Realtime API
