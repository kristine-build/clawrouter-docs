# 取得影片內容

AI 模型介面影片（Videos）Sora格式

# 取得影片內容

取得已完成影片任務的影片檔案內容。

此介面会代理回傳影片檔案流。



## Endpoint
&Authorization

Path

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | AuthorizationBearer <token> 使用 Bearer Token 驗證。 格式: `Authorization: Bearer sk-xxxxxx`.. In: `header`.. |## [Path Parameters](#path-parameters)

task\_id\*string

影片任務 ID

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
curl -X GET "https://clawrouter.com/v1/videos/string/content"
```..

200404

```
"string"
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