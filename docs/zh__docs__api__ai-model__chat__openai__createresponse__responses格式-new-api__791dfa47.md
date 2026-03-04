# zh\_\_docs\_\_api\_\_ai-model\_\_chat\_\_openai\_\_createresponse\_\_responses格式-new-api\_\_791dfa47

> Migrated from NewAPI docs. Content will be adapted for ClawRouter.

## Responses格式 | New API

AI 模型接口聊天（Chat）原生OpenAI格式

## Responses格式

复制 Markdown打开

OpenAI Responses API，用于创建模型响应。 支持多轮对话、工具调用、推理等功能。

loading...

POST

/`v1`/`responses`

Send

Authorization

Body

### [Authorization](zh__docs__api__ai-model__chat__openai__createresponse__responses格式-new-api__791dfa47.md#authorization)

BearerAuth

AuthorizationBearer

使用 Bearer Token 认证。 格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

### [Request Body](zh__docs__api__ai-model__chat__openai__createresponse__responses格式-new-api__791dfa47.md#request-body)

application/json

model\*string

input?string|array输入内容，可以是字符串或消息数组instructions?stringmax\_output\_tokens?integertemperature?numbertop\_p?numberstream?booleantools?arraytool\_choice?string|objectreasoning?objectprevious\_response\_id?stringtruncation?stringValue in`"auto" | "disabled"`[Response Body](zh__docs__api__ai-model__chat__openai__createresponse__responses格式-new-api__791dfa47.md#response-body)200 application/jsoncURLJavaScriptGoPythonJavaC#curl -X POST "https://loading/v1/responses" \  -H "Content-Type: application/json" \  -d '{    "model": "string"  }'200{  "id": "string",  "object": "response",  "created\_at": 0,  "status": "completed",  "model": "string",  "output": \[    {      "type": "string",      "id": "string",      "status": "string",      "role": "string",      "content": \[        {          "type": "string",          "text": "string"        }      ]    }  ],  "usage": {    "prompt\_tokens": 0,    "completion\_tokens": 0,    "total\_tokens": 0,    "prompt\_tokens\_details": {      "cached\_tokens": 0,      "text\_tokens": 0,      "audio\_tokens": 0,      "image\_tokens": 0    },    "completion\_tokens\_details": {      "text\_tokens": 0,      "audio\_tokens": 0,      "reasoning\_tokens": 0    }  \}}这篇文档对您有帮助吗？有帮助没帮助最后更新于
