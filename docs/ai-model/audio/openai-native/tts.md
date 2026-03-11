# 文本转语音

将文本转换为音频

## Endpoint

`POST /v1/audio/speech`

## Authorization

- **类型**：BearerAuth
- **位置**：`header`
- **示例**：`Authorization: Bearer <token>`
- **说明**：使用 Bearer Token 认证。

## Request Body

Content-Type: `application/json`

| name | type | required | description | enum | default | range |
| --- | --- | --- | --- | --- | --- | --- |
| model | string | yes | 模型名称 | `string` | - | - |
| input | string | yes | 要转换的文本 | - | - | length <= 4096 |
| voice | string | yes | 语音角色名 | `alloy`, `echo`, `fable`, `onyx`, `nova`, `shimmer` | - | - |
| response_format | string | no | 音频输出格式 | `mp3`, `opus`, `aac`, `flac`, `wav`, `pcm` | `mp3` | - |
| speed | number | no | 语音速度 | - | `1` | `0.25 <= value <= 4` |

### cURL

```bash
curl -X POST "https://docs.newapi.pro/v1/audio/speech" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"model": "tts-1", "input": "请用中文朗读今天的新闻摘要", "voice": "alloy", "response_format": "mp3", "speed": 1}'
```

### Python requests

```python
url = "https://docs.newapi.pro/v1/audio/speech"
headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "Content-Type": "application/json",
}
payload = {
    "model": "tts-1",
    "input": "请用中文朗读今天的新闻摘要",
    "voice": "alloy",
    "response_format": "mp3",
    "speed": 1,
}
resp = requests.post(url, headers=headers, json=payload, timeout=30)
print(resp.status_code)
print(resp.text)
```

## Response Body

| name | type | required | description | enum | default | range |
| --- | --- | --- | --- | --- | --- | --- |
| response | string | yes | 响应内容（二进制音频，通常按 response_format 编码） | - | - | - |

- 200 响应返回音频流（`audio/mpeg`）。
