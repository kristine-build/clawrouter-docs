# 音訊轉錄

将音訊转换为文本

## Endpoint

**POST** `/v1/audio/transcriptions`..

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | ```http Authorization: Bearer <API_KEY> ```.. |
## Request Body
`multipart/form-data`..
| name | type | required | description |
|---|---|---|---|
| file | string (binary) | yes | 音訊檔案。 |
| model | string | yes | 模型名称，例如 `whisper-1`..。 |
| language | string | no | ISO-639-1 语言代码。 |
| prompt | string | no | 提示词。 |
| response_format | string | no | 取值 `json`.. / `text`.. / `srt`.. / `verbose_json`.. / `vtt`..。預設 `json`..。 |
| temperature | number | no | 温度參數。 |
| timestamp_granularities[] | array<string> | no | 时间戳粒度控制。 |

## Response Body

### 200

```json
{
  "text": "string"
}
```..
## Code Examples

### cURL

```bash
curl -X POST "https://docs.newapi.pro/v1/audio/transcriptions" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -F "text=string"
```..

### JavaScript

```javascript
const formData = new FormData();
formData.append("text", "string");
const response = await fetch("https://docs.newapi.pro/v1/audio/transcriptions", {
  method: "POST",
  headers: {
    "Authorization": "Bearer YOUR_API_KEY"
  },
  body: formData
});
const text = await response.text();
console.log(text);
```..

### Go

```go
package main

	"bytes"
	"io"
	"mime/multipart"
	"net/http"
	"os"
)

func main() {
	var buf bytes.Buffer
	writer := multipart.NewWriter(&buf)
	_ = writer.WriteField("model", "whisper-1")
	file, _ := os.Open("audio.mp3")
	defer file.Close()
	part, _ := writer.CreateFormFile("file", "audio.mp3")
	_, _ = io.Copy(part, file)
	_ = writer.Close()
	req, _ := http.NewRequest("POST", "https://docs.newapi.pro/v1/audio/transcriptions", &buf)
	req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
	req.Header.Set("Content-Type", writer.FormDataContentType())
	http.DefaultClient.Do(req)
}
```..

### Python

```python
url = "https://docs.newapi.pro/v1/audio/transcriptions"
headers = {"Authorization": "Bearer YOUR_API_KEY"}
files = {}
data = {}
data["text"] = "string"
resp = requests.post(url, headers=headers, files=files, data=data, timeout=30)
print(resp.status_code)
print(resp.text)
```..

### Java

```java
HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://docs.newapi.pro/v1/audio/transcriptions"))
    .header("Authorization", "Bearer YOUR_API_KEY")
    .POST(HttpRequest.BodyPublishers.noBody())
    .build();
HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.statusCode());
System.out.println(response.body());
```..

### C#

```csharp
var client = new HttpClient();
client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", "YOUR_API_KEY");
var form = new MultipartFormDataContent();
	form.Add(new StringContent("whisper-1"), "model");
	form.Add(new ByteArrayContent(File.ReadAllBytes("audio.mp3")), "file", "audio.mp3");
var request = new HttpRequestMessage(HttpMethod.Post, "https://docs.newapi.pro/v1/audio/transcriptions") {
	Content = form
};
var response = await client.SendAsync(request);
Console.WriteLine((int)response.StatusCode);
Console.WriteLine(await response.Content.ReadAsStringAsync());
```..
