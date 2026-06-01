# API参考

HiAgent 平台 API 接口概览和调用说明（来源：官方文档中心，可信度：高）。

## 接口分类

| 分类 | 说明 |
|------|------|
| 智能体接口 | 智能体发布后的对话API |
| 平台类接口 | 管理和运维API |

## 前置操作

### 鉴权方式

| 方式 | 适用 | 说明 |
|------|------|------|
| API Key | 智能体API | 在智能体发布页面获取 |
| AK/SK | 平台接口 | HMAC-SHA256签名认证 |
| Cookie | 平台接口 | Web端用户认证 |

### 通用说明

- 接口基础域名：`https://agent.laiyifen.com`
- 数据格式：JSON
- 字符编码：UTF-8
- 时间格式：ISO 8601

## 智能体API

### 会话管理

| API | 说明 |
|-----|------|
| CreateConversation | 创建会话，返回AppConversationID |
| GetConversationList | 获取对话列表 |
| GetConversationInputs | 获取对话变量输入 |
| UpdateConversation | 更新会话（名称、变量） |
| DeleteConversation | 删除会话 |

### 对话接口

| API | 说明 |
|-----|------|
| ChatQuery | 对话类聊天（流式SSE） |
| **ChatQueryV2** | 对话类聊天V2（**推荐使用**，返回结构更规范） |
| QueryAgain | 重新生成回复（最多10次） |
| QueryAgainV2 | 重新生成回复V2（推荐） |
| StopMessage | 停止响应 |
| Feedback | 回答反馈评价（赞或踩） |

### 消息接口

| API | 说明 |
|-----|------|
| GetConversationMessages | 获取会话历史消息列表 |
| GetMessageInfo | 获取消息详情（内容、Token消耗等） |
| DeleteMessage | 删除消息 |
| SetMessageAnswerUsed | 多组回答时设置默认回答 |
| GetSuggestedQuestions | 获取提问建议 |

### 其他接口

| API | 说明 |
|-----|------|
| GetAppConfigPreview | 获取应用配置 |
| UploadFile | 上传文件到会话 |

### ChatQueryV2 调用示例

**请求**：
```json
POST /api/v1/agent/{app_id}/conversation/{conversation_id}/chat/v2
Content-Type: application/json

{
  "query": "用户问题",
  "stream": true,
  "conversation_id": "会话ID"
}
```

**流式响应**（SSE）：
```
event: message
data: {"answer": "部分回答内容", "conversation_id": "xxx"}

event: message_end
data: {"answer": "完整回答", "usage": {"token_consumed": 1234}}
```

**透传自定义header**（v2.5.0+）：请求header以 `X-Trace-***` 命名会默认透传。

## 文件上传服务

| API | 说明 |
|-----|------|
| UploadRaw | 单文件上传（自动长效存储） |
| LongLive | 长效存储文件 |
| Delete | 删除文件索引 |
| BatchDelete | 批量删除文件索引 |
| DownloadKey | 获取下载秘钥 |
| Download | 文件下载 |

## 平台类接口

### 知识库接口

| 接口组 | 说明 |
|--------|------|
| 知识库管理 | 创建、查询、更新、删除知识库 |
| 目录管理 | 创建、查询、更新、删除目录 |
| 文件管理 | 上传、查询、删除文件 |
| 检索 | 知识库检索（向量/全文/混合） |
| 分段管理 | 查询、更新、删除分段 |

### 平台管理接口

| 接口组 | 说明 |
|--------|------|
| 用户管理 | 创建、查询、更新、删除用户 |
| 角色管理 | 创建、查询、更新、删除角色 |
| 组织管理 | 创建、查询、更新、删除组织 |
| 空间管理 | 创建、查询、更新、删除空间 |
| SSO登录 | SSO认证接口 |
| 公告 | 公告管理 |
| 标签 | 标签管理 |
| 系统管理 | 系统配置 |

### 智能体管理接口

| 接口组 | 说明 |
|--------|------|
| 智能体列表 | 查询智能体列表 |
| 智能体详情 | 查询智能体详情 |
| 干预规则 | 管理干预规则 |
| 发布管理 | 智能体发布和渠道管理 |
| 日志查询 | 智能体运行日志 |

### 资源管理接口

| 接口组 | 说明 |
|--------|------|
| 空间管理 | 空间CRUD |
| 标签管理 | 标签CRUD |
| 插件管理 | 插件CRUD |
| 发布管理 | 发布配置 |

### 模型管理及体验中心接口

| 接口组 | 说明 |
|--------|------|
| 体验中心 | 模型体验 |
| 模型管理 | 模型接入、服务、路由 |

## 调用示例

### Python 调用智能体API

```python
import requests

APP_ID = "your_app_id"
API_KEY = "your_api_key"
BASE_URL = "https://agent.laiyifen.com"

# 1. 创建会话
resp = requests.post(
    f"{BASE_URL}/api/v1/agent/{APP_ID}/conversation",
    headers={"Authorization": f"Bearer {API_KEY}"}
)
conversation_id = resp.json()["conversation_id"]

# 2. 发送对话（流式）
resp = requests.post(
    f"{BASE_URL}/api/v1/agent/{APP_ID}/conversation/{conversation_id}/chat/v2",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={"query": "你好", "stream": True},
    stream=True
)
for line in resp.iter_lines():
    if line:
        print(line.decode())
```

### cURL 调用示例

```bash
# 创建会话
curl -X POST "https://agent.laiyifen.com/api/v1/agent/{APP_ID}/conversation" \
  -H "Authorization: Bearer {API_KEY}"

# 对话
curl -X POST "https://agent.laiyifen.com/api/v1/agent/{APP_ID}/conversation/{CONV_ID}/chat/v2" \
  -H "Authorization: Bearer {API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"query": "你好", "stream": true}'
```

## 注意事项

1. 智能体API需先发布智能体获取APP_ID和API_KEY
2. 流式接口使用SSE协议
3. 对话轮数受智能体参数配置限制
4. UserID参数支持中文（v2.3.0+）
5. 完整API参数说明见官方文档中心的API模块

## 相关链接

- [[发布与集成]] - 获取API Key
- [[参数配置]] - 对话轮数和Token限制
- [[开发指南]] - SDK集成
- [[版本更新记录]] - API版本变更
