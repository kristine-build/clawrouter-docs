# Responses格式

AI 模型介面聊天（Chat）原生OpenAI格式

# Responses格式

OpenAI Responses API，用于建立模型回應。
支援多轮對話、工具調用、推理等功能。



## Endpoint

/v1/responses
Authorization

Body

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | AuthorizationBearer <token> 使用 Bearer Token 认证。 格式: `Authorization: Bearer sk-xxxxxx` In: `header` |
## Request Body
application/json

| Name | Type | Required | Description |
|---|---|---|---|
| model | string | yes |  |
| input | string\|array<object> | no | 输入內容，可以是字符串或消息数组 |
| instructions | string | no |  |
| max_output_tokens | integer | no |  |
| temperature | number | no |  |
| top_p | number | no |  |
| stream | boolean | no |  |
| tools | array<object> | no |  |
| tool_choice | string\|object | no |  |
| reasoning | object | no |  |
| previous_response_id | string | no |  |
| truncation | string | no | Value in`"auto" \| "disabled"` |
## Response Body

### 200 application/json



```
curl -X POST "https://docs.newapi.pro/v1/responses" \  -H "Content-Type: application/json" \  -d '{    "model": "string"  }'
```

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
## Code Examples

### cURL

```bash
curl -X POST "https://docs.newapi.pro/v1/responses" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{   "model": "tts-1",   "input": "请用中文朗读今天的新闻摘要" }'
```

### JavaScript

```javascript
const payload = {
  "model": "tts-1",
  "input": "请用中文朗读今天的新闻摘要"
};
const response = await fetch("https://docs.newapi.pro/v1/responses", {
  method: "POST",
  headers: {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
  },
  body: JSON.stringify(payload),
});
console.log(await response.text());
```

### Go

```go
package main

	"bytes"
	"encoding/json"
	"net/http"
)

func main() {
	payloadJSON := `{  "model": "tts-1",  "input": "请用中文朗读今天的新闻摘要"}`
	var payload map[string]interface{}
	_ = json.Unmarshal([]byte(payloadJSON), &payload)
	data, _ := json.Marshal(payload)
	req, _ := http.NewRequest("POST", "https://docs.newapi.pro/v1/responses", bytes.NewReader(data))
	req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
	req.Header.Set("Content-Type", "application/json")
	http.DefaultClient.Do(req)
}
```

### Python

```python
url = "https://docs.newapi.pro/v1/responses"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json",
}
payload = {
  "model": "tts-1",
  "input": "请用中文朗读今天的新闻摘要"
}
resp = requests.request("POST", url, headers=headers, json=payload, timeout=30)
print(resp.status_code)
print(resp.text)
```

### Java

```java
HttpClient client = HttpClient.newHttpClient();
    String json = "{  \"model\": \"tts-1\",  \"input\": \"请用中文朗读今天的新闻摘要\"}";
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://docs.newapi.pro/v1/responses"))
    .header("Authorization", "Bearer YOUR_API_KEY")
    .header("Content-Type", "application/json")
    .POST(HttpRequest.BodyPublishers.ofString(json))
    .build();
HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.statusCode());
System.out.println(response.body());
```

### C#

```csharp
var client = new HttpClient();
client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", "YOUR_API_KEY");
var payload = new StringContent(@"{  ""model"": ""tts-1"",  ""input"": ""请用中文朗读今天的新闻摘要""}", Encoding.UTF8, "application/json");
var request = new HttpRequestMessage(HttpMethod.Post, "https://docs.newapi.pro/v1/responses") {
	Content = payload
};
var response = await client.SendAsync(request);
Console.WriteLine((int)response.StatusCode);
Console.WriteLine(await response.Content.ReadAsStringAsync());
```
