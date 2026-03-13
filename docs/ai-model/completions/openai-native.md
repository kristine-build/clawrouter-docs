# 原生OpenAI格式

基于给定提示建立文本补全

## 請求概览

`POST /v1/completions`

- **Authorization**：BearerAuth
- **Content-Type**：application/json

## Authorization

| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | Bearer Token 认证。格式：`Authorization: Bearer sk-xxxxxx`。通过 `Authorization` 請求头传递，範例：`Authorization: Bearer YOUR_API_KEY`。 |

## Request Body

| Name | Type | Required | Description |
|---|---|---|---|
| model | string | yes | 该介面使用的模型 ID。 |
| prompt | string \| array<string> | yes | 输入提示词。 |
| max_tokens | integer | no | 可生成的最大 token 数。 |
| temperature | number | no | 采样温度。范围通常为 `0` 到 `2`。 |
| top_p | number | no | 使用核采样（Top-p）策略时的概率阈值，范围通常为 `0` 到 `1`。 |
| n | integer | no | 每个提示词回傳的候选数目。 |
| stream | boolean | no | 是否启用流式回傳。 |
| stop | string \| array<string> | no | 停止生成的词元。 |
| suffix | string | no | 在补全结果后追加的后缀。 |
| echo | boolean | no | 是否在回傳文本中回显输入提示词。 |
| best_of | integer | no | 在未开启流式时，服务端会并行采样并回傳 `n` 个中评分最高的一个。 |
| frequency_penalty | number | no | 频率惩罚值，用于抑制重复。 |
| presence_penalty | number | no | 存在惩罚值，用于提高新话题概率。 |
| logit_bias | object | no | 词表偏置映射，键为 token，值为偏置分数。 |
| logprobs | integer | no | 在输出中回傳每个 token 的对数概率个数。 |
| seed | integer | no | 生成随机种子。 |
| user | string | no | 终端使用者标识符，用于审计与风控。 |

## Response Body

### 200 application/json

| Name | Type | Description |
|---|---|---|
| id | string | 回應 ID。 |
| object | string | 回應对象类型，範例值 `text_completion`。 |
| created | integer | 回應建立时间戳（Unix 秒）。 |
| model | string | 使用的模型。 |
| choices | array<object> | 生成候选文本清單。 |
| choices[0].text | string | 本次生成文本。 |
| choices[0].index | integer | 该候选在清單中的索引。 |
| choices[0].finish_reason | string | 生成结束原因。 |
| usage | object | 用量统计。 |
| usage.prompt_tokens | integer | 输入 token 数。 |
| usage.completion_tokens | integer | 输出 token 数。 |
| usage.total_tokens | integer | 总 token 数。 |
| usage.prompt_tokens_details | object | 输入 tokens 细分。 |
| usage.prompt_tokens_details.cached_tokens | integer | 缓存命中的 token 数。 |
| usage.prompt_tokens_details.text_tokens | integer | 文本输入 token 数。 |
| usage.prompt_tokens_details.audio_tokens | integer | 音频输入 token 数。 |
| usage.prompt_tokens_details.image_tokens | integer | 图片 token 数。 |
| usage.completion_tokens_details | object | 输出 tokens 细分。 |
| usage.completion_tokens_details.text_tokens | integer | 文本输出 token 数。 |
| usage.completion_tokens_details.audio_tokens | integer | 音频输出 token 数。 |
| usage.completion_tokens_details.reasoning_tokens | integer | 推理 token 数。 |

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
func main() {
  body := bytes.NewBuffer([]byte(`{
    "model": "gpt-3.5-turbo-instruct",
    "prompt": "Write a short poem about the moon."
  }`))

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

response = requests.request("POST", url, headers=headers, json=payload)
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
request.Content = new StringContent(@"""
{
  "model": "gpt-3.5-turbo-instruct",
  "prompt": "Write a short poem about the moon."
}
""", Encoding.UTF8, "application/json");

await client.sendAsync(request);
```

### 200 Response Example

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

## Error Example

```json
{
  "error": {
    "message": "Invalid request",
    "type": "invalid_request_error",
    "code": "invalid_request_error"
  }
}
```
