# 原生Gemini格式

Gemini 音訊生成。

使用 Gemini 模型生成內容（含語音相關設定）。

## Endpoint

`POST /v1beta/models/{model}:generateContent`..

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | 範例請求头：`Authorization: Bearer YOUR_API_KEY`.. |
## Request Body
Content-Type: `application/json`..
| name | type | required | description | enum | default | range |
|---|---|---|---|---|---|---|
| `contents[]`.. | `array<object>`.. | yes | 输入內容清單 | - | - | - |
| `contents[].role`.. | `string`.. | no | 角色标识 | - | - | - |
| `contents[].parts[]`.. | `array<object>`.. | no | - | - | - | - |
| `contents[].parts[].text`.. | `string`.. | no | 文本內容 | - | - | - |
| `contents[].parts[].inlineData`.. | `object`.. | no | - | - | - | - |
| `contents[].parts[].inlineData.mimeType`.. | `string`.. | no | - | - | - | - |
| `contents[].parts[].inlineData.data`.. | `string`.. | no | Base64 資料 | - | - | - |
| `generationConfig`.. | `object`.. | no | - | - | - | - |
| `generationConfig.responseModalities[]`.. | `array<string>`.. | no | - | - | - | - |
| `generationConfig.speechConfig`.. | `object`.. | no | - | - | - | - |
| `generationConfig.speechConfig.voiceConfig`.. | `object`.. | no | - | - | - | - |
| `generationConfig.speechConfig.voiceConfig.prebuiltVoiceConfig`.. | `object`.. | no | - | - | - | - |
| `generationConfig.speechConfig.voiceConfig.prebuiltVoiceConfig.voiceName`.. | `string`.. | no | 語音名称 | - | - | - |

## Response Body

### 200

| name | type | required | description | enum | default | range |
|---|---|---|---|---|---|---|
| `candidates[]`.. | `array<object>`.. | no | - | - | - | - |
| `candidates[].content`.. | `object`.. | no | - | - | - | - |
| `candidates[].content.role`.. | `string`.. | no | 角色标识 | - | - | - |
| `candidates[].content.parts[]`.. | `array<object>`.. | no | - | - | - | - |
| `candidates[].content.parts[].text`.. | `string`.. | no | 文本內容 | - | - | - |
| `candidates[].content.parts[].inlineData`.. | `object`.. | no | - | - | - | - |
| `candidates[].content.parts[].inlineData.mimeType`.. | `string`.. | no | - | - | - | - |
| `candidates[].content.parts[].inlineData.data`.. | `string`.. | no | Base64 資料 | - | - | - |
| `candidates[].finishReason`.. | `string`.. | no | - | - | - | - |
| `usageMetadata`.. | `object`.. | no | - | - | - | - |
| `usageMetadata.promptTokenCount`.. | `integer`.. | no | - | - | - | - |
| `usageMetadata.candidatesTokenCount`.. | `integer`.. | no | - | - | - | - |
| `usageMetadata.totalTokenCount`.. | `integer`.. | no | - | - | - | - |

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
```..

### 4xx/5xx

| status | meaning |
|---|---|
| `400`.. | 請求參數錯誤 |
| `401`.. | 鑑權失败 |
| `429`.. | 請求过于频繁 |
| `500`.. | 服务端錯誤 |
## Code Examples

### cURL

```bash
curl -X POST "https://clawrouter.com/v1beta/models/gemini-2.5-flash-preview-tts:generateContent" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents": [{"parts": [{"text": "请用中文播报今天的天气摘要"}]}], "generationConfig": {"responseModalities": ["AUDIO"], "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": "Kore"}}}}}'
```..

### Python requests

```python
url = "https://clawrouter.com/v1beta/models/gemini-2.5-flash-preview-tts:generateContent"
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
```..
