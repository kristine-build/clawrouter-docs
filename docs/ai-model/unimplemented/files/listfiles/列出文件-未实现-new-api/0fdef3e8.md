# 列出文件 (未实现) | New API

AI 模型接口未实现（Unimplemented）文件（Files）

# 列出文件 (未实现)

此接口尚未实现



/`v1`/`files`


Authorization

## [Authorization](#authorization)

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

## [Response Body](#response-body)

### 501 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://docs.newapi.pro/v1/files"
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
