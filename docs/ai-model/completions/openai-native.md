# 原生OpenAI格式

基于给定提示创建文本补全

## Endpoint

`POST /v1/completions`

## Authorization

| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | 使用 Bearer Token 认证。格式: `Authorization: Bearer <YOUR_API_KEY>`，位置: `header` |

## Request Body

| Name | Type | Required | Description |
|---|---|---|---|
| model | string | yes | 要使用的模型 ID。 |
| prompt | `string \| array<string>` | yes | 提示词。可为单条字符串或字符串数组。 |
| max_tokens | integer | no | 最大输出 token 数。 |
| temperature | number | no | 采样温度。 |
| top_p | number | no | 采样概率阈值。 |
| n | integer | no | 每个 prompt 返回的补全候选数。 |
| stream | boolean | no | 是否启用流式响应。 |
| stop | `string \| array<string>` | no | 停止生成的词元。 |
| suffix | string | no | 补全生成内容后缀。 |
| echo | boolean | no | 返回结果中是否包含输入提示词。 |

## Code Examples

### cURL

```bash
curl -X POST "https://docs.newapi.pro/v1/completions" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-3.5-turbo-instruct",
    "prompt": "Write a short poem about the moon."
  }'
```

### JavaScript

```javascript
fetch("https://docs.newapi.pro/v1/completions", {
  method: "POST",
  headers: {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "gpt-3.5-turbo-instruct",
    prompt: "Write a short poem about the moon."
  })
});
```

### Go

```go
package main

func main() {
  body := []byte(`{
    "model": "gpt-3.5-turbo-instruct",
    "prompt": "Write a short poem about the moon."
  }`)

  req, _ := http.NewRequest("POST", "https://docs.newapi.pro/v1/completions", body)
  req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
  req.Header.Set("Content-Type", "application/json")
  http.DefaultClient.Do(req)
}
```

### Python

```python
url = "https://docs.newapi.pro/v1/completions"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json",
}
payload = {
    "model": "gpt-3.5-turbo-instruct",
    "prompt": "Write a short poem about the moon."
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Java

```java
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://docs.newapi.pro/v1/completions"))
    .header("Authorization", "Bearer YOUR_API_KEY")
    .header("Content-Type", "application/json")
    .POST(HttpRequest.BodyPublishers.ofString("""
      {
        "model":"gpt-3.5-turbo-instruct",
        "prompt":"Write a short poem about the moon."
      }
      """))
    .build();
```

### C#

```csharp
var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Post, "https://docs.newapi.pro/v1/completions");
request.Headers.Add("Authorization", "Bearer YOUR_API_KEY");
request.Content = new StringContent("""
{
  "model": "gpt-3.5-turbo-instruct",
  "prompt": "Write a short poem about the moon."
}
""", Encoding.UTF8, "application/json");

await client.PostAsync(request.RequestUri, request.Content);
```

Response Body
200 application/json

```json
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
    "total_tokens": 0
  }
}
```
