# 实时语音（Realtime）

AI 模型接口实时语音（Realtime）

# 原生OpenAI格式

建立 WebSocket 连接用于实时对话。

**注意**: 这是一个 WebSocket 端点，需要使用 WebSocket 协议连接。

连接 URL 示例: `wss://api.example.com/v1/realtime?model=gpt-4o-realtime`

loading...


/`v1`/`realtime`

Send

Authorization

Query

## [Authorization](#authorization)

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

## [Query Parameters](#query-parameters)

model?string

要使用的模型

## [Response Body](#response-body)

### 101

### 400 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/v1/realtime"
```

101400

Empty

```
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```
