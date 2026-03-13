# 原生Gemini格式

AI 模型介面模型（Models）列出模型

# 原生Gemini格式

以 Gemini API 格式回傳可用模型清單



## Endpoint

/v1beta/models
Authorization

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | AuthorizationBearer <token> 使用 Bearer Token 驗證。 格式: `Authorization: Bearer sk-xxxxxx`.. In: `header`.. |
## Response Body

### 200 application/json

### cURL
### JavaScript
### Go
### Python
### Java
### C#

```
curl -X GET "https://docs.newapi.pro/v1beta/models"
```..

```
{
  "models": [
    {
      "name": "models/gemini-pro",
      "version": "string",
      "displayName": "string",
      "description": "string",
      "inputTokenLimit": 0,
      "outputTokenLimit": 0,
      "supportedGenerationMethods": [
        "string"
      ]
    }
  ]
}
```..
