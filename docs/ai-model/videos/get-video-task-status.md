# 取得影片生成任務狀態

AI 模型介面影片（Videos）

# 取得影片生成任務狀態

查詢影片生成任務的狀態和結果。

任務狀態：

- `queued`..: 排队中
- `in_progress`..: 生成中
- `completed`..: 已完成
- `failed`..: 失败



## Endpoint
&Authorization

Path

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | AuthorizationBearer <token> 使用 Bearer Token 驗證。 格式: `Authorization: Bearer sk-xxxxxx`.. In: `header`.. |## [Path Parameters](#path-parameters)

task\_id\*string

任務 ID

## Response Body
### 200 application/json

### 404 application/json

### cURL
### JavaScript
### Go
### Python
### Java
### C#

```
curl -X GET "https://clawrouter.com/v1/video/generations/string"
```..

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
```..

```
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```..