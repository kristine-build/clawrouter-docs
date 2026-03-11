# ChatCompletions格式

根据对话历史创建模型响应。支持流式和非流式响应。  
兼容 OpenAI Chat Completions API。

## Endpoint

`POST /v1/chat/completions`

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | \| --- \| --- \| --- \| --- \| \| `Authorization` \| `string` \| yes \| Bearer API Key，示例：`Authorization: Bearer YOUR_API_KEY` \| |
## Request Body
Content-Type: `application/json`
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `model` | `string` | yes | 模型 ID |
| `messages` | `array` | yes | 对话消息列表 |
| `messages[].role` | `string` | yes | 消息角色，示例：`system` / `user` / `assistant` |
| `messages[].content` | `string` | yes | 消息内容 |
| `messages[].name` | `string` | no | （可选）名称 |
| `messages[].tool_calls` | `array` | no | 工具调用列表 |
| `temperature` | `number` | no | 采样温度（默认 `1`，范围 `0 <= value <= 2`） |
| `top_p` | `number` | no | 核采样参数（默认 `1`，范围 `0 <= value <= 1`） |
| `n` | `integer` | no | 生成数量（默认 `1`，范围 `value >= 1`） |
| `stream` | `boolean` | no | 是否流式响应（默认 `false`） |
| `stream_options` | `object` | no | 流式选项 |
| `stop` | `string / array<string>` | no | 停止序列 |
| `max_tokens` | `integer` | no | 最大生成 Token 数 |
| `max_completion_tokens` | `integer` | no | 最大补全 Token 数 |
| `presence_penalty` | `number` | no | 存在惩罚（默认 `0`，范围 `-2 <= value <= 2`） |
| `frequency_penalty` | `number` | no | 频率惩罚（默认 `0`，范围 `-2 <= value <= 2`） |
| `logit_bias` | `object` | no | token 偏置映射 |
| `user` | `string` | no | 用户标识 |
| `tools` | `array` | no | 工具定义列表 |
| `tool_choice` | `string / object` | no | 工具选择策略 |
| `response_format` | `object` | no | 响应格式参数 |
| `response_format.type` | `string` | no | 响应格式类型 |
| `seed` | `integer` | no | 随机种子 |
| `reasoning_effort` | `string` | no | 推理强度，枚举：`low` / `medium` / `high` |
| `modalities` | `array<string>` | no | 模态列表 |
| `audio` | `object` | no | 音频参数 |

## Response Body

### 200 application/json

```json
{
  "id": "string",
  "object": "chat.completion",
  "created": 0,
  "model": "string",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "string",
        "name": "string",
        "tool_calls": [
          {
            "id": "string",
            "type": "function",
            "function": {
              "name": "string",
              "arguments": "string"
            }
          }
        ],
        "tool_call_id": "string",
        "reasoning_content": "string"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 0,
    "completion_tokens": 0,
    "total_tokens": 0,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "text_tokens": 0,
      "audio_tokens": 0,
      "image_tokens": 0
    },
    "completion_tokens_details": {
      "text_tokens": 0,
      "audio_tokens": 0,
      "reasoning_tokens": 0
    }
  },
  "system_fingerprint": "string"
}
```
## Error Example

### 400 application/json

```json
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```

### 401 application/json

```json
{
  "error": {
    "message": "Unauthorized",
    "type": "auth_error",
    "code": "invalid_api_key"
  }
}
```

### 429 application/json

```json
{
  "error": {
    "message": "Too many requests",
    "type": "rate_limit_error",
    "code": "rate_limit"
  }
}
```

## Code Examples

### cURL

```bash
curl -X POST "https://docs.newapi.pro/v1/chat/completions" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [
      {
        "role": "user",
        "content": "Hello"
      }
    ]
  }'
```

### JavaScript

```javascript
const response = await fetch("https://docs.newapi.pro/v1/chat/completions", {
  method: "POST",
  headers: {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "gpt-4o-mini",
    messages: [
      {
        role: "user",
        content: "Hello"
      }
    ]
  })
});
console.log(await response.status);
console.log(await response.text());
```

### Go

```go
func main() {
	body := bytes.NewBuffer([]byte(`{
    "model":"gpt-4o-mini",
    "messages":[{"role":"user","content":"Hello"}]
  }`))
	req, _ := http.NewRequest("POST", "https://docs.newapi.pro/v1/chat/completions", body)
	req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
	req.Header.Set("Content-Type", "application/json")
	http.DefaultClient.Do(req)
}
```

### Python

```python
url = "https://docs.newapi.pro/v1/chat/completions"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json",
}
payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "user",
            "content": "Hello"
        }
    ]
}
response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Java

```java
String json = """
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": "Hello"
    }
  ]
}
""";
var request = HttpRequest.newBuilder()
    .uri(URI.create("https://docs.newapi.pro/v1/chat/completions"))
    .header("Authorization", "Bearer YOUR_API_KEY")
    .header("Content-Type", "application/json")
    .POST(HttpRequest.BodyPublishers.ofString(json))
    .build();
```

### C#

```csharp
var request = new HttpRequestMessage(HttpMethod.Post, "https://docs.newapi.pro/v1/chat/completions");
request.Headers.Add("Authorization", "Bearer YOUR_API_KEY");
request.Content = new StringContent("""
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": "Hello"
    }
  ]
}
""", Encoding.UTF8, "application/json");
await client.SendAsync(request);
```
