# 原生Gemini格式 | ClawRouter

AI 模型介面音訊（Audio）

# 原生Gemini格式

Gemini 音訊生成介面。
可使用gemini-2.5-flash-preview-tts等模型



## Endpoint

/v1beta/models/{model}:generateContent
Authorization

Path

Body

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | AuthorizationBearer <token> 使用 Bearer Token 驗證。 格式: `Authorization: Bearer sk-xxxxxx`.. In: `header`.. |
## [Path Parameters](#path-parameters)

model\*string

模型名称

## Request Body
application/json

| Name | Type | Required | Description |
|---|---|---|---|
| contents | array<object> | yes |  |
| generationConfig | object | yes |  |
## Response Body

### 200 application/json

### cURL
### JavaScript
### Go
### Python
### Java
### C#

```
curl -X POST "https://clawrouter.com/v1beta/models/string:generateContent" \  -H "Content-Type: application/json" \  -d '{    "contents": [      {}    ],    "generationConfig": {      "responseModalities": [        "string"      ],      "speechConfig": {        "voiceConfig": {          "prebuiltVoiceConfig": {            "voiceName": "string"          }        }      }    }  }'
```..

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
```..
