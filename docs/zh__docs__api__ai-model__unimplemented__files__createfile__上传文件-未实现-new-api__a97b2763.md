> Migrated from NewAPI docs. Content will be adapted for ClawRouter.

# 上传文件 (未实现) | New API

AI 模型接口未实现（Unimplemented）文件（Files）

# 上传文件 (未实现)

复制 Markdown打开

此接口尚未实现

loading...

POST

/`v1`/`files`

Send

Authorization

Body

## [Authorization](#authorization)

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

## [Request Body](#request-body)

multipart/form-data

file?file

Format`binary`

purpose?string

## [Response Body](#response-body)

### 501 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/files"
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
