# 原生Gemini格式

使用指定引擎/模型创建嵌入

## Endpoint

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
| encoding_format | string | no | 返回向量的编码格式。可选值：`float`、`base64`。默认值：`float`。 |
| dimensions | integer | no | 输出向量的维度。 |

## Response Body

### 200 application/json

| Name | Type | Description |
|---|---|---|
| object | string | 响应对象类型，通常为 `list`。 |
| data | array<object> | 嵌入结果列表。 |
| data[0].object | string | 列表项类型，通常为 `embedding`。 |
| data[0].index | integer | 与输入对应的序号。 |
| data[0].embedding | array<number> | 生成的向量。
| model | string | 使用的模型标识（按请求中的 `model`）。 |
| usage | object | 用量信息。 |
| usage.prompt_tokens | integer | 输入 token 数。 |
| usage.total_tokens | integer | 总 token 数。 |

## Example Request

```bash
curl -X POST "https://api.example.com/v1/engines/text-embedding-ada-002/embeddings" \
  -H "Authorization: Bearer sk-xxxxxx" \
  -H "Content-Type: application/json" \
  -d '{
    "input": "Hello world"
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
