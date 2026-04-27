---
name: summary-for-week
description: Organizes weekly notes into a structured weekly summary with key insights, tasks, risks, and next-step recommendations. Use when the user wants to generate, refine, or standardize a weekly report from existing materials. Trigger phrases: "整理周报", "生成本周总结", "weekly summary", "本周复盘"
metadata:
  author: woodgaya@gmail.com
  version: 1.0.0
---

# Weekly Summary Organizer

## Overview

This skill converts weekly working materials into a clear, decision-oriented weekly report. It focuses on extracting core viewpoints, models, SOPs, progress status, risks, and next actions, then producing both topic-based sections and an overall weekly summary file.

## When To Use

Use this skill when the user:

- Wants to turn scattered weekly notes into a structured summary
- Needs a management-style weekly report with progress, risks, and actions
- Wants to identify disputed viewpoints, gaps, or weak reasoning in the week's work
- Needs a final `weekly-*.md` summary file in the same directory as the source weekly report

Do not use this skill for:

- Daily reports
- Meeting minutes that are not weekly review materials
- Long-term quarterly planning without week-based source inputs

## Operating Instructions

1. Collect the user's weekly materials, including notes, drafts, task lists, decisions, and supporting documents.
2. Extract the week's core viewpoints, models, methods, and SOPs that appeared in the input.
3. Identify disagreements, questionable assumptions, weak logic, or places where the current SOP may need revision.
4. Separate work into three groups: completed, in progress, and not completed. For each group, evaluate status, impact, and next-step recommendations.
5. Summarize the most important progress of the week using the following required blocks:
   - Key goals and risk list
   - Technical and product highlights
   - Problem list and action suggestions
   - Weekly summary method improvement suggestions
6. Produce the "Insights & Decisions" section and answer these questions explicitly:
   - What was the biggest cognitive change this week?
   - What key decision must be made next week based on that change?
   - Did the user uphold their principles, such as ROI discipline and focus?
7. Organize the content by theme. Create clear section titles automatically and group related content into the same topic area.
8. Generate a final Markdown summary file with a `weekly-` prefix in the same directory as the weekly report source file.

## Output Requirements

The output should:

- Be written in clear Markdown
- Be grouped by topic rather than by raw chronology
- Highlight decisions, tradeoffs, and unresolved risks
- Distinguish facts, interpretations, and recommendations where possible
- End with concrete next actions for the coming week

Recommended output structure:

1. Core viewpoints, models, and SOPs
2. Disputed points or questionable assumptions
3. Task status review
4. Most important weekly progress
5. Insights and decisions
6. Next-week action recommendations

## Usage Example

**User input**: "请基于我这周的工作记录整理周报，并输出总总结文件。"

**AI action**:

- Reads the weekly materials
- Extracts key viewpoints, methods, progress, and risks
- Groups the content by theme
- Produces a final `weekly-*.md` summary in the same directory

**Expected result**: A structured weekly report with progress analysis, insight extraction, decision prompts, and next-step recommendations.

## Error Handling

- If the source material is incomplete, clearly state which inputs are missing and continue with a best-effort summary.
- If task status is ambiguous, mark it as uncertain instead of guessing.
- If no meaningful insight or decision can be inferred, explicitly say so and suggest what information should be added next time.
- If multiple themes overlap, merge them only when doing so improves clarity.

## Performance Notes

- Prefer concise synthesis over repeating raw notes.
- Preserve signal: prioritize decisions, risks, changes in understanding, and execution quality.
- Avoid inventing achievements, conclusions, or action items that are not supported by the input.
