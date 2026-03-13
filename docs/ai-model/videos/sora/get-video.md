# 取得视频内容

AI 模型介面视频（Videos）Sora格式

# 取得视频内容

取得已完成视频任務的视频檔案内容。

此介面会代理回傳视频檔案流。



## Endpoint
&Authorization

Path

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | AuthorizationBearer <token> 使用 Bearer Token 认证。 格式: `Authorization: Bearer sk-xxxxxx` In: `header` |## [Path Parameters](#path-parameters)

task\_id\*string

视频任務 ID

## Response Body
### 200 video/mp4

### 404 application/json

### cURL
### JavaScript
### Go
### Python
### Java
### C#

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