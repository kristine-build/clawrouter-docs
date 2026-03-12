# 原生Gemini格式

使用指定引擎/模型创建嵌入

POST `/v1/engines/{model}/embeddings`

## Authorization

使用 Bearer Token 进行身份验证。

Header 示例：

`Authorization: Bearer sk-xxxxxx`

## Path Parameters

### model

string

要使用的模型名称。

## Request Body

| Name | Type | Required | Description |
|---|---|---|---|
| input | string \| array<string> | yes | 需要生成嵌入向量的文本。 |
| encoding_format | string | no | 返回向量的编码格式。默认值：`float`。可选值：`float`、`base64`。 |
| dimensions | integer | no | 输出向量的维度。 |

## Response

成功返回：

### 200 application/json

```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [0]
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
curl -X POST "https://api.example.com/v1/engines/text-embedding-ada-002/embeddings" \
  -H "Authorization: Bearer sk-xxxxxx" \
  -H "Content-Type: application/json" \
  -d '{
    "input": "Hello world"
  }'
```
