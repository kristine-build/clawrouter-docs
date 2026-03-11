# 获取令牌使用情况

管理接口令牌管理

# 获取令牌使用情况

🔑 需要令牌认证（TokenAuth）



/`api`/`usage`/`token`/


Authorization

Header

## [Authorization](#authorization)

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

## [Header Parameters](#header-parameters)

Authorization?string

## [Response Body](#response-body)

### 200

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://docs.newapi.pro/api/usage/token/"
```

200

Empty
