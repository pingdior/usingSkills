---
name: lisp-core-syntax
description: Lisp/Scheme core syntax for prompt DSL and meta-programming. Use when writing Lisp-style prompts, defining DSLs, or understanding prompt structure. Trigger phrases: "Lisp语法", "Scheme", "括号语法", "元编程"
metadata:
  author: woodgaya@gmail.com
  version: 1.0.0
---

# Lisp Core Syntax

## Overview

Lisp (Scheme dialect) syntax for defining prompt structures and DSLs. Uses parentheses, prefix notation, symbols, lists.

## Core Syntax

### 1. Parentheses
- `(function arg1 arg2)` - first element is function/operator, rest are arguments

### 2. Prefix Notation
- `(+ 1 2)` not `1 + 2`

### 3. Symbols
- Variables, function names: `define`, `let`, `invoke`

### 4. Lists
- Core data structure, code and data: `(1 2 3)`

### 5. Quote
- `'` prevents evaluation: `'(1 2 3)` is data not code

### 6. let
- Local variables: `(let ((x 1) (y 2)) (+ x y))`

### 7. define
- Define variable or function: `(define (add x y) (+ x y))`

### 8. Conditionals
- `if`, `cond`: `(if (> x 0) 'positive 'negative)`

### 9. Lambda
- Anonymous functions: `(lambda (x) (+ x 1))`

## Key Features

- **Homoiconicity**: Code and data same structure, enables meta-programming
- **Dynamic typing**
- **Macros**: Extend language, create new syntax
- **Comments**: `;;` for single line

## Usage in Prompts

Lisp syntax used for structured prompt definitions: `(define story-prompt '(...))`, `(let ((context "...")) ...)`, keyword args `:mood "..."`, nested lists for sequences.

## Usage Example

**User input**: "这段Lisp风格的提示词是什么意思？"
**AI action**: Parses parentheses, explains define/let/lambda, translates to plain language
**Expected result**: Clear explanation of Lisp-style prompt structure
