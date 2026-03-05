# 原生Gemini格式

Gemini 音频生成接口。

可使用 gemini-2.5-flash-preview-tts 等模型。

## Endpoint
POST /v1beta/models/{model}:generateContent

## Path Parameters
| name | type | required | description |
|-----|-----|-----|-----|
| model | string | yes | 模型名称 |

## Request Example
```bash
curl https://api.newapi.pro/v1beta/models/gemini-2.5-flash-preview-tts:generateContent \
 -H "Authorization: Bearer $NEWAPI_API_KEY" \
 -H "Content-Type: application/json"
```
