> Migrated from NewAPI docs. Content will be adapted for ClawRouter.

# 获取文件信息 (未实现) | New API

AI 模型接口未实现（Unimplemented）文件（Files）

# 获取文件信息 (未实现)

复制 Markdown打开

此接口尚未实现

loading...

GET

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
curl -X GET "https://loading/v1/files/string"
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

这篇文档对您有帮助吗？

有帮助没帮助

最后更新于
