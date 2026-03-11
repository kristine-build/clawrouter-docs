# ChatCompletions格式

AI 模型接口聊天（Chat）原生OpenAI格式

# ChatCompletions格式

根据对话历史创建模型响应。支持流式和非流式响应。

兼容 OpenAI Chat Completions API。



/`v1`/`chat`/`completions`


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

模型 ID

messages\*array<object>

对话消息列表

temperature?number

采样温度

Default`1`

Range`0 <= value <= 2`

top\_p?number

核采样参数

Default`1`

Range`0 <= value <= 1`

n?integer

生成数量

Default`1`

Range`1 <= value`

stream?boolean

是否流式响应

Default`false`

stream\_options?object

stop?string|array<string>

停止序列

max\_tokens?integer

最大生成 Token 数

max\_completion\_tokens?integer

最大补全 Token 数

presence\_penalty?number

Default`0`

Range`-2 <= value <= 2`

frequency\_penalty?number

Default`0`

Range`-2 <= value <= 2`

logit\_bias?object

user?string

tools?array<object>

tool\_choice?string|object

response\_format?object

seed?integer

reasoning\_effort?string

推理强度 (用于支持推理的模型)

Value in`"low" | "medium" | "high"`

modalities?array<string>

audio?object

## [Response Body](#response-body)

### 200 application/json

### 400 application/json

### 429 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://docs.newapi.pro/v1/chat/completions" \  -H "Content-Type: application/json" \  -d '{    "model": "gpt-4",    "messages": [      {        "role": "system",        "content": "string"      }    ]  }'
```

200400429

```
{
  "id": "string",
  "object": "chat.completion",
  "created": 0,
  "model": "string",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "system",
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
