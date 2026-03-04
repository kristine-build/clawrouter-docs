# zh\_\_docs\_\_api\_\_ai-model\_\_chat\_\_openai\_\_createchatcompletion\_\_chatcompletions格式-new-api\_\_1f721286

> Migrated from NewAPI docs. Content will be adapted for ClawRouter.

## ChatCompletions格式 | New API

AI 模型接口聊天（Chat）原生OpenAI格式

## ChatCompletions格式

复制 Markdown打开

根据对话历史创建模型响应。支持流式和非流式响应。

兼容 OpenAI Chat Completions API。

loading...

POST

/`v1`/`chat`/`completions`

Send

Authorization

Body

### [Authorization](zh__docs__api__ai-model__chat__openai__createchatcompletion__chatcompletions格式-new-api__1f721286.md#authorization)

BearerAuth

AuthorizationBearer

使用 Bearer Token 认证。 格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

### [Request Body](zh__docs__api__ai-model__chat__openai__createchatcompletion__chatcompletions格式-new-api__1f721286.md#request-body)

application/json

model\*string

模型 ID

messages\*array对话消息列表temperature?number采样温度Default`1`Range`0 <= value <= 2`top\_p?number核采样参数Default`1`Range`0 <= value <= 1`n?integer生成数量Default`1`Range`1 <= value`stream?boolean是否流式响应Default`false`stream\_options?objectstop?string|array停止序列max\_tokens?integer最大生成 Token 数max\_completion\_tokens?integer最大补全 Token 数presence\_penalty?numberDefault`0`Range`-2 <= value <= 2`frequency\_penalty?numberDefault`0`Range`-2 <= value <= 2`logit\_bias?objectuser?stringtools?arraytool\_choice?string|objectresponse\_format?objectseed?integerreasoning\_effort?string推理强度 (用于支持推理的模型)Value in`"low" | "medium" | "high"`modalities?arrayaudio?object[Response Body](zh__docs__api__ai-model__chat__openai__createchatcompletion__chatcompletions格式-new-api__1f721286.md#response-body)200 application/json400 application/json429 application/jsoncURLJavaScriptGoPythonJavaC#curl -X POST "https://loading/v1/chat/completions" \  -H "Content-Type: application/json" \  -d '{    "model": "gpt-4",    "messages": \[      {        "role": "system",        "content": "string"      }    ]  }'200400429{  "id": "string",  "object": "chat.completion",  "created": 0,  "model": "string",  "choices": \[    {      "index": 0,      "message": {        "role": "system",        "content": "string",        "name": "string",        "tool\_calls": \[          {            "id": "string",            "type": "function",            "function": {              "name": "string",              "arguments": "string"            }          }        ],        "tool\_call\_id": "string",        "reasoning\_content": "string"      },      "finish\_reason": "stop"    }  ],  "usage": {    "prompt\_tokens": 0,    "completion\_tokens": 0,    "total\_tokens": 0,    "prompt\_tokens\_details": {      "cached\_tokens": 0,      "text\_tokens": 0,      "audio\_tokens": 0,      "image\_tokens": 0    },    "completion\_tokens\_details": {      "text\_tokens": 0,      "audio\_tokens": 0,      "reasoning\_tokens": 0    }  },  "system\_fingerprint": "string"}{  "error": {    "message": "string",    "type": "string",    "param": "string",    "code": "string"  \}}{  "error": {    "message": "string",    "type": "string",    "param": "string",    "code": "string"  \}}这篇文档对您有帮助吗？有帮助没帮助最后更新于
