# 创建视频

AI 模型接口视频（Videos）Sora格式

# 创建视频

OpenAI 兼容的视频生成接口。

参考文档: <https://platform.openai.com/docs/api-reference/videos/create>



## Endpoint
&Authorization

Body

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | AuthorizationBearer <token> 使用 Bearer Token 认证。 格式: `Authorization: Bearer sk-xxxxxx` In: `header` |## Request Body
multipart/form-data

| Name | Type | Required | Description |
|---|---|---|---|
| model | string | no | 模型/风格 ID |
| prompt | string | no | 文本描述提示词 |
| image | string | no | 图片输入 (URL 或 Base64) |
| duration | number | no | 视频时长（秒） |
| width | integer | no | 视频宽度 |
| height | integer | no | 视频高度 |
| fps | integer | no | 视频帧率 |
| seed | integer | no | 随机种子 |
| n | integer | no | 生成视频数量 |
| response_format | string | no | 响应格式 |
| user | string | no | 用户标识 |
| metadata | object | no | 扩展参数 (如 negative\_prompt, style, quality\_level 等) |## Response Body

### 200 application/json

### 400 application/json

### cURL
### JavaScript
### Go
### Python
### Java
### C#

```
curl -X POST "https://docs.newapi.pro/v1/videos"
```

200400

```
{
  "id": "string",
  "object": "string",
  "model": "string",
  "status": "string",
  "progress": 0,
  "created_at": 0,
  "seconds": "string",
  "completed_at": 0,
  "expires_at": 0,
  "size": "string",
  "error": {
    "message": "string",
    "code": "string"
  },
  "metadata": {}
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
