> Migrated from NewAPI docs. Content will be adapted for ClawRouter.

# 获取令牌使用情况 | New API

管理接口令牌管理

# 获取令牌使用情况

复制 Markdown打开

🔑 需要令牌认证（TokenAuth）

loading...

GET

/`api`/`usage`/`token`/

Send

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
curl -X GET "https://loading/api/usage/token/"
```

200

Empty

这篇文档对您有帮助吗？

有帮助没帮助

最后更新于
