---
name: text-to-image-prompt-gen3-runway
description: Guides Gen-3 Alpha Runway video generation prompts. Use when creating video prompts for Runway, text-to-video, or Gen-3 Alpha. Trigger phrases: "Gen-3 Alpha", "Runway", "文生图", "视频提示词"
metadata:
  author: woodgaya@gmail.com
  version: 1.0.0
---

# Gen-3 Alpha Prompt Guide - Runway

## Overview

Gen-3 Alpha can turn artistic visions into video. Creating powerful prompts that convey scenes is key to generating video that matches your concept.

## Prompt Basics

### Direct, Not Conceptual
Describe as if to a new collaborator who will shoot the scene. Avoid conceptual language when simple description works.

❌ 一名男子侵入了主机 → ✅ 一名男子在键盘上用力打字

### Descriptive, Not Conversational
Runway models focus on visual details. Dialogue adds no value.

❌ 你能给我制作一段关于两个朋友吃生日蛋糕的视频吗？ → ✅ 两个朋友吃生日蛋糕

### Positive Wording
No negative prompts. Model doesn't support "what should NOT happen."

❌ 相机不动。没有动作。 → ✅ 静态相机。相机保持静止。

## Structure

[Camera movement]: [Establish scene]. [Additional details].

Example: "Low angle static shot: The camera is angled up at a woman wearing all orange as she stands in a tropical rainforest with colorful flora. The dramatic sky is overcast and gray."

## Image + Text

When using input images: use simple, direct text describing **movement** only. Do NOT describe image contents.

Example: "Subject cheerfully poses, her hands forming a peace sign."

## Keywords

- **Camera**: Low angle, High angle, Overhead, FPV, Hand held, Wide angle, Close up, Macro, Tracking, 50mm lens, SnorriCam
- **Lighting**: Diffused, Silhouette, Lens flare, Back lit, Side lit, [color] gel lighting
- **Movement**: 成长, 出现, 爆炸, 上升, 波动, 扭曲, 变换, 涟漪, 破碎, 展开, 涡流
- **Style**: 穆迪, 电影, 彩虹色, 家庭录像VHS, 故障核
- **Text**: 大胆的, 涂鸦, 氖, 校队, 刺绣

## Bracket Placeholders

Use brackets for reusable presets: 摄像机无缝飞过[拍摄对象位置]

## Usage Example

**User input**: "生成一个冰川峡谷到云海的转场视频"
**AI action**: Applies structure, uses positive wording, outputs prompt with camera + scene + details
**Expected result**: Runway-ready prompt for Gen-3 Alpha
