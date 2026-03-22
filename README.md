# HiAgent 知识库

> Wiki 风格的智能体平台知识库，便于 AI 智能体理解和设计。

## 结构

```
hiagent-knowledge-base/
├── manifest.json          # 结构化索引
├── README.md              # 本文件
└── wiki/                  # Wiki 页面
    ├── Home.md            # 首页 ★
    ├── 模型选择.md
    ├── 参数配置.md
    ├── 提示词设计.md
    ├── 插件与MCP.md
    ├── 工作流.md
    ├── 知识库与RAG.md
    ├── 发布与集成.md
    ├── 多智能体.md
    └── 能力边界.md
```

## 快速开始

1. **入口**：`wiki/Home.md`
2. **索引**：`manifest.json`（程序可解析）
3. **决策树**：见 Home.md 或 manifest.json

## 设计决策

```
需求分析
    │
    ├─ 私有知识？ ──────→ wiki/知识库与RAG.md
    │
    ├─ 实时数据/外部动作？ ─→ wiki/插件与MCP.md
    │
    ├─ 固定流程？ ───────→ wiki/工作流.md
    │
    └─ 任务类型差异大？ ──→ wiki/多智能体.md
```

## Wiki 链接语法

页面间使用 `[[页面名]]` 格式链接，如 `[[模型选择]]` 指向 `wiki/模型选择.md`。

## 版本

- 知识库版本：3.0
- 结构：Wiki 风格
- 来源：培训 PDF + 视频 OCR
