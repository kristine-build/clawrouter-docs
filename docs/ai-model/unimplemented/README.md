# 未实现（Unimplemented）

AI 模型接口未实现（Unimplemented）文件（Files）

# 删除文件 (未实现)

此接口尚未实现

loading...


/`v1`/`files`/`{file_id}`

Send

Authorization

Path

## [Authorization](#authorization)

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

## [Path Parameters](#path-parameters)

file\_id\*string

## [Response Body](#response-body)

### 501 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X DELETE "https://loading/v1/files/string"
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
