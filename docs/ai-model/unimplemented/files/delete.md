# 刪除檔案 (未实现)

AI 模型介面未实现（Unimplemented）檔案（Files）

# 刪除檔案 (未实现)

此介面尚未实现



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
curl -X DELETE "https://docs.newapi.pro/v1/files/string"
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