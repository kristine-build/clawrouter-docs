# 音频翻译

AI 模型接口音频（Audio）原生OpenAI格式

# 音频翻译

将音频翻译为英文文本



/`v1`/`audio`/`translations`


Authorization

Body

## [Authorization](#authorization)

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

## [Request Body](#request-body)

multipart/form-data

file\*file

Format`binary`

model\*string

prompt?string

response\_format?string

temperature?number

## [Response Body](#response-body)

### 200 application/json



```
curl -X POST "https://docs.newapi.pro/v1/audio/translations" \  -F file="string" \  -F model="string"
```

200

```
{
  "text": "string"
}
```





## Code Examples

### cURL

```bash
curl -X POST "https://docs.newapi.pro/v1/audio/translations" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -F "file=@/path/to/audio.mp3" \
  -F "model=whisper-1"
```

### JavaScript

```javascript
const formData = new FormData();
formData.append("file", fileInput.files[0]);
formData.append("model", "whisper-1");
const response = await fetch("https://docs.newapi.pro/v1/audio/translations", {
  method: "POST",
  headers: {
    "Authorization": "Bearer YOUR_API_KEY"
  },
  body: formData
});
const text = await response.text();
console.log(text);
```

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
	req, _ := http.NewRequest("POST", "https://docs.newapi.pro/v1/audio/translations", &buf)
	req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
	req.Header.Set("Content-Type", writer.FormDataContentType())
	http.DefaultClient.Do(req)
}
```

### Python

```python
url = "https://docs.newapi.pro/v1/audio/translations"
headers = {"Authorization": "Bearer YOUR_API_KEY"}
files = {}
data = {}
files["file"] = open("/path/to/audio.mp3", "rb")
data["model"] = "whisper-1"
resp = requests.post(url, headers=headers, files=files, data=data, timeout=30)
print(resp.status_code)
print(resp.text)
```

### Java

```java
HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://docs.newapi.pro/v1/audio/translations"))
    .header("Authorization", "Bearer YOUR_API_KEY")
    .POST(HttpRequest.BodyPublishers.noBody())
    .build();
HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.statusCode());
System.out.println(response.body());
```

### C#

```csharp
var client = new HttpClient();
client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", "YOUR_API_KEY");
var form = new MultipartFormDataContent();
	form.Add(new StringContent("whisper-1"), "model");
	form.Add(new ByteArrayContent(File.ReadAllBytes("audio.mp3")), "file", "audio.mp3");
var request = new HttpRequestMessage(HttpMethod.Post, "https://docs.newapi.pro/v1/audio/translations") {
	Content = form
};
var response = await client.SendAsync(request);
Console.WriteLine((int)response.StatusCode);
Console.WriteLine(await response.Content.ReadAsStringAsync());
```
