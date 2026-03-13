# 取得檔案內容 (未實作)

AI 模型介面未實作（Unimplemented）檔案（Files）

# 取得檔案內容 (未實作)

此介面尚未實作



## Endpoint
&Authorization

Path

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | AuthorizationBearer <token> 使用 Bearer Token 认证。 格式: `Authorization: Bearer sk-xxxxxx` In: `header` |## [Path Parameters](#path-parameters)

file\_id\*string

## Response Body
### 501 application/json

### cURL
### JavaScript
### Go
### Python
### Java
### C#

```
curl -X GET "https://docs.newapi.pro/v1/files/string/content"
```

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
```