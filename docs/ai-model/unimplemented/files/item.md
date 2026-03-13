# 上傳檔案 (未实现)

AI 模型介面未实现（Unimplemented）檔案（Files）

# 上傳檔案 (未实现)

此介面尚未实现



## Endpoint
&Authorization

Body

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | AuthorizationBearer <token> 使用 Bearer Token 认证。 格式: `Authorization: Bearer sk-xxxxxx` In: `header` |## Request Body
multipart/form-data

| Name | Type | Required | Description |
|---|---|---|---|
| file | file | no | Format`binary` |
| purpose | string | no |  |## Response Body

### 501 application/json

### cURL
### JavaScript
### Go
### Python
### Java
### C#

```
curl -X POST "https://docs.newapi.pro/v1/files"
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
