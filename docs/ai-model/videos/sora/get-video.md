# 获取视频内容

AI 模型接口视频（Videos）Sora格式

# 获取视频内容

获取已完成视频任务的视频文件内容。

此接口会代理返回视频文件流。



/`v1`/`videos`/`{task_id}`/`content`


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
curl -X GET "https://docs.newapi.pro/v1/videos/string/content"
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
