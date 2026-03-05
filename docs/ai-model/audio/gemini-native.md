# 原生Gemini格式

Gemini 音频生成。 使用 Gemini 模型生成内容（含语音相关配置）。

## Endpoint

`POST /v1beta/models/{model}:generateContent`

## Authentication

使用 Bearer Token（`Authorization: Bearer YOUR_API_KEY`）。

## Parameters

| 名称      | 位置     | 类型       | 必填  | 说明                                   |
| ------- | ------ | -------- | --- | ------------------------------------ |
| `model` | `path` | `string` | yes | 模型名称，例如 gemini-2.5-flash-preview-tts |

## Request Body

Content-Type:

* `application/json`

| 字段                                                                        | 类型              | 必填  | 说明        |
| ------------------------------------------------------------------------- | --------------- | --- | --------- |
| `contents[]`                                                              | `array<object>` | yes | 输入内容列表    |
| `contents[].role`                                                         | `string`        | no  | 角色标识      |
| `contents[].parts[]`                                                      | `array<object>` | no  | -         |
| `contents[].parts[].text`                                                 | `string`        | no  | 文本内容      |
| `contents[].parts[].inlineData`                                           | `object`        | no  | -         |
| `contents[].parts[].inlineData.mimeType`                                  | `string`        | no  | -         |
| `contents[].parts[].inlineData.data`                                      | `string`        | no  | Base64 数据 |
| `generationConfig`                                                        | `object`        | no  | -         |
| `generationConfig.responseModalities[]`                                   | `array<string>` | no  | -         |
| `generationConfig.speechConfig`                                           | `object`        | no  | -         |
| `generationConfig.speechConfig.voiceConfig`                               | `object`        | no  | -         |
| `generationConfig.speechConfig.voiceConfig.prebuiltVoiceConfig`           | `object`        | no  | -         |
| `generationConfig.speechConfig.voiceConfig.prebuiltVoiceConfig.voiceName` | `string`        | no  | 语音名称      |

### Minimal Request JSON

```json
{
  "contents": [
    {
      "parts": [
        {
          "text": "请用中文播报今天的天气摘要"
        }
      ]
    }
  ],
  "generationConfig": {
    "responseModalities": [
      "AUDIO"
    ],
    "speechConfig": {
      "voiceConfig": {
        "prebuiltVoiceConfig": {
          "voiceName": "Kore"
        }
      }
    }
  }
}
```

## Responses

### 200

| 字段                                                 | 类型              | 必填 | 说明        |
| -------------------------------------------------- | --------------- | -- | --------- |
| `candidates[]`                                     | `array<object>` | no | -         |
| `candidates[].content`                             | `object`        | no | -         |
| `candidates[].content.role`                        | `string`        | no | 角色标识      |
| `candidates[].content.parts[]`                     | `array<object>` | no | -         |
| `candidates[].content.parts[].text`                | `string`        | no | 文本内容      |
| `candidates[].content.parts[].inlineData`          | `object`        | no | -         |
| `candidates[].content.parts[].inlineData.mimeType` | `string`        | no | -         |
| `candidates[].content.parts[].inlineData.data`     | `string`        | no | Base64 数据 |
| `candidates[].finishReason`                        | `string`        | no | -         |
| `usageMetadata`                                    | `object`        | no | -         |
| `usageMetadata.promptTokenCount`                   | `integer`       | no | -         |
| `usageMetadata.candidatesTokenCount`               | `integer`       | no | -         |
| `usageMetadata.totalTokenCount`                    | `integer`       | no | -         |

### Minimal Response JSON

```json
{
  "candidates": [
    {
      "content": {
        "role": "model",
        "parts": [
          {
            "inlineData": {
              "mimeType": "audio/wav",
              "data": "BASE64_AUDIO_DATA"
            }
          }
        ]
      },
      "finishReason": "STOP"
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 12,
    "candidatesTokenCount": 58,
    "totalTokenCount": 70
  }
}
```

### Error Responses

| 状态码   | 含义     |
| ----- | ------ |
| `400` | 请求参数错误 |
| `401` | 鉴权失败   |
| `429` | 请求过于频繁 |
| `500` | 服务端错误  |

## Examples

```bash
curl -X POST "
https://YOUR_BASE_URL/v1beta/models/gemini-2.5-flash-preview-tts:generateContent" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "contents": [
    {
      "parts": [
        {
          "text": "请用中文播报今天的天气摘要"
        }
      ]
    }
  ],
  "generationConfig": {
    "responseModalities": [
      "AUDIO"
    ],
    "speechConfig": {
      "voiceConfig": {
        "prebuiltVoiceConfig": {
          "voiceName": "Kore"
        }
      }
    }
  }
}
JSON
```

### Error Example

```json
{
  "error": {
    "code": 400,
    "message": "Invalid request"
  }
}
```
