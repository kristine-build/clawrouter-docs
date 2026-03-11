# 音频转录

将音频转换为文本

## Endpoint

**POST** `/v1/audio/transcriptions`

## Authorization

使用 Bearer Token（Authorization header）

```http
Authorization: Bearer <API_KEY>
```

## Request Body

`multipart/form-data`

| name | type | required | description |
|---|---|---|---|
| file | string (binary) | yes | 音频文件。 |
| model | string | yes | 模型名称，例如 `whisper-1`。 |
| language | string | no | ISO-639-1 语言代码。 |
| prompt | string | no | 提示词。 |
| response_format | string | no | 取值 `json` / `text` / `srt` / `verbose_json` / `vtt`。默认 `json`。 |
| temperature | number | no | 温度参数。 |
| timestamp_granularities[] | array<string> | no | 时间戳粒度控制。 |

## Response Body

### 200

```json
{
  "text": "string"
}
```

## Code Examples

```bash
curl -X POST "https://docs.newapi.pro/v1/audio/transcriptions" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -F "file=@/path/to/audio.mp3" \
  -F "model=whisper-1" \
  -F "response_format=json"
```

```python
import requests

url = "https://docs.newapi.pro/v1/audio/transcriptions"
headers = {"Authorization": "Bearer YOUR_API_KEY"}
files = {"file": open("/path/to/audio.mp3", "rb")}
data = {
    "model": "whisper-1",
    "response_format": "json",
}
response = requests.post(url, headers=headers, files=files, data=data)
print(response.status_code)
print(response.text)
```
