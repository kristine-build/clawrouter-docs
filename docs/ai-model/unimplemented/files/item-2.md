# 列出檔案 (未實作)

AI 模型介面未實作（Unimplemented）檔案（Files）

# 列出檔案 (未實作)

此介面尚未實作



## Endpoint
&Authorization

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | AuthorizationBearer <token> 使用 Bearer Token 驗證。 格式: `Authorization: Bearer sk-xxxxxx`.. In: `header`.. |## Response Body

### 501 application/json

### cURL
### JavaScript
### Go
### Python
### Java
### C#

```
curl -X GET "https://clawrouter.com/v1/files"
```..

501

```
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```..
