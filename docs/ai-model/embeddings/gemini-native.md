# 原生Gemini格式

使用指定引擎/模型创建嵌入

## Endpoint

POST `/v1/engines/{model}/embeddings`

## Authorization

Bearer Token 认证。

Header 示例:

`Authorization: Bearer sk-xxxxxx`

## Path Parameters

### model

`string`

模型/引擎 ID。

## Request Body

| Name | Type | Required | Description |
|---|---|---|---|
| model | string | yes |  |
| input | string \| array<string> | yes | 要嵌入的文本。 |
| encoding_format | string | no | Default`"float"` Value in`"float" \| "base64"` |
| dimensions | integer | no | 输出向量维度。 |

## Response Body

### 200 application/json

```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [0]
    }
  ],
  "model": "string",
  "usage": {
    "prompt_tokens": 0,
    "total_tokens": 0
  }
}
```

## Example Request

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST "https://docs.newapi.pro/v1/engines/string/embeddings" \
  -H "Authorization: Bearer " \
  -H "Content-Type: application/json" \
  -d '{
    "model": "text-embedding-ada-002",
    "input": "string"
  }'
```

{% endtab %}
{% tab title="JavaScript" %}

```javascript
fetch("https://docs.newapi.pro/v1/engines/string/embeddings", {
  method: "POST",
  headers: {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "text-embedding-ada-002",
    input: "string"
  })
});
```

{% endtab %}
{% tab title="Go" %}

```go
package main

import (
  "bytes"
  "net/http"
)

func main() {
  body := bytes.NewBuffer([]byte(`{
    "model": "text-embedding-ada-002",
    "input": "string"
  }`))

  req, _ := http.NewRequest("POST", "https://docs.newapi.pro/v1/engines/string/embeddings", body)
  req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
  req.Header.Set("Content-Type", "application/json")
  http.DefaultClient.Do(req)
}
```

{% endtab %}
{% tab title="Python" %}

```python
import requests

url = "https://docs.newapi.pro/v1/engines/string/embeddings"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}
payload = {
    "model": "text-embedding-ada-002",
    "input": "string"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

{% endtab %}
{% tab title="Java" %}

```java
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://docs.newapi.pro/v1/engines/string/embeddings"))
    .header("Authorization", "Bearer YOUR_API_KEY")
    .header("Content-Type", "application/json")
    .POST(HttpRequest.BodyPublishers.ofString("""
      {
        "model": "text-embedding-ada-002",
        "input": "string"
      }
      """))
    .build();
```

{% endtab %}
{% tab title="C#" %}

```csharp
var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Post, "https://docs.newapi.pro/v1/engines/string/embeddings");
request.Headers.Add("Authorization", "Bearer YOUR_API_KEY");
request.Content = new StringContent(@"
{
  \"model\": \"text-embedding-ada-002\",
  \"input\": \"string\"
}", Encoding.UTF8, "application/json");

await client.SendAsync(request);
```

{% endtab %}
{% endtabs %}

## Example Response

```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [0]
    }
  ],
  "model": "string",
  "usage": {
    "prompt_tokens": 0,
    "total_tokens": 0
  }
}
```
