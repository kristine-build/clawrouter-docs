> Migrated from NewAPI docs. Content will be adapted for ClawRouter.

# 原生Gemini格式 | New API

AI 模型接口音频（Audio）

# 原生Gemini格式

复制 Markdown打开

Gemini 音频生成接口。
可使用gemini-2.5-flash-preview-tts等模型

loading...

POST

/`v1beta`/`models`/`{model}:generateContent`

Send

Authorization

Path

Body

## [Authorization](#authorization)

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

## [Path Parameters](#path-parameters)

model\*string

模型名称

## [Request Body](#request-body)

application/json

contents\*array<object>

generationConfig\*object

## [Response Body](#response-body)

### 200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1beta/models/string:generateContent" \  -H "Content-Type: application/json" \  -d '{    "contents": [      {}    ],    "generationConfig": {      "responseModalities": [        "string"      ],      "speechConfig": {        "voiceConfig": {          "prebuiltVoiceConfig": {            "voiceName": "string"          }        }      }    }  }'
```

200

```
{
  "candidates": [
    {
      "content": {
        "role": "string",
        "parts": [
          {}
        ]
      },
      "finishReason": "string",
      "safetyRatings": [
        {}
      ]
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 0,
    "candidatesTokenCount": 0,
    "totalTokenCount": 0
  }
}
```

这篇文档对您有帮助吗？

有帮助没帮助

最后更新于
