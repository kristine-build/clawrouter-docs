# 文本转语音

AI 模型接口音频（Audio）原生OpenAI格式

# 文本转语音

将文本转换为音频

loading...


/`v1`/`audio`/`speech`

Send

Authorization

Body

## [Authorization](#authorization)

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

## [Request Body](#request-body)

application/json

model\*string

input\*string

要转换的文本

Length`length <= 4096`

voice\*string

Value in`"alloy" | "echo" | "fable" | "onyx" | "nova" | "shimmer"`

response\_format?string

Default`"mp3"`

Value in`"mp3" | "opus" | "aac" | "flac" | "wav" | "pcm"`

speed?number

Default`1`

Range`0.25 <= value <= 4`

## [Response Body](#response-body)

### 200 audio/mpeg

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/audio/speech" \  -H "Content-Type: application/json" \  -d '{    "model": "tts-1",    "input": "string",    "voice": "alloy"  }'
```

200

```
"string"
```
