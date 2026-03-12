# 原生OpenAI格式

## Code Examples

### cURL

```bash
curl -X POST "https://docs.newapi.pro/" \
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
const response = await fetch("https://docs.newapi.pro/", {
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
	req, _ := http.NewRequest("POST", "https://docs.newapi.pro/", bytes.NewReader(data))
	req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
	req.Header.Set("Content-Type", "application/json")
	http.DefaultClient.Do(req)
}
```

### Python

```python
url = "https://docs.newapi.pro/"
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
    .uri(URI.create("https://docs.newapi.pro/"))
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
var request = new HttpRequestMessage(HttpMethod.Post, "https://docs.newapi.pro/") {
	Content = payload
};
var response = await client.SendAsync(request);
Console.WriteLine((int)response.StatusCode);
Console.WriteLine(await response.Content.ReadAsStringAsync());
```
