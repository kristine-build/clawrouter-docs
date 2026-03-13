# 原生OpenAI格式

AI 模型介面即時语音（Realtime）

# 原生OpenAI格式

建立 WebSocket 連線用于即時對話。

**注意**: 这是一个 WebSocket 端点，需要使用 WebSocket 协议連線。

連線 URL 範例: `wss://api.example.com/v1/realtime?model=gpt-4o-realtime`..



## Endpoint
&Authorization

Query

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | AuthorizationBearer <token> 使用 Bearer Token 认证。 格式: `Authorization: Bearer sk-xxxxxx`.. In: `header`.. |## [Query Parameters](#query-parameters)

model?string

要使用的模型

## Response Body
### 101

### 400 application/json

### cURL
### JavaScript
### Go
### Python
### Java
### C#

```
curl -X GET "https://docs.newapi.pro/v1/realtime"
```..

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
```..