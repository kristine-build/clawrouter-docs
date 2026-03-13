# 原生OpenAI格式 | ClawRouter

AI 模型介面补全（Completions）

# 原生OpenAI格式

基于给定提示建立文本补全



## Endpoint

/v1/completions
Authorization

Body

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | AuthorizationBearer <token> 使用 Bearer Token 认证。 格式: `Authorization: Bearer sk-xxxxxx` In: `header` |
## Request Body
application/json

| Name | Type | Required | Description |
|---|---|---|---|
| model | string | yes |  |
| prompt | string\|array<string> | yes |  |
| max_tokens | integer | no |  |
| temperature | number | no |  |
| top_p | number | no |  |
| n | integer | no |  |
| stream | boolean | no |  |
| stop | string\|array<string> | no |  |
| suffix | string | no |  |
| echo | boolean | no |  |
## Response Body

### 200 application/json

### cURL
### JavaScript
### Go
### Python
### Java
### C#

```
curl -X POST "https://docs.newapi.pro/v1/completions" \  -H "Content-Type: application/json" \  -d '{    "model": "string",    "prompt": "string"  }'
```

```
{
  "id": "string",
  "object": "text_completion",
  "created": 0,
  "model": "string",
  "choices": [
    {
      "text": "string",
      "index": 0,
      "finish_reason": "string"
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
  }
}
```
