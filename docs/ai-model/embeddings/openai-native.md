# 原生OpenAI格式

将文本转换为向量嵌入

## Endpoint

`POST /v1/embeddings`

## Authorization

| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | 使用 Bearer Token 认证。格式: `Authorization: Bearer sk-xxxxxx`。在请求头中通过 `Authorization` 传递。 |

## Request Body

| Name | Type | Required | Description |
|---|---|---|---|
| model | string | yes | 模型标识。 |
| input | string \| array<string> | yes | 要嵌入的文本。 |
| encoding_format | string | no | 输出向量格式，默认值：`"float"`。可选值：`"float"`、`"base64"`。 |
| dimensions | integer | no | 输出向量维度。 |

## Response Body

### 200 application/json

| Name | Type | Description |
|---|---|---|
| object | string | 响应对象类型，值通常为 `list`。 |
| data | array<object> | 嵌入结果列表。 |
| data[0].object | string | 单项对象类型，通常为 `embedding`。 |
| data[0].index | integer | 与输入顺序对应的索引。 |
| data[0].embedding | array<number> | 向量数值列表。 |
| model | string | 使用的模型。 |
| usage | object | 用量统计。 |
| usage.prompt_tokens | integer | 输入 token 数。 |
| usage.total_tokens | integer | 总 token 数。 |

## Example Request

### cURL

```bash
curl -X POST "https://docs.newapi.pro/v1/embeddings" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "text-embedding-ada-002",
    "input": "将文本转换为向量嵌入"
  }'
```

### JavaScript

```javascript
fetch("https://docs.newapi.pro/v1/embeddings", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY"
  },
  body: JSON.stringify({
    model: "text-embedding-ada-002",
    input: "将文本转换为向量嵌入"
  })
});
```

### Go

```go
package main

import (
  "bytes"
  "net/http"
)

func main() {
  body := bytes.NewBuffer([]byte(`{
    "model": "text-embedding-ada-002",
    "input": "将文本转换为向量嵌入"
  }`))

  req, _ := http.NewRequest("POST", "https://docs.newapi.pro/v1/embeddings", body)
  req.Header.Set("Content-Type", "application/json")
  req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
  http.DefaultClient.Do(req)
}
```

### Python

```python
import requests

url = "https://docs.newapi.pro/v1/embeddings"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY",
}
payload = {
    "model": "text-embedding-ada-002",
    "input": "将文本转换为向量嵌入"
}

response = requests.request("POST", url, headers=headers, json=payload)
print(response.json())
```

### Java

```java
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://docs.newapi.pro/v1/embeddings"))
    .header("Content-Type", "application/json")
    .header("Authorization", "Bearer YOUR_API_KEY")
    .POST(HttpRequest.BodyPublishers.ofString("""
      {
        "model": "text-embedding-ada-002",
        "input": "将文本转换为向量嵌入"
      }
      """))
    .build();
```

### C#

```csharp
var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Post, "https://docs.newapi.pro/v1/embeddings");
request.Headers.Add("Content-Type", "application/json");
request.Headers.Add("Authorization", "Bearer YOUR_API_KEY");
request.Content = new StringContent(@"{
  \"model\": \"text-embedding-ada-002\",
  \"input\": \"将文本转换为向量嵌入\"
}", Encoding.UTF8, "application/json");

await client.SendAsync(request);
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

## Maintainer Note

该页面当前为纯 Markdown 重建。建议下一步改为 GitBook 的 OpenAPI 引用/渲染块，以便直接从规范生成完整参数、示例与错误响应。
- 接口：`POST /v1/embeddings`
- OpenAPI 规格文件：`openapi/generated/ai-model/嵌入（Embeddings）/post-v1-embeddings-createembedding-383826477.json`
