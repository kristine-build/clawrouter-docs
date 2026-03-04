> Migrated from NewAPI docs. Content will be adapted for ClawRouter.

# 更新当前用户信息 | New API

管理接口用户管理

# 更新当前用户信息

复制 Markdown打开

🔐 需要登录（User权限）

loading...

PUT

/`api`/`user`/`self`

Send

Body

## [Request Body](#request-body)

application/json

username?string

display\_name?string

password?string

original\_password?string

## [Response Body](#response-body)

### 200

cURLJavaScriptGoPythonJavaC#

```
curl -X PUT "https://loading/api/user/self" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

这篇文档对您有帮助吗？

有帮助没帮助

最后更新于
