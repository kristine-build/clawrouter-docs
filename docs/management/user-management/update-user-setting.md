# 更新用户设置

管理接口用户管理

# 更新用户设置

🔐 需要登录（User权限）



/`api`/`user`/`setting`


Body

## [Request Body](#request-body)

application/json

notify\_type?string

quota\_warning\_threshold?number

webhook\_url?string

notification\_email?string

## [Response Body](#response-body)

### 200

cURLJavaScriptGoPythonJavaC#

```
curl -X PUT "https://docs.newapi.pro/api/user/setting" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty
