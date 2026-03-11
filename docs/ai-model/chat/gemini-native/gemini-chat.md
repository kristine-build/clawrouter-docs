# Gemini文本聊天

AI 模型接口嵌入（Embeddings）

# 原生Gemini格式

使用指定引擎/模型创建嵌入



/`v1`/`engines`/`{model}`/`embeddings`


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

模型/引擎 ID

## [Request Body](#request-body)

application/json

model\*string

input\*string|array<string>

要嵌入的文本

encoding\_format?string

Default`"float"`

Value in`"float" | "base64"`

dimensions?integer

输出向量维度

## [Response Body](#response-body)

### 200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://docs.newapi.pro/v1/engines/string/embeddings" \  -H "Content-Type: application/json" \  -d '{    "model": "text-embedding-ada-002",    "input": "string"  }'
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
