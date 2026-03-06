---
name: chatgpt-tasks-design
description: ChatGPT Scheduled Tasks (automations) system prompt design. Use when implementing task scheduling, reminders, or iCal VEVENT format. Trigger phrases: "ChatGPT Tasks", "scheduled tasks", "automations", "RRULE"
metadata:
  author: woodgaya@gmail.com
  version: 1.0.0
---

# ChatGPT Tasks Design

## Overview

ChatGPT uses "automations" tool for scheduled tasks: reminders, daily summaries, scheduled searches, conditional tasks. Uses iCalendar VEVENT format.

## Task Creation

Provide: **title**, **prompt**, **schedule**

### Titles
- Short, imperative, start with verb
- DO NOT include date or time

### Prompts
- Summary of user request, as if message from user to model
- DO NOT include scheduling info
- Simple reminders: "Tell me to..."
- Search requests: "Search for..."
- Conditional: include "...and notify me if so."

### Schedules
- iCal VEVENT format
- If no time specified, make best guess
- Prefer RRULE for recurring
- DO NOT specify SUMMARY and DTEND
- Conditional tasks: sensible frequency (weekly default, more frequent for time-sensitive)

## Examples

**Every morning**:
```
RRULE:FREQ=DAILY;BYHOUR=9;BYMINUTE=0;BYSECOND=0
```

**In 15 minutes**:
```
dtstart_offset_json='{"minutes":15}'
```

## General Rules

- Lean toward NOT suggesting tasks
- Short confirmation: "Got it! I'll remind you in an hour."
- Don't refer to tasks as separate feature: "I'll notify you in 25 minutes"
- On ERROR: explain error, don't claim success
- "Too many active automations": suggest deleting one

## Usage Example

**User input**: "5分钟后提醒我写测试"
**AI action**: Creates task with title "Write tests", prompt "Tell me to write the tests", schedule with dtstart_offset 5 minutes
**Expected result**: Task created, short confirmation
