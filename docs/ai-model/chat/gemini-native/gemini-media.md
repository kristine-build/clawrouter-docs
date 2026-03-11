# Gemini媒体识别

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


## Code Examples

### cURL

```bash
curl -X POST "https://docs.newapi.pro/v1/engines/" \
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
const response = await fetch("https://docs.newapi.pro/v1/engines/", {
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
	req, _ := http.NewRequest("POST", "https://docs.newapi.pro/v1/engines/", bytes.NewReader(data))
	req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
	req.Header.Set("Content-Type", "application/json")
	http.DefaultClient.Do(req)
}
```

### Python

```python
url = "https://docs.newapi.pro/v1/engines/"
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
    .uri(URI.create("https://docs.newapi.pro/v1/engines/"))
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
var request = new HttpRequestMessage(HttpMethod.Post, "https://docs.newapi.pro/v1/engines/") {
	Content = payload
};
var response = await client.SendAsync(request);
Console.WriteLine((int)response.StatusCode);
Console.WriteLine(await response.Content.ReadAsStringAsync());
```
