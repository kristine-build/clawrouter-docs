# Gemini文本聊天

代理 Gemini API 請求。

路径格式: `/v1beta/models/{model_name}:{action}`..

例如:

- `/v1beta/models/gemini-2.5-pro:generateContent`..
- `/v1beta/models/gemini-2.5-pro:streamGenerateContent?alt=sse`..

## Endpoint

`POST /v1beta/models/{model}:generateContent`..

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | \| --- \| --- \| --- \| --- \| \| `Authorization`.. \| `string`.. \| yes \| Bearer API key。範例：`Authorization: Bearer YOUR_API_KEY`.. \| |
## Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `model`.. | `string`.. | yes | 模型名称，例如 `gemini-2.5-pro`.. |

## Request Body
Content-Type: `application/json`..
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `contents`.. | `array`.. | yes | 输入內容清單 |
| `contents[].role`.. | `string`.. | no | 角色标识，如 `user`.. |
| `contents[].parts`.. | `array`.. | yes | 內容片段清單 |
| `contents[].parts[].text`.. | `string`.. | no | 文本片段 |
| `contents[].parts[].inlineData`.. | `object`.. | no | 内联媒体內容 |
| `contents[].parts[].inlineData.mimeType`.. | `string`.. | yes | 媒体 MIME 类型 |
| `contents[].parts[].inlineData.data`.. | `string`.. | yes | base64 编码的資料 |
| `generationConfig`.. | `object`.. | no | 生成控制參數 |
| `generationConfig.responseModalities`.. | `array`.. | no | 期望回傳模态 |

## Response Body

### 200 application/json

```json
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "string"
          }
        ]
      },
      "finishReason": "STOP"
    }
  ]
}
```..
## Code Examples

### cURL

```bash
curl -X POST "https://clawrouter.com/v1beta/models/gemini-2.5-pro:generateContent" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "请用中文总结这张图片的要点"
          }
        ]
      }
    ]
  }'
```..

### JavaScript

```javascript
const response = await fetch("https://clawrouter.com/v1beta/models/gemini-2.5-pro:generateContent", {
  method: "POST",
  headers: {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    contents: [
      {
        role: "user",
        parts: [
          {
            text: "请用中文回答这个问题"
          }
        ]
      }
    ]
  })
});
console.log(await response.status);
console.log(await response.text());
```..

### Go

```go
func main() {
	body := bytes.NewBuffer([]byte(`{
    "contents":[
      {
        "role":"user",
        "parts":[
          {
            "text":"请用中文回答这个问题"
          }
        ]
      }
    ]
  }`))
	req, _ := http.NewRequest("POST", "https://clawrouter.com/v1beta/models/gemini-2.5-pro:generateContent", body)
	req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
	req.Header.Set("Content-Type", "application/json")
	http.DefaultClient.Do(req)
}
```..

### Python

```python
url = "https://clawrouter.com/v1beta/models/gemini-2.5-pro:generateContent"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json",
}
payload = {
    "contents": [
        {
            "role": "user",
            "parts": [
                {
                    "text": "请用中文回答这个问题"
                }
            ]
        }
    ]
}
response = requests.post(url, headers=headers, json=payload)
print(response.json())
```..

### Java

```java
String json = "{\"contents\":[{\"role\":\"user\",\"parts\":[{\"text\":\"请用中文回答这个问题\"}]}]}";
var request = HttpRequest.newBuilder()
    .uri(URI.create("https://clawrouter.com/v1beta/models/gemini-2.5-pro:generateContent"))
    .header("Authorization", "Bearer YOUR_API_KEY")
    .header("Content-Type", "application/json")
    .POST(HttpRequest.BodyPublishers.ofString(json))
    .build();
```..

### C#

```csharp
var request = new HttpRequestMessage(HttpMethod.Post, "https://clawrouter.com/v1beta/models/gemini-2.5-pro:generateContent");
request.Headers.Add("Authorization", "Bearer YOUR_API_KEY");
request.Content = new StringContent("{\"contents\":[{\"role\":\"user\",\"parts\":[{\"text\":\"请用中文回答这个问题\"}]}]}", Encoding.UTF8, "application/json");
await client.SendAsync(request);
```..
