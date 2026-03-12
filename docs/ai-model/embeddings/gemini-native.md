# 原生Gemini格式

使用指定引擎/模型创建嵌入

## Endpoint

POST `/v1/engines/{model}/embeddings`

## Authorization

Bearer Token 认证。

Header 示例：

Authorization: Bearer sk-xxxxxx

## Path Parameters

### model

string

模型/引擎 ID。

## Request Body

| Name | Type | Required | Description |
|---|---|---|---|
| model | string | yes | 使用的模型/引擎 ID。 |
| input | string \| array<string> | yes | 需要生成嵌入向量的文本。 |
| encoding_format | string | no | 返回向量的编码格式。默认值：`float`。可选值：`float`、`base64`。 |
| dimensions | integer | no | 输出向量的维度。 |

## Response Body

### 200 application/json

```json
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

## Example Request

```bash
curl -X POST "https://docs.newapi.pro/v1/engines/text-embedding-ada-002/embeddings" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "text-embedding-ada-002",
    "input": "string"
  }'
```

## Example Response

```json
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
