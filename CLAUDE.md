# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a Wiki-style knowledge base for **HiAgent** - an enterprise-level AI agent low-code platform (`https://agent.laiyifen.com`). The knowledge base helps AI agents understand and design solutions for the HiAgent platform.

## Structure

```
hiagent-knowledge-base/
├── manifest.json     # Machine-parseable index with decision tree and quick reference
├── README.md         # Overview
└── wiki/             # Wiki pages
    ├── Home.md       # Entry point ★
    ├── 模型选择.md    # Model selection (reasoning vs non-reasoning models)
    ├── 参数配置.md    # Agent parameters (thinking modes, RAG settings)
    ├── 提示词设计.md  # Prompt design (structure, fields, optimization)
    ├── 插件与MCP.md   # Plugins and MCP protocol
    ├── 工作流.md      # Workflow orchestration (nodes, variables)
    ├── 知识库与RAG.md # Knowledge base and RAG configuration
    ├── 发布与集成.md  # Publishing and integration channels
    ├── 多智能体.md    # Multi-agent orchestration
    └── 能力边界.md    # Platform capabilities (supported/unsupported/uncertain)
```

## Wiki Link Syntax

Pages use `[[页面名]]` format for internal links. Example: `[[模型选择]]` → `wiki/模型选择.md`.

## Credibility Levels

| Source | Credibility | Usage |
|--------|-------------|-------|
| PDF original | 高 (High) | Primary reference |
| Video OCR | 中 (Medium) | Supplementary, needs UI confirmation |

**Rule**: When designing solutions, only use capabilities marked as "明确支持" (explicitly supported) in `能力边界.md`. Do not assume capabilities marked as "未明确支持" exist.

## Design Decision Tree

```
需求分析 (Requirement Analysis)
    │
    ├─ 私有知识？ ──────→ wiki/知识库与RAG.md
    │
    ├─ 实时数据/外部动作？ ─→ wiki/插件与MCP.md
    │
    ├─ 固定流程？ ───────→ wiki/工作流.md
    │
    └─ 任务类型差异大？ ──→ wiki/多智能体.md
```

## Key Platform Concepts

- **Agent**: LLM-based system with tool calling, planning, reflection, and memory
- **Thinking Modes**: ReAct (default), Function_call, Plan and Execute, deep_search
- **Model Selection**: Non-reasoning models for agent base; reasoning models for content/analysis
- **Default Parameters**: max_token=4096, 对话轮数=30, RAG范围=3

## When Updating This Knowledge Base

1. Update the relevant wiki/*.md file
2. Update manifest.json if adding new pages or changing structure
3. Mark credibility level for new information (PDF vs video OCR source)
4. Cross-reference related pages using [[链接]] syntax
