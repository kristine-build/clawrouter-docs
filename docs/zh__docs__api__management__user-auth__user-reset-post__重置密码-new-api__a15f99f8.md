> Migrated from NewAPI docs. Content will be adapted for ClawRouter.

# 重置密码 | New API

管理接口用户登陆注册

# 重置密码

复制 Markdown打开

🔓 无需鉴权

loading...

POST

/`api`/`user`/`reset`

Send

Body

## [Request Body](#request-body)

application/json

email?string

token?string

password?string

## [Response Body](#response-body)

### 200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/reset" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

这篇文档对您有帮助吗？

有帮助没帮助

最后更新于
