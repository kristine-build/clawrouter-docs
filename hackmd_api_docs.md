# ClawRouter API 文檔


[TOC]

---


## ai model

---


---

### audio


#### 原生gemini格式


AI 模型接口音频（Audio）

Gemini 音频生成接口。
可使用gemini-2.5-flash-preview-tts等模型

loading...

POST

/`v1beta`/`models`/`{model}:generateContent`

Send

Authorization

Path

Body

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Path Parameters

model\*string

模型名称

Request Body

application/json

contents\*array<object>

generationConfig\*object

Response Body

200 application/json

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

---

#### 文本转语音


AI 模型接口音频（Audio）原生OpenAI格式

将文本转换为音频

loading...

POST

/`v1`/`audio`/`speech`

Send

Authorization

Body

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Request Body

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

Response Body

200 audio/mpeg

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/audio/speech" \  -H "Content-Type: application/json" \  -d '{    "model": "tts-1",    "input": "string",    "voice": "alloy"  }'
```

200

```
"string"
```

---

#### 音频转录


AI 模型接口音频（Audio）原生OpenAI格式

将音频转换为文本

loading...

POST

/`v1`/`audio`/`transcriptions`

Send

Authorization

Body

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Request Body

multipart/form-data

file\*file

音频文檔

Format`binary`

model\*string

language?string

ISO-639-1 语言代码

prompt?string

response\_format?string

Default`"json"`

Value in`"json" | "text" | "srt" | "verbose_json" | "vtt"`

temperature?number

timestamp\_granularities?array<string>

Response Body

200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/audio/transcriptions" \  -F file="string" \  -F model="whisper-1"
```

200

```
{
  "text": "string"
}
```

---

#### 音频翻译


AI 模型接口音频（Audio）原生OpenAI格式

将音频翻译为英文文本

loading...

POST

/`v1`/`audio`/`translations`

Send

Authorization

Body

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Request Body

multipart/form-data

file\*file

Format`binary`

model\*string

prompt?string

response\_format?string

temperature?number

Response Body

200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/audio/translations" \  -F file="string" \  -F model="string"
```

200

```
{
  "text": "string"
}
```

---


### chat


#### 原生claude格式


AI 模型接口聊天（Chat）

Anthropic Claude Messages API 格式的请求。
需要在请求头中包含 `anthropic-version`。

loading...

POST

/`v1`/`messages`

Send

Authorization

Header

Body

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Header Parameters

anthropic-version\*string

Anthropic API 版本

x-api-key?string

Anthropic API Key (可选，也可使用 Bearer Token)

Request Body

application/json

model\*string

messages\*array<object>

system?string|array<object>

max\_tokens\*integer

Range`1 <= value`

temperature?number

Range`0 <= value <= 1`

top\_p?number

top\_k?integer

stream?boolean

stop\_sequences?array<string>

tools?array<object>

tool\_choice?object

thinking?object

metadata?object

Response Body

200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/messages" \  -H "anthropic-version: 2023-06-01" \  -H "Content-Type: application/json" \  -d '{    "model": "claude-3-opus-20240229",    "messages": [      {        "role": "user",        "content": "string"      }    ],    "max_tokens": 1  }'
```

200

```
{
  "id": "string",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "string",
      "text": "string"
    }
  ],
  "model": "string",
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 0,
    "output_tokens": 0,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0
  }
}
```

---

#### chatcompletions格式


AI 模型接口聊天（Chat）原生OpenAI格式

根据对话历史创建模型响应。支持流式和非流式响应。

兼容 OpenAI Chat Completions API。

loading...

POST

/`v1`/`chat`/`completions`

Send

Authorization

Body

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Request Body

application/json

model\*string

模型 ID

messages\*array<object>

对话消息列表

temperature?number

采样温度

Default`1`

Range`0 <= value <= 2`

top\_p?number

核采样参数

Default`1`

Range`0 <= value <= 1`

n?integer

生成数量

Default`1`

Range`1 <= value`

stream?boolean

是否流式响应

Default`false`

stream\_options?object

stop?string|array<string>

停止序列

max\_tokens?integer

最大生成 Token 数

max\_completion\_tokens?integer

最大补全 Token 数

presence\_penalty?number

Default`0`

Range`-2 <= value <= 2`

frequency\_penalty?number

Default`0`

Range`-2 <= value <= 2`

logit\_bias?object

user?string

tools?array<object>

tool\_choice?string|object

response\_format?object

seed?integer

reasoning\_effort?string

推理强度 (用于支持推理的模型)

Value in`"low" | "medium" | "high"`

modalities?array<string>

audio?object

Response Body

200 application/json

400 application/json

429 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/chat/completions" \  -H "Content-Type: application/json" \  -d '{    "model": "gpt-4",    "messages": [      {        "role": "system",        "content": "string"      }    ]  }'
```

200400429

```
{
  "id": "string",
  "object": "chat.completion",
  "created": 0,
  "model": "string",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "system",
        "content": "string",
        "name": "string",
        "tool_calls": [
          {
            "id": "string",
            "type": "function",
            "function": {
              "name": "string",
              "arguments": "string"
            }
          }
        ],
        "tool_call_id": "string",
        "reasoning_content": "string"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 0,
    "completion_tokens": 0,
    "total_tokens": 0,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "text_tokens": 0,
      "audio_tokens": 0,
      "image_tokens": 0
    },
    "completion_tokens_details": {
      "text_tokens": 0,
      "audio_tokens": 0,
      "reasoning_tokens": 0
    }
  },
  "system_fingerprint": "string"
}
```

```
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```

```
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```

---

#### responses格式


AI 模型接口聊天（Chat）原生OpenAI格式

OpenAI Responses API，用于创建模型响应。
支持多轮对话、工具调用、推理等功能。

loading...

POST

/`v1`/`responses`

Send

Authorization

Body

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Request Body

application/json

model\*string

input?string|array<object>

输入内容，可以是字符串或消息数组

instructions?string

max\_output\_tokens?integer

temperature?number

top\_p?number

stream?boolean

tools?array<object>

tool\_choice?string|object

reasoning?object

previous\_response\_id?string

truncation?string

Value in`"auto" | "disabled"`

Response Body

200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/responses" \  -H "Content-Type: application/json" \  -d '{    "model": "string"  }'
```

200

```
{
  "id": "string",
  "object": "response",
  "created_at": 0,
  "status": "completed",
  "model": "string",
  "output": [
    {
      "type": "string",
      "id": "string",
      "status": "string",
      "role": "string",
      "content": [
        {
          "type": "string",
          "text": "string"
        }
      ]
    }
  ],
  "usage": {
    "prompt_tokens": 0,
    "completion_tokens": 0,
    "total_tokens": 0,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "text_tokens": 0,
      "audio_tokens": 0,
      "image_tokens": 0
    },
    "completion_tokens_details": {
      "text_tokens": 0,
      "audio_tokens": 0,
      "reasoning_tokens": 0
    }
  }
}
```

---


### completions


#### 原生openai格式


AI 模型接口补全（Completions）

基于给定提示创建文本补全

loading...

POST

/`v1`/`completions`

Send

Authorization

Body

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Request Body

application/json

model\*string

prompt\*string|array<string>

max\_tokens?integer

temperature?number

top\_p?number

n?integer

stream?boolean

stop?string|array<string>

suffix?string

echo?boolean

Response Body

200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/completions" \  -H "Content-Type: application/json" \  -d '{    "model": "string",    "prompt": "string"  }'
```

200

```
{
  "id": "string",
  "object": "text_completion",
  "created": 0,
  "model": "string",
  "choices": [
    {
      "text": "string",
      "index": 0,
      "finish_reason": "string"
    }
  ],
  "usage": {
    "prompt_tokens": 0,
    "completion_tokens": 0,
    "total_tokens": 0,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "text_tokens": 0,
      "audio_tokens": 0,
      "image_tokens": 0
    },
    "completion_tokens_details": {
      "text_tokens": 0,
      "audio_tokens": 0,
      "reasoning_tokens": 0
    }
  }
}
```

---


### embeddings


#### 原生openai格式


AI 模型接口嵌入（Embeddings）

将文本转换为向量嵌入

loading...

POST

/`v1`/`embeddings`

Send

Authorization

Body

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Request Body

application/json

model\*string

input\*string|array<string>

要嵌入的文本

encoding\_format?string

Default`"float"`

Value in`"float" | "base64"`

dimensions?integer

输出向量维度

Response Body

200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/embeddings" \  -H "Content-Type: application/json" \  -d '{    "model": "text-embedding-ada-002",    "input": "string"  }'
```

200

```
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [
        0
      ]
    }
  ],
  "model": "string",
  "usage": {
    "prompt_tokens": 0,
    "total_tokens": 0
  }
}
```

---

#### 原生gemini格式


AI 模型接口嵌入（Embeddings）

使用指定引擎/模型创建嵌入

loading...

POST

/`v1`/`engines`/`{model}`/`embeddings`

Send

Authorization

Path

Body

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Path Parameters

model\*string

模型/引擎 ID

Request Body

application/json

model\*string

input\*string|array<string>

要嵌入的文本

encoding\_format?string

Default`"float"`

Value in`"float" | "base64"`

dimensions?integer

输出向量维度

Response Body

200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/engines/string/embeddings" \  -H "Content-Type: application/json" \  -d '{    "model": "text-embedding-ada-002",    "input": "string"  }'
```

200

```
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [
        0
      ]
    }
  ],
  "model": "string",
  "usage": {
    "prompt_tokens": 0,
    "total_tokens": 0
  }
}
```

---


### images


#### 编辑图像


AI 模型接口图像（Images）原生OpenAI格式

在给定原始图像和提示的情况下创建编辑或扩展图像。

loading...

POST

/`v1`/`images`/`edits`/

Send

Authorization

Body

Authorization

Bearer

AuthorizationBearer <token>

In: `header`

Request Body

multipart/form-data

image\*file

要编辑的图像。必须是有效的 PNG 文檔，小于 4MB，并且是方形的。如果未提供遮罩，图像必须具有透明度，将用作遮罩。

Format`binary`

mask?file

附加图像，其完全透明区域（例如，alpha 为零的区域）指示image应编辑的位置。必须是有效的 PNG 文檔，小于 4MB，并且尺寸与原始image相同。

Format`binary`

prompt\*string

所需图像的文本描述。最大长度为 1000 个字符。

n?string

要生成的图像数。必须介于 1 和 10 之间。

size?string

生成图像的大小。必须是`256x256`、`512x512`或 `1024x1024`之一。

response\_format?string

生成的图像返回的格式。必须是`url`或`b64_json`。

user?string

代表您的最终用户的唯一标识符，可以帮助 OpenAI 监控和检测滥用行为。[了解更多](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids)。

model?string

Response Body

200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/images/edits/" \  -F image="cmMtdXBsb2FkLTE2ODc4MzMzNDc3NTEtMjA=/31225951_59371037e9_small.png" \  -F prompt="A cute baby sea otter wearing a beret."
```

200

```
{}
```

---

#### 生成图像


AI 模型接口图像（Images）原生OpenAI格式

