# 原生Claude格式

AI 模型接口聊天（Chat）

# 原生Claude格式

Anthropic Claude Messages API 格式的请求。
需要在请求头中包含 `anthropic-version`。

loading...


/`v1`/`messages`

Send

Authorization

Header

Body

## [Authorization](#authorization)

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

## [Header Parameters](#header-parameters)

anthropic-version\*string

Anthropic API 版本

x-api-key?string

Anthropic API Key (可选，也可使用 Bearer Token)

## [Request Body](#request-body)

application/json

model\*string

messages\*array<object>

system?string|array<object>

max\_tokens\*integer

Range`1 <= value`

temperature?number

Range`0 <= value <= 1`

top\_p?number

top\_k?integer

stream?boolean

stop\_sequences?array<string>

tools?array<object>

tool\_choice?object

thinking?object

metadata?object

## [Response Body](#response-body)

### 200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/messages" \  -H "anthropic-version: 2023-06-01" \  -H "Content-Type: application/json" \  -d '{    "model": "claude-3-opus-20240229",    "messages": [      {        "role": "user",        "content": "string"      }    ],    "max_tokens": 1  }'
```

200

```
{
  "id": "string",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "string",
      "text": "string"
    }
  ],
  "model": "string",
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 0,
    "output_tokens": 0,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0
  }
}
```
