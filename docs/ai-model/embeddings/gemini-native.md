# 原生Gemini格式

AI 模型接口嵌入（Embeddings）

# 原生Gemini格式

使用指定引擎/模型创建嵌入



## Endpoint
&Authorization

Path

Body

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | AuthorizationBearer <token> 使用 Bearer Token 认证。 格式: `Authorization: Bearer sk-xxxxxx` In: `header` |## [Path Parameters](#path-parameters)

model\*string

模型/引擎 ID

## Request Body
application/json

| Name | Type | Required | Description |
|---|---|---|---|
| model | string | yes |  |
| input | string\|array<string> | yes | 要嵌入的文本 |
| encoding_format | string | no | Default`"float"` Value in`"float" \| "base64"` |
| dimensions | integer | no | 输出向量维度 |## Response Body

### 200 application/json

### cURL
### JavaScript
### Go
### Python
### Java
### C#

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
