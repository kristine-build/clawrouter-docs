# 即梦视频生成

AI 模型接口视频（Videos）

# 获取视频生成任务状态

查询视频生成任务的状态和结果。

任务状态：

- `queued`: 排队中
- `in_progress`: 生成中
- `completed`: 已完成
- `failed`: 失败



/`v1`/`video`/`generations`/`{task_id}`


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

任务 ID

## [Response Body](#response-body)

### 200 application/json

### 404 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://docs.newapi.pro/v1/video/generations/string"
```

200404

```
{
  "task_id": "abcd1234efgh",
  "status": "completed",
  "url": "https://example.com/video.mp4",
  "format": "mp4",
  "metadata": {
    "duration": 5,
    "fps": 30,
    "width": 1280,
    "height": 720,
    "seed": 20231234
  },
  "error": {
    "code": 0,
    "message": "string"
  }
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
