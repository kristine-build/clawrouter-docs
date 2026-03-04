# zh\_\_docs\_\_api\_\_ai-model\_\_chat\_\_createmessage\_\_原生claude格式-new-api\_\_32072057

> Migrated from NewAPI docs. Content will be adapted for ClawRouter.

## 原生Claude格式 | New API

AI 模型接口聊天（Chat）

## 原生Claude格式

复制 Markdown打开

Anthropic Claude Messages API 格式的请求。 需要在请求头中包含 `anthropic-version`。

loading...

POST

/`v1`/`messages`

Send

Authorization

Header

Body

### [Authorization](zh__docs__api__ai-model__chat__createmessage__原生claude格式-new-api__32072057.md#authorization)

BearerAuth

AuthorizationBearer

使用 Bearer Token 认证。 格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

### [Header Parameters](zh__docs__api__ai-model__chat__createmessage__原生claude格式-new-api__32072057.md#header-parameters)

anthropic-version\*string

Anthropic API 版本

x-api-key?string

Anthropic API Key (可选，也可使用 Bearer Token)

### [Request Body](zh__docs__api__ai-model__chat__createmessage__原生claude格式-new-api__32072057.md#request-body)

application/json

model\*string

messages\*arraysystem?string|arraymax\_tokens\*integerRange`1 <= value`temperature?numberRange`0 <= value <= 1`top\_p?numbertop\_k?integerstream?booleanstop\_sequences?arraytools?arraytool\_choice?objectthinking?objectmetadata?object[Response Body](zh__docs__api__ai-model__chat__createmessage__原生claude格式-new-api__32072057.md#response-body)200 application/jsoncURLJavaScriptGoPythonJavaC#curl -X POST "https://loading/v1/messages" \  -H "anthropic-version: 2023-06-01" \  -H "Content-Type: application/json" \  -d '{    "model": "claude-3-opus-20240229",    "messages": \[      {        "role": "user",        "content": "string"      }    ],    "max\_tokens": 1  }'200{  "id": "string",  "type": "message",  "role": "assistant",  "content": \[    {      "type": "string",      "text": "string"    }  ],  "model": "string",  "stop\_reason": "end\_turn",  "usage": {    "input\_tokens": 0,    "output\_tokens": 0,    "cache\_creation\_input\_tokens": 0,    "cache\_read\_input\_tokens": 0  \}}这篇文档对您有帮助吗？有帮助没帮助最后更新于
