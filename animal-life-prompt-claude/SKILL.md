---
name: animal-life-prompt-claude
description: Generates animal lifecycle SVG charts and descriptions using Lisp-style pseudocode. Use when creating educational content about animal life cycles, SVG visualizations, or science communication. Trigger phrases: "动物的一生", "生命周期", "SVG图表", "蝉/鲸鱼/长颈鹿"
metadata:
  author: woodgaya@gmail.com
  version: 1.0.0
---

# Animal Life Cycle Prompt for Claude

## Overview

Generates animal lifecycle SVG charts and descriptions. Uses Lisp-style function structure to define stages,科普数据, background, timeline, emoji for different animals (蝉, 鲸鱼, 长颈鹿, etc.).

## Supported Animals

- **蝉**: 卵→若虫期(地下)→成虫期; timeline 0-17年
- **鲸鱼**: 胎儿期→幼年→青年→成年→老年; timeline 0-100年
- **长颈鹿**: 新生期→幼年→青年→成年→老年; timeline 0月-25年
- **Default**: 初期→成长期→成熟期→衰老期

## Output Components

- Life stage labels with emoji
- Timeline axis
- 科普数据 points
- Background (gradient by theme: 蝉=sky/land, 鲸鱼=ocean, 长颈鹿=grassland)
- Subtitle: "你知道吗？[interesting fact]"

## Workflow

1. Run (start) - prompt for animal theme input
2. Get life stages, 科普数据, background design, timeline for theme
3. Select stage emoji and decoration emoji
4. Fill SVG template, output optimized chart + text description

## Usage Example

**User input**: "蝉的一生" or "鲸鱼的一生"
**AI action**: Generates lifecycle SVG with stages, timeline, 科普数据, theme-appropriate styling
**Expected result**: Complete SVG chart + scientific description with interesting facts