在给定提示的情况下创建图像。[了解更多](https://platform.openai.com/docs/guides/images)。

loading...

POST

/`v1`/`images`/`generations`/

Send

Authorization

Body

Authorization

Bearer

AuthorizationBearer <token>

In: `header`

Request Body

application/json

model?string

用于图像生成的模型。`dall-e-2`、`dall-e-3` 或 `gpt-image-1` 之一。默认为 `dall-e-2`，除非使用特定于 `gpt-image-1` 的参数。

prompt\*string

所需图像的文本描述。`gpt-image-1` 的最大长度为 32000 个字符，`dall-e-2` 的最大长度为 1000 个字符，`dall-e-3` 的最大长度为 4000 个字符。

n?integer

要生成的图像数量。必须介于 1 到 10 之间。对于 `dall-e-3`，仅支持 `n=1`。

size?string

生成的图像的大小。`对于 gpt-image-1`，必须是 `1024x1024`、`1536x1024`（横向）、`1024x1536`（纵向）或`自动`（默认值）之一，`对于 dall-e-2`，必须是 ``` 256x256、``512x512 ``` 或 `1024x1024` 之一，对于 `dall-e-3`，必须是 `1024x1024`、`1792x1024` 或 `1024x1792` 之一。

background?string

允许为生成的图像的背景设置透明度。此参数仅支持 `gpt-image-1`。必须是以下之一 `透明`、`不透明`或`自动`（默认值）。使用`自动`时，模型将自动确定图像的最佳背景。

如果`是透明`的，则输出格式需要支持透明度，因此应将其设置为 `png`（默认值）或 `webp`。

moderation?string

控制 `gpt-image-1` 生成的图像的内容审核级别。必须为`低，` 以进行限制较少的筛选或`自动`（默认值）。

quality?string

将生成的图像的质量。

stream?string

style?string

user?string

Response Body

200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/images/generations/" \  -H "Content-Type: application/json" \  -d '{    "prompt": "string"  }'
```

200

```
{
  "created": 0,
  "data": [
    {
      "b64_json": "string",
      "url": "string"
    }
  ],
  "usage": {
    "total_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0,
    "input_tokens_details": {
      "text_tokens": 0,
      "image_tokens": 0
    }
  }
}
```

---


### models


#### 原生openai格式


AI 模型接口模型（Models）列出模型

获取当前可用的模型列表。

根据请求头自动识别返回格式：

- 包含 `x-api-key` 和 `anthropic-version` 头时返回 Anthropic 格式
- 包含 `x-goog-api-key` 头或 `key` 查询参数时返回 Gemini 格式
- 其他情况返回 OpenAI 格式

loading...

GET

/`v1`/`models`

Send

Authorization

Header

Query

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Query Parameters

key?string

Google API Key (用于 Gemini 格式)

Header Parameters

x-api-key?string

Anthropic API Key (用于 Claude 格式)

anthropic-version?string

Anthropic API 版本

x-goog-api-key?string

Google API Key (用于 Gemini 格式)

Response Body

200 application/json

401 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/v1/models"
```

200401

```
{
  "object": "list",
  "data": [
    {
      "id": "gpt-4",
      "object": "model",
      "created": 0,
      "owned_by": "openai"
    }
  ]
}
```

```
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```

---

#### 原生gemini格式


AI 模型接口模型（Models）列出模型

以 Gemini API 格式返回可用模型列表

loading...

GET

/`v1beta`/`models`

Send

Authorization

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Response Body

200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/v1beta/models"
```

200

```
{
  "models": [
    {
      "name": "models/gemini-pro",
      "version": "string",
      "displayName": "string",
      "description": "string",
      "inputTokenLimit": 0,
      "outputTokenLimit": 0,
      "supportedGenerationMethods": [
        "string"
      ]
    }
  ]
}
```

---


### moderations


#### 原生openai格式


AI 模型接口审查（Moderations）

检查文本内容是否违反使用政策

loading...

POST

/`v1`/`moderations`

Send

Authorization

Body

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Request Body

application/json

input\*string|array<string>

model?string

Response Body

200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/moderations" \  -H "Content-Type: application/json" \  -d '{    "input": "string"  }'
```

200

```
{
  "id": "string",
  "model": "string",
  "results": [
    {
      "flagged": true,
      "categories": {},
      "category_scores": {}
    }
  ]
}
```

---


### realtime


#### 原生openai格式


AI 模型接口实时语音（Realtime）

创建 WebSocket 连接用于实时对话。

**注意**: 这是一个 WebSocket 端点，需要使用 WebSocket 协议连接。

连接 URL 示例: `wss://api.example.com/v1/realtime?model=gpt-4o-realtime`

loading...

GET

/`v1`/`realtime`

Send

Authorization

Query

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Query Parameters

model?string

要使用的模型

Response Body

101

400 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/v1/realtime"
```

101400

Empty

```
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```

---


### rerank


#### 文檔重排序


AI 模型接口重排序（Rerank）

根据查询对文檔列表进行相关性重排序

loading...

POST

/`v1`/`rerank`

Send

Authorization

Body

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Request Body

application/json

model\*string

query\*string

查询文本

documents\*array<string | object>

要重排序的文檔列表

top\_n?integer

返回前 N 个结果

return\_documents?boolean

Default`false`

Response Body

200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/rerank" \  -H "Content-Type: application/json" \  -d '{    "model": "rerank-english-v2.0",    "query": "string",    "documents": [      "string"    ]  }'
```

200

```
{
  "id": "string",
  "results": [
    {
      "index": 0,
      "relevance_score": 0,
      "document": {}
    }
  ],
  "meta": {}
}
```

---


### unimplemented


#### 上传文檔


AI 模型接口未实现（Unimplemented）文檔（Files）

此接口尚未实现

loading...

POST

/`v1`/`files`

Send

Authorization

Body

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Request Body

multipart/form-data

file?file

Format`binary`

purpose?string

Response Body

501 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/files"
```

501

```
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```

---

#### 删除文檔


AI 模型接口未实现（Unimplemented）文檔（Files）

此接口尚未实现

loading...

DELETE

/`v1`/`files`/`{file_id}`

Send

Authorization

Path

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Path Parameters

file\_id\*string

Response Body

501 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X DELETE "https://loading/v1/files/string"
```

501

```
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```

---

#### 获取文檔内容


AI 模型接口未实现（Unimplemented）文檔（Files）

此接口尚未实现

loading...

GET

/`v1`/`files`/`{file_id}`/`content`

Send

Authorization

Path

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Path Parameters

file\_id\*string

Response Body

501 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/v1/files/string/content"
```

501

```
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```

---

#### 列出文檔


AI 模型接口未实现（Unimplemented）文檔（Files）

此接口尚未实现

loading...

GET

/`v1`/`files`

Send

Authorization

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Response Body

501 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/v1/files"
```

501

```
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```

---

#### 获取文檔信息


AI 模型接口未实现（Unimplemented）文檔（Files）

此接口尚未实现

loading...

GET

/`v1`/`files`/`{file_id}`

Send

Authorization

Path

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Path Parameters

file\_id\*string

Response Body

501 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/v1/files/string"
```

501

```
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```

---


### videos


#### 创建视频生成任务


AI 模型接口视频（Videos）

提交视频生成任务，支持文生视频和图生视频。

返回任务 ID，可通过 GET 接口查询任务状态。

loading...

POST

/`v1`/`video`/`generations`

Send

Authorization

Body

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Request Body

application/json

model?string

模型/风格 ID

prompt?string

文本描述提示词

image?string

图片输入 (URL 或 Base64)

duration?number

视频时长（秒）

width?integer

视频宽度

height?integer

视频高度

fps?integer

视频帧率

seed?integer

随机种子

n?integer

生成视频数量

response\_format?string

响应格式

user?string

用户标识

metadata?object

扩展参数 (如 negative\_prompt, style, quality\_level 等)

Response Body

200 application/json

400 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/video/generations" \  -H "Content-Type: application/json" \  -d '{}'
```

200400

```
{
  "task_id": "abcd1234efgh",
  "status": "queued"
}
```

```
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```

---

#### 获取视频生成任务状态


AI 模型接口视频（Videos）

查询视频生成任务的状态和结果。

任务状态：

- `queued`: 排队中
- `in_progress`: 生成中
- `completed`: 已完成
- `failed`: 失败

loading...

GET

/`v1`/`video`/`generations`/`{task_id}`

Send

Authorization

Path

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Path Parameters

task\_id\*string

任务 ID

Response Body

200 application/json

404 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/v1/video/generations/string"
```

200404

```
{
  "task_id": "abcd1234efgh",
  "status": "completed",
  "url": "https://example.com/video.mp4",
  "format": "mp4",
  "metadata": {
    "duration": 5,
    "fps": 30,
    "width": 1280,
    "height": 720,
    "seed": 20231234
  },
  "error": {
    "code": 0,
    "message": "string"
  }
}
```

```
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```

---

#### 创建视频


AI 模型接口视频（Videos）Sora格式

OpenAI 兼容的视频生成接口。

参考文檔: <https://platform.openai.com/docs/api-reference/videos/create>

loading...

POST

/`v1`/`videos`

Send

Authorization

Body

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Request Body

multipart/form-data

model?string

模型/风格 ID

prompt?string

文本描述提示词

image?string

图片输入 (URL 或 Base64)

duration?number

视频时长（秒）

width?integer

视频宽度

height?integer

视频高度

fps?integer

视频帧率

seed?integer

随机种子

n?integer

生成视频数量

response\_format?string

响应格式

user?string

用户标识

metadata?object

扩展参数 (如 negative\_prompt, style, quality\_level 等)

Response Body

200 application/json

400 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/videos"
```

200400

```
{
  "id": "string",
  "object": "string",
  "model": "string",
  "status": "string",
  "progress": 0,
  "created_at": 0,
  "seconds": "string",
  "completed_at": 0,
  "expires_at": 0,
  "size": "string",
  "error": {
    "message": "string",
    "code": "string"
  },
  "metadata": {}
}
```

```
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```

---

#### 获取视频任务状态


AI 模型接口视频（Videos）Sora格式

OpenAI 兼容的视频任务状态查询接口。

返回视频任务的详细状态信息。

loading...

GET

/`v1`/`videos`/`{task_id}`

Send

Authorization

Path

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Path Parameters

task\_id\*string

视频任务 ID

Response Body

200 application/json

404 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/v1/videos/string"
```

200404

```
{
  "id": "string",
  "object": "string",
  "model": "string",
  "status": "string",
  "progress": 0,
  "created_at": 0,
  "seconds": "string"
}
```

```
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```

---

#### 获取视频内容


AI 模型接口视频（Videos）Sora格式

获取已完成视频任务的视频文檔内容。

此接口会代理返回视频文檔流。

loading...

GET

/`v1`/`videos`/`{task_id}`/`content`

Send

Authorization

Path

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Path Parameters

task\_id\*string

视频任务 ID

Response Body

200 video/mp4

404 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/v1/videos/string/content"
```

200404

```
"string"
```

```
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```

---


---


## management

---


---

### auth


鉴权体系说明auth

管理接口

后台管理接口鉴权方式与权限级别说明

说明

后台管理接口采用多级鉴权机制，常见为：**公开**、**用户**、**管理员**、**Root**。

认证方式（二选一）

Session

通过登录接口获取 Session：

- `POST /api/user/login`

Access Token（推荐）

在请求头中携带：

```
Authorization: Bearer {token}
```

Token 可在「个人设置 - 安全设置 - 系统访问令牌」中生成。

必需请求头

部分接口要求携带用户标识请求头：

```
New-Api-User: {user_id}
```

其中 `{user_id}` 必须与当前登录用户匹配。

权限级别

- **公开（Public）**：无需鉴权
- **用户（User）**：需要登录或 Access Token
- **管理员（Admin）**：需要管理员权限
- **Root**：最高权限

---


### channel management


批量删除渠道

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

POST

/`api`/`channel`/`batch`

Send

Body

Request Body

application/json

ids?array<integer>

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/channel/batch" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

批量设置渠道标签

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

POST

/`api`/`channel`/`batch`/`tag`

Send

Body

Request Body

application/json

ids?array<integer>

tag?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/channel/batch/tag" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

复制渠道

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

POST

/`api`/`channel`/`copy`/`{id}`

Send

Path

Query

Path Parameters

id\*integer

Query Parameters

suffix?string

reset\_balance?boolean

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/channel/copy/0"
```

200

Empty

---

删除已禁用渠道

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

DELETE

/`api`/`channel`/`disabled`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X DELETE "https://loading/api/channel/disabled"
```

200

Empty

---

获取上游模型列表

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`channel`/`fetch_models`/`{id}`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/channel/fetch_models/0"
```

200

Empty

---

获取模型列表

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

POST

/`api`/`channel`/`fetch_models`

Send

Body

Request Body

application/json

base\_url?string

type?integer

key?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/channel/fetch_models" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

修复渠道能力

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

POST

/`api`/`channel`/`fix`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/channel/fix"
```

200

Empty

---

获取所有渠道

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`channel`/

Send

Query

Query Parameters

p?integer

page\_size?integer

id\_sort?boolean

tag\_mode?boolean

status?string

type?integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/channel/"
```

200

Empty

---

删除渠道

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

DELETE

/`api`/`channel`/`{id}`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X DELETE "https://loading/api/channel/0"
```

200

Empty

---

获取指定渠道

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`channel`/`{id}`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/channel/0"
```

200

Empty

---

获取渠道密钥

管理接口渠道管理

👑 需要超级管理员权限（Root）+ 安全验证

loading...

POST

/`api`/`channel`/`{id}`/`key`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/channel/0/key"
```

200

Empty

---

获取渠道模型列表

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`channel`/`models`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/channel/models"
```

200

Empty

---

获取已启用模型列表

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`channel`/`models_enabled`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/channel/models_enabled"
```

200

Empty

---

管理多密钥

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

POST

/`api`/`channel`/`multi_key`/`manage`

Send

Body

Request Body

application/json

channel\_id?integer

action?string

Value in`"get_key_status" | "disable_key" | "enable_key" | "delete_key" | "delete_disabled_keys" | "enable_all_keys" | "disable_all_keys"`

key\_index?integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/channel/multi_key/manage" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

添加渠道

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

POST

/`api`/`channel`/

Send

Body

Request Body

application/json

mode?string

Value in`"single" | "batch" | "multi_to_single"`

channel?object

Unresolved $ref: #/definitions/224188811

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/channel/" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

更新渠道

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

PUT

/`api`/`channel`/

Send

Body

Request Body

application/json

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X PUT "https://loading/api/channel/" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

搜索渠道

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`channel`/`search`

Send

Query

Query Parameters

keyword?string

group?string

model?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/channel/search"
```

200

Empty

---

禁用标签渠道

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

POST

/`api`/`channel`/`tag`/`disabled`

Send

Body

Request Body

application/json

tag?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/channel/tag/disabled" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

启用标签渠道

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

POST

/`api`/`channel`/`tag`/`enabled`

Send

Body

Request Body

application/json

tag?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/channel/tag/enabled" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

获取标签模型

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`channel`/`tag`/`models`

Send

Query

Query Parameters

tag\*string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/channel/tag/models?tag=string"
```

200

Empty

---

编辑标签渠道

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

PUT

/`api`/`channel`/`tag`

Send

Body

Request Body

application/json

tag?string

new\_tag?string

priority?integer

weight?integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X PUT "https://loading/api/channel/tag" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

测试所有渠道

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`channel`/`test`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/channel/test"
```

200

Empty

---

测试指定渠道

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`channel`/`test`/`{id}`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/channel/test/0"
```

200

Empty

---

更新所有渠道余额

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`channel`/`update_balance`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/channel/update_balance"
```

200

Empty

---

更新指定渠道余额

管理接口渠道管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`channel`/`update_balance`/`{id}`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/channel/update_balance/0"
```

200

Empty

---


### groups


获取所有分组

管理接口分组

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`group`/

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/group/"
```

200

Empty

---

获取预填分组

管理接口分组

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`prefill_group`/

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/prefill_group/"
```

200

Empty

---

删除预填分组

管理接口分组

👨💼 需要管理员权限（Admin）

loading...

DELETE

/`api`/`prefill_group`/`{id}`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X DELETE "https://loading/api/prefill_group/0"
```

200

Empty

---

创建预填分组

管理接口分组

👨💼 需要管理员权限（Admin）

loading...

POST

/`api`/`prefill_group`/

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/prefill_group/"
```

200

Empty

---

更新预填分组

管理接口分组

👨💼 需要管理员权限（Admin）

loading...

PUT

/`api`/`prefill_group`/

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X PUT "https://loading/api/prefill_group/"
```

200

Empty

---


### logs


删除历史日志

管理接口日志

👨💼 需要管理员权限（Admin）

loading...

DELETE

/`api`/`log`/

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X DELETE "https://loading/api/log/"
```

200

Empty

---

获取所有日志

管理接口日志

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`log`/

Send

Query

Query Parameters

p?integer

page\_size?integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/log/"
```

200

Empty

---

搜索日志

管理接口日志

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`log`/`search`

Send

Query

Query Parameters

keyword?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/log/search"
```

200

Empty

---

获取个人日志

管理接口日志

🔐 需要登录（User权限）

loading...

GET

/`api`/`log`/`self`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/log/self"
```

200

Empty

---

搜索个人日志

管理接口日志

🔐 需要登录（User权限）

loading...

GET

/`api`/`log`/`self`/`search`

Send

Query

Query Parameters

keyword?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/log/self/search"
```

200

Empty

---

获取个人日志统计

管理接口日志

🔐 需要登录（User权限）

loading...

GET

/`api`/`log`/`self`/`stat`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/log/self/stat"
```

200

Empty

---

获取日志统计

管理接口日志

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`log`/`stat`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/log/stat"
```

200

Empty

---

通过令牌获取日志

管理接口日志

🔓 无需鉴权（通过令牌查询）

loading...

GET

/`api`/`log`/`token`

Send

Query

Query Parameters

key?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/log/token"
```

200

Empty

---


### model management


获取所有模型元数据

管理接口模型管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`models`/

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/models/"
```

200

Empty

---

删除模型

管理接口模型管理

👨💼 需要管理员权限（Admin）

loading...

DELETE

/`api`/`models`/`{id}`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X DELETE "https://loading/api/models/0"
```

200

Empty

---

获取指定模型

管理接口模型管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`models`/`{id}`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/models/0"
```

200

Empty

---

获取缺失模型

管理接口模型管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`models`/`missing`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/models/missing"
```

200

Empty

---

创建模型元数据

管理接口模型管理

👨💼 需要管理员权限（Admin）

loading...

POST

/`api`/`models`/

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/models/"
```

200

Empty

---

更新模型元数据

管理接口模型管理

👨💼 需要管理员权限（Admin）

loading...

PUT

/`api`/`models`/

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X PUT "https://loading/api/models/"
```

200

Empty

---

搜索模型

管理接口模型管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`models`/`search`

Send

Query

Query Parameters

keyword?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/models/search"
```

200

Empty

---

同步上游模型

管理接口模型管理

👨💼 需要管理员权限（Admin）

loading...

POST

/`api`/`models`/`sync_upstream`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/models/sync_upstream"
```

200

Empty

---

预览上游模型同步

管理接口模型管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`models`/`sync_upstream`/`preview`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/models/sync_upstream/preview"
```

200

Empty

---


### oauth


discord oauth登录

管理接口OAuth

🔓 无需鉴权（OAuth回调）

loading...

GET

/`api`/`oauth`/`discord`

Send

Query

Query Parameters

code?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/oauth/discord"
```

200

Empty

---

绑定邮箱

管理接口OAuth

🔓 无需鉴权

loading...

GET

/`api`/`oauth`/`email`/`bind`

Send

Query

Query Parameters

email?string

code?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/oauth/email/bind"
```

200

Empty

---

github oauth登录

管理接口OAuth

🔓 无需鉴权（OAuth回调）

loading...

GET

/`api`/`oauth`/`github`

Send

Query

Query Parameters

code?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/oauth/github"
```

200

Empty

---

linuxdo oauth登录

管理接口OAuth

🔓 无需鉴权（OAuth回调）

loading...

GET

/`api`/`oauth`/`linuxdo`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/oauth/linuxdo"
```

200

Empty

---

oidc登录

管理接口OAuth

🔓 无需鉴权（OAuth回调）

loading...

GET

/`api`/`oauth`/`oidc`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/oauth/oidc"
```

200

Empty

---

生成oauth state

管理接口OAuth

🔓 无需鉴权

loading...

GET

/`api`/`oauth`/`state`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/oauth/state"
```

200

Empty

---

绑定telegram

管理接口OAuth

🔓 无需鉴权

loading...

GET

/`api`/`oauth`/`telegram`/`bind`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/oauth/telegram/bind"
```

200

Empty

---

telegram登录

管理接口OAuth

🔓 无需鉴权（OAuth回调）

loading...

GET

/`api`/`oauth`/`telegram`/`login`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/oauth/telegram/login"
```

200

Empty

---

绑定微信

管理接口OAuth

🔓 无需鉴权

loading...

GET

/`api`/`oauth`/`wechat`/`bind`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/oauth/wechat/bind"
```

200

Empty

---

微信oauth登录

管理接口OAuth

🔓 无需鉴权（OAuth回调）

loading...

GET

/`api`/`oauth`/`wechat`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/oauth/wechat"
```

200

Empty

---


### payment


creem webhook

管理接口充值

🔓 无需鉴权（Webhook回调）

loading...

POST

/`api`/`creem`/`webhook`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/creem/webhook"
```

200

Empty

---

stripe webhook

管理接口充值

🔓 无需鉴权（Webhook回调）

loading...

POST

/`api`/`stripe`/`webhook`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/stripe/webhook"
```

200

Empty

---

获取支付金额

管理接口充值

🔐 需要登录（User权限）

loading...

POST

/`api`/`user`/`amount`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/amount"
```

200

Empty

---

发起creem支付

管理接口充值

🔐 需要登录（User权限）

loading...

POST

/`api`/`user`/`creem`/`pay`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/creem/pay"
```

200

Empty

---

易支付回调

管理接口充值

🔓 无需鉴权（支付回调）

loading...

GET

/`api`/`user`/`epay`/`notify`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/user/epay/notify"
```

200

Empty

---

发起易支付

管理接口充值

🔐 需要登录（User权限）

loading...

POST

/`api`/`user`/`pay`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/pay"
```

200

Empty

---

获取stripe支付金额

管理接口充值

🔐 需要登录（User权限）

loading...

POST

/`api`/`user`/`stripe`/`amount`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/stripe/amount"
```

200

Empty

---

发起stripe支付

管理接口充值

🔐 需要登录（User权限）

loading...

POST

/`api`/`user`/`stripe`/`pay`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/stripe/pay"
```

200

Empty

---

获取充值信息

管理接口充值

🔐 需要登录（User权限）

loading...

GET

/`api`/`user`/`topup`/`info`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/user/topup/info"
```

200

Empty

---

获取用户充值记录

管理接口充值

🔐 需要登录（User权限）

loading...

GET

/`api`/`user`/`topup`/`self`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/user/topup/self"
```

200

Empty

---


### redemption


获取所有兑换码

管理接口兑换码

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`redemption`/

Send

Query

Query Parameters

p?integer

page\_size?integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/redemption/"
```

200

Empty

---

删除兑换码

管理接口兑换码

👨💼 需要管理员权限（Admin）

loading...

DELETE

/`api`/`redemption`/`{id}`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X DELETE "https://loading/api/redemption/0"
```

200

Empty

---

获取指定兑换码

管理接口兑换码

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`redemption`/`{id}`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/redemption/0"
```

200

Empty

---

删除无效兑换码

管理接口兑换码

👨💼 需要管理员权限（Admin）

loading...

DELETE

/`api`/`redemption`/`invalid`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X DELETE "https://loading/api/redemption/invalid"
```

200

Empty

---

创建兑换码

管理接口兑换码

👨💼 需要管理员权限（Admin）

loading...

POST

/`api`/`redemption`/

Send

Body

Request Body

application/json

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/redemption/" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

更新兑换码

管理接口兑换码

👨💼 需要管理员权限（Admin）

loading...

PUT

/`api`/`redemption`/

Send

Body

Request Body

application/json

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X PUT "https://loading/api/redemption/" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

搜索兑换码

管理接口兑换码

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`redemption`/`search`

Send

Query

Query Parameters

keyword?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/redemption/search"
```

200

Empty

---


### security verification


通用安全验证

管理接口安全验证

🔐 需要登录（User权限）

loading...

POST

/`api`/`verify`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/verify"
```

200

Empty

---

获取验证状态

管理接口安全验证

🔐 需要登录（User权限）

loading...

GET

/`api`/`verify`/`status`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/verify/status"
```

200

Empty

---


### statistics


获取所有额度数据

管理接口数据统计

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`data`/

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/data/"
```

200

Empty

---

获取个人额度数据

管理接口数据统计

🔐 需要登录（User权限）

loading...

GET

/`api`/`data`/`self`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/data/self"
```

200

Empty

---


### system settings


获取系统选项

管理接口系统设置

👑 需要超级管理员权限（Root）

loading...

GET

/`api`/`option`/

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/option/"
```

200

Empty

---

迁移控制台设置

管理接口系统设置

👑 需要超级管理员权限（Root）

loading...

POST

/`api`/`option`/`migrate_console_setting`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/option/migrate_console_setting"
```

200

Empty

---

更新系统选项

管理接口系统设置

👑 需要超级管理员权限（Root）

loading...

PUT

/`api`/`option`/

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X PUT "https://loading/api/option/"
```

200

Empty

---

重置模型倍率

管理接口系统设置

👑 需要超级管理员权限（Root）

loading...

POST

/`api`/`option`/`rest_model_ratio`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/option/rest_model_ratio"
```

200

Empty

---

获取可同步渠道

管理接口系统设置

👑 需要超级管理员权限（Root）

loading...

GET

/`api`/`ratio_sync`/`channels`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/ratio_sync/channels"
```

200

Empty

---

获取上游倍率

管理接口系统设置

👑 需要超级管理员权限（Root）

loading...

POST

/`api`/`ratio_sync`/`fetch`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/ratio_sync/fetch"
```

200

Empty

---


### system


获取关于信息

管理接口系统

🔓 无需鉴权

loading...

GET

/`api`/`about`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/about"
```

200

Empty

---

获取首页内容

管理接口系统

🔓 无需鉴权

loading...

GET

/`api`/`home_page_content`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/home_page_content"
```

200

Empty

---

获取模型列表

管理接口系统

🔐 需要登录（User权限）

loading...

GET

/`api`/`models`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/models"
```

200

Empty

---

获取公告

管理接口系统

🔓 无需鉴权

loading...

GET

/`api`/`notice`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/notice"
```

200

Empty

---

获取定价信息

管理接口系统

🔓 无需鉴权（可选登录）

loading...

GET

/`api`/`pricing`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/pricing"
```

200

Empty

---

获取隐私政策

管理接口系统

🔓 无需鉴权

loading...

GET

/`api`/`privacy-policy`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/privacy-policy"
```

200

Empty

---

获取倍率配置

管理接口系统

🔓 无需鉴权

loading...

GET

/`api`/`ratio_config`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/ratio_config"
```

200

Empty

---

获取初始化状态

管理接口系统

🔓 无需鉴权

loading...

GET

/`api`/`setup`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/setup"
```

200

Empty

---

初始化系统

管理接口系统

🔓 无需鉴权

loading...

POST

/`api`/`setup`

Send

Body

Request Body

application/json

username?string

password?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/setup" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

获取系统状态

管理接口系统

🔓 无需鉴权

loading...

GET

/`api`/`status`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/status"
```

200

Empty

---

测试系统状态

管理接口系统

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`status`/`test`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/status/test"
```

200

Empty

---

获取uptime kuma状态

管理接口系统

🔓 无需鉴权

loading...

GET

/`api`/`uptime`/`status`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/uptime/status"
```

200

Empty

---

获取用户协议

管理接口系统

🔓 无需鉴权

loading...

GET

/`api`/`user-agreement`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/user-agreement"
```

200

Empty

---


### tasks


获取所有midjourney任务

管理接口任务

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`mj`/

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/mj/"
```

200

Empty

---

获取个人midjourney任务

管理接口任务

🔐 需要登录（User权限）

loading...

GET

/`api`/`mj`/`self`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/mj/self"
```

200

Empty

---

获取所有任务

管理接口任务

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`task`/

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/task/"
```

200

Empty

---

获取个人任务

管理接口任务

🔐 需要登录（User权限）

loading...

GET

/`api`/`task`/`self`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/task/self"
```

200

Empty

---


### token management


批量删除令牌

管理接口令牌管理

🔐 需要登录（User权限）

loading...

POST

/`api`/`token`/`batch`

Send

Body

Request Body

application/json

ids?array<integer>

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/token/batch" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

获取所有令牌

管理接口令牌管理

🔐 需要登录（User权限）

loading...

GET

/`api`/`token`/

Send

Query

Query Parameters

p?integer

page\_size?integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/token/"
```

200

Empty

---

删除令牌

管理接口令牌管理

🔐 需要登录（User权限）

loading...

DELETE

/`api`/`token`/`{id}`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X DELETE "https://loading/api/token/0"
```

200

Empty

---

获取指定令牌

管理接口令牌管理

🔐 需要登录（User权限）

loading...

GET

/`api`/`token`/`{id}`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/token/0"
```

200

Empty

---

创建令牌

管理接口令牌管理

🔐 需要登录（User权限）

loading...

POST

/`api`/`token`/

Send

Body

Request Body

application/json

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/token/" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

更新令牌

管理接口令牌管理

🔐 需要登录（User权限）

loading...

PUT

/`api`/`token`/

Send

Body

Request Body

application/json

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X PUT "https://loading/api/token/" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

搜索令牌

管理接口令牌管理

🔐 需要登录（User权限）

loading...

GET

/`api`/`token`/`search`

Send

Query

Query Parameters

keyword?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/token/search"
```

200

Empty

---

获取令牌使用情况

管理接口令牌管理

🔑 需要令牌认证（TokenAuth）

loading...

GET

/`api`/`usage`/`token`/

Send

Authorization

Header

Authorization

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

Header Parameters

Authorization?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/usage/token/"
```

200

Empty

---


### two factor auth


重新生成备用码

管理接口两步验证

🔐 需要登录（User权限）

loading...

POST

/`api`/`user`/`2fa`/`backup_codes`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/2fa/backup_codes"
```

200

Empty

---

禁用2fa

管理接口两步验证

🔐 需要登录（User权限）

loading...

POST

/`api`/`user`/`2fa`/`disable`

Send

Body

Request Body

application/json

code?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/2fa/disable" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

启用2fa

管理接口两步验证

🔐 需要登录（User权限）

loading...

POST

/`api`/`user`/`2fa`/`enable`

Send

Body

Request Body

application/json

code?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/2fa/enable" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

设置2fa

管理接口两步验证

🔐 需要登录（User权限）

loading...

POST

/`api`/`user`/`2fa`/`setup`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/2fa/setup"
```

200

Empty

---

获取2fa统计

管理接口两步验证

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`user`/`2fa`/`stats`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/user/2fa/stats"
```

200

Empty

---

获取2fa状态

管理接口两步验证

🔐 需要登录（User权限）

loading...

GET

/`api`/`user`/`2fa`/`status`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/user/2fa/status"
```

200

Empty

---


### user auth


发送密码重置邮件

管理接口用户登陆注册

🔓 无需鉴权

loading...

GET

/`api`/`reset_password`

Send

Query

Query Parameters

email\*string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/reset_password?email=string"
```

200

Empty

---

获取用户分组列表

管理接口用户登陆注册

🔓 无需鉴权

loading...

GET

/`api`/`user`/`groups`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/user/groups"
```

200

Empty

---

两步验证登录

管理接口用户登陆注册

🔓 无需鉴权（登录流程）

loading...

POST

/`api`/`user`/`login`/`2fa`

Send

Body

Request Body

application/json

code?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/login/2fa" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

用户登录

管理接口用户登陆注册

🔓 无需鉴权

loading...

POST

/`api`/`user`/`login`

Send

Body

Request Body

application/json

username?string

password?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/login" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

用户登出

管理接口用户登陆注册

🔓 无需鉴权

loading...

GET

/`api`/`user`/`logout`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/user/logout"
```

200

Empty

---

开始passkey登录

管理接口用户登陆注册

🔓 无需鉴权

loading...

POST

/`api`/`user`/`passkey`/`login`/`begin`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/passkey/login/begin"
```

200

Empty

---

完成passkey登录

管理接口用户登陆注册

🔓 无需鉴权

loading...

POST

/`api`/`user`/`passkey`/`login`/`finish`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/passkey/login/finish"
```

200

Empty

---

用户注册

管理接口用户登陆注册

🔓 无需鉴权

loading...

POST

/`api`/`user`/`register`

Send

Body

Request Body

application/json

username?string

password?string

email?string

verification\_code?string

aff\_code?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/register" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

重置密码

管理接口用户登陆注册

🔓 无需鉴权

loading...

POST

/`api`/`user`/`reset`

Send

Body

Request Body

application/json

email?string

token?string

password?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/reset" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

发送邮箱验证码

管理接口用户登陆注册

🔓 无需鉴权

loading...

GET

/`api`/`verification`

Send

Query

Query Parameters

email\*string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/verification?email=string"
```

200

Empty

---


### user management


获取邀请码

管理接口用户管理

🔐 需要登录（User权限）

loading...

GET

/`api`/`user`/`aff`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/user/aff"
```

200

Empty

---

转换邀请额度

管理接口用户管理

🔐 需要登录（User权限）

loading...

POST

/`api`/`user`/`aff_transfer`

Send

Body

Request Body

application/json

quota?integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/aff_transfer" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

获取所有用户

管理接口用户管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`user`/

Send

Query

Query Parameters

p?integer

page\_size?integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/user/"
```

200

Empty

---

管理员禁用用户2fa

管理接口用户管理

👨💼 需要管理员权限（Admin）

loading...

DELETE

/`api`/`user`/`{id}`/`2fa`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X DELETE "https://loading/api/user/0/2fa"
```

200

Empty

---

删除用户

管理接口用户管理

👨💼 需要管理员权限（Admin）

loading...

DELETE

/`api`/`user`/`{id}`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X DELETE "https://loading/api/user/0"
```

200

Empty

---

获取指定用户

管理接口用户管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`user`/`{id}`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/user/0"
```

200

Empty

---

管理员重置用户passkey

管理接口用户管理

👨💼 需要管理员权限（Admin）

loading...

DELETE

/`api`/`user`/`{id}`/`reset_passkey`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X DELETE "https://loading/api/user/0/reset_passkey"
```

200

Empty

---

管理用户状态

管理接口用户管理

👨💼 需要管理员权限（Admin）

loading...

POST

/`api`/`user`/`manage`

Send

Body

Request Body

application/json

id?integer

action?string

Value in`"disable" | "enable" | "delete" | "promote" | "demote"`

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/manage" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

获取用户可用模型

管理接口用户管理

🔐 需要登录（User权限）

loading...

GET

/`api`/`user`/`models`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/user/models"
```

200

Empty

---

删除passkey

管理接口用户管理

🔐 需要登录（User权限）

loading...

DELETE

/`api`/`user`/`passkey`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X DELETE "https://loading/api/user/passkey"
```

200

Empty

---

获取passkey状态

管理接口用户管理

🔐 需要登录（User权限）

loading...

GET

/`api`/`user`/`passkey`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/user/passkey"
```

200

Empty

---

开始注册passkey

管理接口用户管理

🔐 需要登录（User权限）

loading...

POST

/`api`/`user`/`passkey`/`register`/`begin`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/passkey/register/begin"
```

200

Empty

---

完成注册passkey

管理接口用户管理

🔐 需要登录（User权限）

loading...

POST

/`api`/`user`/`passkey`/`register`/`finish`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/passkey/register/finish"
```

200

Empty

---

开始验证passkey

管理接口用户管理

🔐 需要登录（User权限）

loading...

POST

/`api`/`user`/`passkey`/`verify`/`begin`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/passkey/verify/begin"
```

200

Empty

---

完成验证passkey

管理接口用户管理

🔐 需要登录（User权限）

loading...

POST

/`api`/`user`/`passkey`/`verify`/`finish`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/passkey/verify/finish"
```

200

Empty

---

创建用户

管理接口用户管理

👨💼 需要管理员权限（Admin）

loading...

POST

/`api`/`user`/

Send

Body

Request Body

application/json

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

更新用户

管理接口用户管理

👨💼 需要管理员权限（Admin）

loading...

PUT

/`api`/`user`/

Send

Body

Request Body

application/json

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X PUT "https://loading/api/user/" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

搜索用户

管理接口用户管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`user`/`search`

Send

Query

Query Parameters

keyword?string

group?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/user/search"
```

200

Empty

---

注销当前用户

管理接口用户管理

🔐 需要登录（User权限）

loading...

DELETE

/`api`/`user`/`self`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X DELETE "https://loading/api/user/self"
```

200

Empty

---

获取当前用户信息

管理接口用户管理

🔐 需要登录（User权限）

loading...

GET

/`api`/`user`/`self`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/user/self"
```

200

Empty

---

获取当前用户分组

管理接口用户管理

🔐 需要登录（User权限）

loading...

GET

/`api`/`user`/`self`/`groups`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/user/self/groups"
```

200

Empty

---

更新当前用户信息

管理接口用户管理

🔐 需要登录（User权限）

loading...

PUT

/`api`/`user`/`self`

Send

Body

Request Body

application/json

username?string

display\_name?string

password?string

original\_password?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X PUT "https://loading/api/user/self" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

更新用户设置

管理接口用户管理

🔐 需要登录（User权限）

loading...

PUT

/`api`/`user`/`setting`

Send

Body

Request Body

application/json

notify\_type?string

quota\_warning\_threshold?number

webhook\_url?string

notification\_email?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X PUT "https://loading/api/user/setting" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

---

生成访问令牌

管理接口用户管理

🔐 需要登录（User权限）

loading...

GET

/`api`/`user`/`token`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/user/token"
```

200

Empty

---

管理员完成充值

管理接口用户管理

👨💼 需要管理员权限（Admin）

loading...

POST

/`api`/`user`/`topup`/`complete`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/topup/complete"
```

200

Empty

---

获取所有充值记录

管理接口用户管理

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`user`/`topup`

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/user/topup"
```

200

Empty

---


### vendors


获取所有供应商

管理接口供应商

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`vendors`/

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/vendors/"
```

200

Empty

---

删除供应商

管理接口供应商

👨💼 需要管理员权限（Admin）

loading...

DELETE

/`api`/`vendors`/`{id}`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X DELETE "https://loading/api/vendors/0"
```

200

Empty

---

获取指定供应商

管理接口供应商

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`vendors`/`{id}`

Send

Path

Path Parameters

id\*integer

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/vendors/0"
```

200

Empty

---

创建供应商

管理接口供应商

👨💼 需要管理员权限（Admin）

loading...

POST

/`api`/`vendors`/

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/vendors/"
```

200

Empty

---

更新供应商

管理接口供应商

👨💼 需要管理员权限（Admin）

loading...

PUT

/`api`/`vendors`/

Send

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X PUT "https://loading/api/vendors/"
```

200

Empty

---

搜索供应商

管理接口供应商

👨💼 需要管理员权限（Admin）

loading...

GET

/`api`/`vendors`/`search`

Send

Query

Query Parameters

keyword?string

Response Body

200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/api/vendors/search"
```

200

Empty

---
