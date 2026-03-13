# 原生OpenAI格式

将文本转换为向量嵌入

## Endpoint

POST `/v1/embeddings`..

## Authorization

BearerAuth

Authorization: Bearer <token>

使用 Bearer Token 驗證。 格式: Authorization: Bearer sk-xxxxxx

In: header

## Request Body

| Name | Type | Required | Description |
|---|---|---|---|
| model | string | yes |  |
| input | string \| array<string> | yes | 要嵌入的文本 |
| encoding_format | string | no | Default "float" Value in "float" \| "base64" |
| dimensions | integer | no | 输出向量维度 |

## Example Request

```bash
curl -X POST "https://docs.newapi.pro/v1/embeddings" \
  -H "Authorization: Bearer " \
  -H "Content-Type: application/json" \
  -d '{
    "model": "text-embedding-ada-002",
    "input": "string"
  }'
```..

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
```..

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
```..
