# zh\_\_docs\_\_api\_\_ai-model\_\_audio\_\_geminirelayv1beta-383836364\_\_原生gemini格式-new-api\_\_04afcc5e

> Migrated from NewAPI docs. Content will be adapted for ClawRouter.

## 原生Gemini格式 | New API

AI 模型接口音频（Audio）

## 原生Gemini格式

复制 Markdown打开

Gemini 音频生成接口。 可使用gemini-2.5-flash-preview-tts等模型

loading...

POST

/`v1beta`/`models`/`{model}:generateContent`

Send

Authorization

Path

Body

### [Authorization](zh__docs__api__ai-model__audio__geminirelayv1beta-383836364__原生gemini格式-new-api__04afcc5e.md#authorization)

BearerAuth

AuthorizationBearer

使用 Bearer Token 认证。 格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

### [Path Parameters](zh__docs__api__ai-model__audio__geminirelayv1beta-383836364__原生gemini格式-new-api__04afcc5e.md#path-parameters)

model\*string

模型名称

### [Request Body](zh__docs__api__ai-model__audio__geminirelayv1beta-383836364__原生gemini格式-new-api__04afcc5e.md#request-body)

application/json

contents\*arraygenerationConfig\*object[Response Body](zh__docs__api__ai-model__audio__geminirelayv1beta-383836364__原生gemini格式-new-api__04afcc5e.md#response-body)200 application/jsoncURLJavaScriptGoPythonJavaC#curl -X POST "https://loading/v1beta/models/string:generateContent" \  -H "Content-Type: application/json" \  -d '{    "contents": \[      {}    ],    "generationConfig": {      "responseModalities": \[        "string"      ],      "speechConfig": {        "voiceConfig": {          "prebuiltVoiceConfig": {            "voiceName": "string"          }        }      }    }  }'200{  "candidates": \[    {      "content": {        "role": "string",        "parts": \[          {}        ]      },      "finishReason": "string",      "safetyRatings": \[        {}      ]    }  ],  "usageMetadata": {    "promptTokenCount": 0,    "candidatesTokenCount": 0,    "totalTokenCount": 0  \}}这篇文档对您有帮助吗？有帮助没帮助最后更新于
