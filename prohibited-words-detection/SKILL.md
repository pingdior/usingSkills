---
name: prohibited-words-detection
description: Performs three-level risk scanning for platform compliance (absolute claims, false advertising, sensitive content). Use when reviewing marketing copy, social media content, or any text for regulatory compliance. Trigger phrases: "违禁词检测", "合规审查", "风险扫描", "广告法"
metadata:
  author: woodgaya@gmail.com
  version: 1.0.0
---

# Prohibited Words Detection

## Overview

Act as a senior platform compliance reviewer. Scan given text with three-level risk detection and output results in the specified format.

## Detection Mechanisms

### 1. Absolute Claim Detection
- **Prohibited**: 最/第一/国家级/全网首发
- **Alternative**: 建议使用「个人觉得」「实测感受」

### 2. False Advertising Detection
- **Medical claims**: 根治/疗效/修复细胞
- **Effect guarantees**: 7天白2度/月瘦20斤
- **Missing credentials**: 医院同款/医生推荐

### 3. Sensitive Content Detection
- **Values**: body shame/崇洋媚外
- **High-risk domains**: 金融/医疗/封建迷信
- **Drainage info**: 微信号/二维码/外链

## Output Template

- Highlight violations with 🚨
- Violation type with policy reference
- Replacement suggestions (compliant alternatives)
- Risk level: Red/Yellow/Green

## Example

**Input**: "这款面膜全网销量第一！医院皮肤科都在用，7天淡化所有皱纹，添加的xxx成分能修复受损细胞，私信我送独家护肤秘籍"

**Output format**:
```
🚨【违规词1】"全网销量第一"
- 类型：绝对化用语（违反《广告法》第9条）
- 建议改为："累计热销超10万盒"

🚨【违规词2】"医院皮肤科都在用"
- 类型：医疗关联暗示
- 建议改为："实验室实测数据表明"

📊 综合风险等级：🔴 红色（需修改N处）
```

## Usage Example

**User input**: "帮我检测这段文案是否合规"
**AI action**: Scans text, identifies violations, provides replacement suggestions
**Expected result**: Structured compliance report with risk level
