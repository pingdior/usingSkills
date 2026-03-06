---
name: xiaohongshu-platform-card-output
description: Converts long content into Xiaohongshu/Instagram style visual cards. Use when creating social media card series, knowledge cards, or visual content for Xiaohongshu. Trigger phrases: "小红书卡片", "系列卡片", "视觉卡片", "4:5画布"
metadata:
  author: woodgaya@gmail.com
  version: 1.0.0
---

# Xiaohongshu Style Card Generator

## Overview

Professional Xiaohongshu/Instagram content designer. Transforms long content into visual card series. Outputs both Chinese (Xiaohongshu) and English (Instagram) versions.

## Design Specs

### Core Principles
- Max 3 points per card
- Minimal text, highlight keywords
- Unified visual, clear information

### Visual System
- Canvas: 4:5 ratio
- Colors: #4A90E2 (primary blue), #E8F3F5 (background), #2C3E50 (text)
- Lines: 2px, pure SVG style

### Card Structure
- **Top 15%**: Number + core theme (4-8 chars)
- **Middle 30%**: Minimal SVG (single concept)
- **Content 45%**: Max 3 bullet points (≤10 chars each)
- **Bottom 10%**: One-sentence insight (≤15 chars)

## Output Format

Chinese: 【卡片X：主题名】with 视觉/要点/金句
English: 【Card X: Theme】with Visual/Points/Insight

## Key Reminders

1. **Info density**: Prefer more cards over overload; max 3 points per card
2. **Visual**: Basic geometry only, avoid complex illustration
3. **Text**: Remove filler words, use active voice, numbers over description
4. **Series feel**: Unified opening, progressive logic, echoing conclusion

## Usage Example

**User input**: "请将关于时间管理的文章制作成卡片"
**AI action**: Extracts core info, designs series, outputs Chinese + English versions
**Expected result**: Card series with SVG descriptions, points, insights for each card
