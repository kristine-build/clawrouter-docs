# 原生Gemini格式

Gemini 音频生成。

使用 Gemini 模型生成内容（含语音相关配置）。

## Endpoint

`POST /v1beta/models/{model}:generateContent`

## Authorization

使用 BearerAuth。
示例请求头：`Authorization: Bearer YOUR_API_KEY`

## Request Body

Content-Type: `application/json`

| name | type | required | description | enum | default | range |
|---|---|---|---|---|---|---|
| `contents[]` | `array<object>` | yes | 输入内容列表 | - | - | - |
| `contents[].role` | `string` | no | 角色标识 | - | - | - |
| `contents[].parts[]` | `array<object>` | no | - | - | - | - |
| `contents[].parts[].text` | `string` | no | 文本内容 | - | - | - |
| `contents[].parts[].inlineData` | `object` | no | - | - | - | - |
| `contents[].parts[].inlineData.mimeType` | `string` | no | - | - | - | - |
| `contents[].parts[].inlineData.data` | `string` | no | Base64 数据 | - | - | - |
| `generationConfig` | `object` | no | - | - | - | - |
| `generationConfig.responseModalities[]` | `array<string>` | no | - | - | - | - |
| `generationConfig.speechConfig` | `object` | no | - | - | - | - |
| `generationConfig.speechConfig.voiceConfig` | `object` | no | - | - | - | - |
| `generationConfig.speechConfig.voiceConfig.prebuiltVoiceConfig` | `object` | no | - | - | - | - |
| `generationConfig.speechConfig.voiceConfig.prebuiltVoiceConfig.voiceName` | `string` | no | 语音名称 | - | - | - |

## Response Body

### 200

| name | type | required | description | enum | default | range |
|---|---|---|---|---|---|---|
| `candidates[]` | `array<object>` | no | - | - | - | - |
| `candidates[].content` | `object` | no | - | - | - | - |
| `candidates[].content.role` | `string` | no | 角色标识 | - | - | - |
| `candidates[].content.parts[]` | `array<object>` | no | - | - | - | - |
| `candidates[].content.parts[].text` | `string` | no | 文本内容 | - | - | - |
| `candidates[].content.parts[].inlineData` | `object` | no | - | - | - | - |
| `candidates[].content.parts[].inlineData.mimeType` | `string` | no | - | - | - | - |
| `candidates[].content.parts[].inlineData.data` | `string` | no | Base64 数据 | - | - | - |
| `candidates[].finishReason` | `string` | no | - | - | - | - |
| `usageMetadata` | `object` | no | - | - | - | - |
| `usageMetadata.promptTokenCount` | `integer` | no | - | - | - | - |
| `usageMetadata.candidatesTokenCount` | `integer` | no | - | - | - | - |
| `usageMetadata.totalTokenCount` | `integer` | no | - | - | - | - |

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

### 4xx/5xx

| status | meaning |
|---|---|
| `400` | 请求参数错误 |
| `401` | 鉴权失败 |
| `429` | 请求过于频繁 |
| `500` | 服务端错误 |

## Code Examples

### cURL

```bash
curl -X POST "https://docs.newapi.pro/v1beta/models/gemini-2.5-flash-preview-tts:generateContent" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents": [{"parts": [{"text": "请用中文播报今天的天气摘要"}]}], "generationConfig": {"responseModalities": ["AUDIO"], "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": "Kore"}}}}}'
```

### Python requests

```python
url = "https://docs.newapi.pro/v1beta/models/gemini-2.5-flash-preview-tts:generateContent"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}
payload = {
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
resp = requests.request("POST", url, headers=headers, json=payload, timeout=30)
print(resp.status_code)
print(resp.text)
```
