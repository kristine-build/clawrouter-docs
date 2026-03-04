> Migrated from NewAPI docs. Content will be adapted for ClawRouter.

# 获取视频任务状态  | New API

AI 模型接口视频（Videos）Sora格式

# 获取视频任务状态

复制 Markdown打开

OpenAI 兼容的视频任务状态查询接口。

返回视频任务的详细状态信息。

loading...

GET

/`v1`/`videos`/`{task_id}`

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

task\_id\*string

视频任务 ID

## [Response Body](#response-body)

### 200 application/json

### 404 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/v1/videos/string"
```

200404

```
{
  "id": "string",
  "object": "string",
  "model": "string",
  "status": "string",
  "progress": 0,
  "created_at": 0,
  "seconds": "string"
}
```

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
