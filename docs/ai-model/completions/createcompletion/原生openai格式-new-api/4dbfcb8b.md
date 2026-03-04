# 原生OpenAI格式 | New API

AI 模型接口补全（Completions）

# 原生OpenAI格式

基于给定提示创建文本补全

loading...

POST

/`v1`/`completions`

Send

Authorization

Body

## [Authorization](#authorization)

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

## [Request Body](#request-body)

application/json

model\*string

prompt\*string|array<string>

max\_tokens?integer

temperature?number

top\_p?number

n?integer

stream?boolean

stop?string|array<string>

suffix?string

echo?boolean

## [Response Body](#response-body)

### 200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/completions" \  -H "Content-Type: application/json" \  -d '{    "model": "string",    "prompt": "string"  }'
```

200

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
