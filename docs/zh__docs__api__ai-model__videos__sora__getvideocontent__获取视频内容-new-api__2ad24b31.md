> Migrated from NewAPI docs. Content will be adapted for ClawRouter.

# 获取视频内容 | New API

AI 模型接口视频（Videos）Sora格式

# 获取视频内容

复制 Markdown打开

获取已完成视频任务的视频文件内容。

此接口会代理返回视频文件流。

loading...

GET

/`v1`/`videos`/`{task_id}`/`content`

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

### 200 video/mp4

### 404 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/v1/videos/string/content"
```

200404

```
"string"
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
