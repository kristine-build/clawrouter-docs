# 原生Claude格式

Anthropic Claude Messages API 格式的請求。
需要在請求头中包含 `anthropic-version`..。

## Endpoint

`POST /v1/messages`..

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | - **位置**：`header`.. - **範例**：`Authorization: Bearer YOUR_API_KEY`.. - **說明**：使用 Bearer Token 驗證，不适用时可使用 `x-api-key`..。 |
## Header Parameters

| name | type | required | description | enum | default | range |
| --- | --- | --- | --- | --- | --- | --- |
| anthropic-version | string | yes | Anthropic API 版本。 | `2023-06-01`.. | `2023-06-01`.. | - |
| x-api-key | string | no | Anthropic API Key（可選，也可使用 Bearer Token）。 | - | - | - |

## Request Body
Content-Type: `application/json`..
| name | type | required | description | enum | default | range |
| --- | --- | --- | --- | --- | --- | --- |
| model | string | yes | 模型名称，例如 `claude-3-opus-20240229`..。 | `claude-3-opus-20240229`.., `claude-3-sonnet-20240229`.., `claude-3-haiku-20240307`.. | - | - |
| messages | array<object> | yes | 對話內容数组。 | - | - | - |
| system | string \| array<object> | no | 系統提示词/系統上下文。 | - | - | - |
| max_tokens | integer | yes | 生成最大 token 数。 | - | - | `>= 1`.. |
| temperature | number | no | 温度參數。 | - | - | `0 <= value <= 1`.. |
| top_p | number | no | nucleus sampling 上界。 | - | - | `0 <= value <= 1`.. |
| top_k | integer | no | top-k 采样參數。 | - | - | `>= 1`.. |
| stream | boolean | no | 是否开启流式回應。 | `true`.., `false`.. | `false`.. | - |
| stop_sequences | array<string> | no | 停止词清單。 | - | - | - |
| tools | array<object> | no | 工具調用定义。 | - | - | - |
| tool_choice | object | no | 工具选择策略。 | - | - | - |
| thinking | object | no | 思考/推理相關參數。 | - | - | - |
| metadata | object | no | 额外元資料。 | - | - | - |

## Response Body

### 200

| name | type | description |
| --- | --- | --- |
| id | string | 消息 ID。 |
| type | string | 回應类型，通常为 `message`..。 |
| role | string | 回傳角色，通常为 `assistant`..。 |
| content | array<object> | 回傳內容清單。 |
| content[].type | string | 內容片段类型。 |
| content[].text | string | 文本內容。 |
| model | string | 实际使用模型。 |
| stop_reason | string | 结束原因。 |
| usage | object | 令牌使用量。 |
| usage.input_tokens | integer | 输入 token 数。 |
| usage.output_tokens | integer | 输出 token 数。 |
| usage.cache_creation_input_tokens | integer | 缓存建立输入 token 数。 |
| usage.cache_read_input_tokens | integer | 缓存读取输入 token 数。 |

```json
{
  "id": "string",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "string"
    }
  ],
  "model": "string",
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 0,
    "output_tokens": 0,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0
  }
}
```..
## Error Example

```json
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "Missing required parameter"
  }
}
```..

## Code Examples

### cURL

```bash
curl -X POST "https://docs.newapi.pro/v1/messages" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{ "model": "claude-3-opus-20240229", "messages": [ { "role": "user", "content": "你好，请介绍 API 网关。" } ], "max_tokens": 256 }'
```..

### JavaScript

```javascript
const payload = {
  model: "claude-3-opus-20240229",
  messages: [{ role: "user", content: "你好，请介绍 API 网关。" }],
  max_tokens: 256
};
const response = await fetch("https://docs.newapi.pro/v1/messages", {
  method: "POST",
  headers: {
    "Authorization": "Bearer YOUR_API_KEY",
    "anthropic-version": "2023-06-01",
    "Content-Type": "application/json"
  },
  body: JSON.stringify(payload)
});
console.log(await response.status);
console.log(await response.text());
```..

### Go

```go
package main

func main() {
	payloadJSON := `{
	  "model": "claude-3-opus-20240229",
	  "messages": [{ "role": "user", "content": "你好，请介绍 API 网关。" }],
	  "max_tokens": 256
	}`
	var payload map[string]interface{}
	_ = json.Unmarshal([]byte(payloadJSON), &payload)
	data, _ := json.Marshal(payload)

	req, _ := http.NewRequest("POST", "https://docs.newapi.pro/v1/messages", bytes.NewReader(data))
	req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
	req.Header.Set("anthropic-version", "2023-06-01")
	req.Header.Set("Content-Type", "application/json")
	http.DefaultClient.Do(req)
}
```..

### Python

```python
url = "https://docs.newapi.pro/v1/messages"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "anthropic-version": "2023-06-01",
    "Content-Type": "application/json",
}
payload = {
    "model": "claude-3-opus-20240229",
    "messages": [{"role": "user", "content": "你好，请介绍 API 网关。"}],
    "max_tokens": 256
}
resp = requests.request("POST", url, headers=headers, json=payload, timeout=30)
print(resp.status_code)
print(resp.text)
```..

### Java

```java
HttpClient client = HttpClient.newHttpClient();
String json = "{ \"model\": \"claude-3-opus-20240229\", \"messages\": [{\"role\":\"user\",\"content\":\"你好，请介绍 API 网关。\"}], \"max_tokens\":256 }";
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://docs.newapi.pro/v1/messages"))
    .header("Authorization", "Bearer YOUR_API_KEY")
    .header("anthropic-version", "2023-06-01")
    .header("Content-Type", "application/json")
    .POST(HttpRequest.BodyPublishers.ofString(json))
    .build();
HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.statusCode());
System.out.println(response.body());
```..

### C#

```csharp
var client = new HttpClient();
client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", "YOUR_API_KEY");
client.DefaultRequestHeaders.Add("anthropic-version", "2023-06-01");
var payload = new StringContent(
    "{ \"model\": \"claude-3-opus-20240229\", \"messages\": [{\"role\":\"user\",\"content\":\"你好，请介绍 API 网关。\"}], \"max_tokens\":256 }",
    Encoding.UTF8,
    "application/json"
);
var request = new HttpRequestMessage(HttpMethod.Post, "https://docs.newapi.pro/v1/messages") {
    Content = payload
};
var response = await client.SendAsync(request);
Console.WriteLine((int)response.StatusCode);
Console.WriteLine(await response.Content.ReadAsStringAsync());
```..
