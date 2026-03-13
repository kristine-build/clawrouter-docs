# Gemini媒体识别

Gemini影像、PDF、音频、影片识别請求

⚠️注意：仅支援透過 inlineData 以 base64 方式上傳影像、PDF、音频、影片，不支援 fileData.fileUri 或 File API。

## Endpoint

`POST /v1beta/models/{model}:generateContent`

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | \| --- \| --- \| --- \| --- \| \| `Authorization` \| `string` \| yes \| Bearer API key。範例：`Authorization: Bearer YOUR_API_KEY` \| |
## Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `model` | `string` | yes | 模型名称，例如 `gemini-2.5-pro-vision` |

## Request Body
Content-Type: `application/json`
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `contents` | `array` | yes | 输入內容清單 |
| `contents[].parts` | `array` | yes | 每个输入片段清單 |
| `contents[].parts[].text` | `string` | no | 文本內容片段 |
| `contents[].parts[].inlineData` | `object` | no | base64 媒体內容 |
| `contents[].parts[].inlineData.mimeType` | `string` | yes | 媒体 MIME 类型 |
| `contents[].parts[].inlineData.data` | `string` | yes | base64 编码的資料 |
| `generationConfig` | `object` | no | 生成控制參數 |
| `generationConfig.responseModalities` | `array` | no | 期望回傳模态 |

## Response Body

### 200 application/json

```json
{
  "candidates": [
    {
      "content": {
        "role": "model",
        "parts": [
          {
            "inlineData": {
              "mimeType": "audio/wav",
              "data": "BASE64_AUDIO_DATA"
            }
          }
        ]
      },
      "finishReason": "STOP"
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 12,
    "candidatesTokenCount": 58,
    "totalTokenCount": 70
  }
}
```
## Error Example

```json
{
  "error": {
    "code": 400,
    "message": "Invalid request"
  }
}
```

## Code Examples

### cURL

```bash
curl -X POST "https://docs.newapi.pro/v1beta/models/gemini-2.5-pro-vision:generateContent" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "image/jpeg",
              "data": "iVBORw0KGgoAAAANSUhEUgAAAAUA"
            }
          }
        ]
      }
    ]
  }'
```

### JavaScript

```javascript
const response = await fetch("https://docs.newapi.pro/v1beta/models/gemini-2.5-pro-vision:generateContent", {
  method: "POST",
  headers: {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    contents: [
      {
        parts: [
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "iVBORw0KGgoAAAANSUhEUgAAAAUA"
            }
          }
        ]
      }
    ]
  })
});
console.log(await response.status);
console.log(await response.text());
```

### Go

```go
func main() {
	payloadJSON := `{"contents":[{"parts":[{"inlineData":{"mimeType":"image/jpeg","data":"iVBORw0KGgoAAAANSUhEUgAAAAUA"}}]}]}`
	var payload map[string]interface{}
	_ = jsonutil.Unmarshal([]byte(payloadJSON), &payload)
	data, _ := jsonutil.Marshal(payload)
	req, _ := http.NewRequest("POST", "https://docs.newapi.pro/v1beta/models/gemini-2.5-pro-vision:generateContent", bytesutil.NewReader(data))
	req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
	req.Header.Set("Content-Type", "application/json")
	http.DefaultClient.Do(req)
}
```

### Python

```python
url = "https://docs.newapi.pro/v1beta/models/gemini-2.5-pro-vision:generateContent"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json",
}
payload = {
    "contents": [
        {
            "parts": [
                {
                    "inlineData": {
                        "mimeType": "image/jpeg",
                        "data": "iVBORw0KGgoAAAANSUhEUgAAAAUA"
                    }
                }
            ]
        }
    ]
}
resp = requests.request("POST", url, headers=headers, json=payload, timeout=30)
print(resp.status_code)
print(resp.text)
```

### Java

```java
var client = HttpClient.newHttpClient();
String json = "{\"contents\":[{\"parts\":[{\"inlineData\":{\"mimeType\":\"image/jpeg\",\"data\":\"iVBORw0KGgoAAAANSUhEUgAAAAUA\"}}]]}";
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://docs.newapi.pro/v1beta/models/gemini-2.5-pro-vision:generateContent"))
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
client.DefaultRequestHeaders.Authorization =
    new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", "YOUR_API_KEY");
var payload = new StringContent(@"{""contents"":[{""parts"":[{""inlineData"":{""mimeType"":""image/jpeg"",""data"":""iVBORw0KGgoAAAANSUhEUgAAAAUA""}}]}]}", Encoding.UTF8, "application/json");
var request = new HttpRequestMessage(HttpMethod.Post, "https://docs.newapi.pro/v1beta/models/gemini-2.5-pro-vision:generateContent") {
    Content = payload
};
var response = await client.SendAsync(request);
Console.WriteLine((int)response.StatusCode);
Console.WriteLine(await response.Content.ReadAsStringAsync());
```
