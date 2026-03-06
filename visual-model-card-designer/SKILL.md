---
name: visual-model-card-designer
description: Transforms long content into logic-model or minimal-graphic vertical cards. Use when creating visual summaries, social media cards, or diagram-based content. Trigger phrases: "视觉卡片", "逻辑模型", "竖屏卡片", "图解"
metadata:
  author: woodgaya@gmail.com
  version: 3.1
---

# Visual Model Card Designer

## Overview

Transforms long content into "logic model" or "minimal graphic" style vertical cards. Prioritizes diagrams over pure text. All graphics must use native SVG code - no external image links.

## Goals

1. **Core Extraction**: Extract 4-7 key nodes
2. **Visual Translation**:
   - Priority 1: Convert concepts to Venn diagrams, pyramids, funnels, quadrants, cycle arrows
   - Priority 2: Use geometric shapes (circles, lines, rectangles) for metaphors
   - Constraint: Never generate "Error", "404", or external image links
3. **Batch Delivery**: Generate HTML Artifact with "download all" function

## Workflow

1. **Input Parse**: Analyze user-provided URL or topic
2. **Visual Conception**: What chart represents this view? (e.g., system collapse = inverted pyramid)
3. **Code Build**: HTML/CSS cards (320x520px), embed SVG, include downloadAll() JS
4. **Copy Generation**: Output 3 style variations

## Visual Style

- **Colors**: Background #f7f9fa or #fdfbf7; Graphics #2c3e50, #e74c3c, #3498db
- **Lines**: stroke-width 2px, linecap round
- **Fill**: Use opacity 0.1-0.2 for layering
- **Prohibited**: Complex illustration details, keep iconic

## Output Format

Must use Artifact structure with HTML content. Card structure: visual-area (180px) + content-area. Include html2canvas for batch download.

## Usage Example

**User input**: "把这段文章做成视觉卡片"
**AI action**: Extracts key points, designs diagrams, generates HTML with SVG and download function
**Expected result**: HTML Artifact with 320x520px cards, batch download button
