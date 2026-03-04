> Migrated from NewAPI docs. Content will be adapted for ClawRouter.

# 管理用户状态 | New API

管理接口用户管理

# 管理用户状态

复制 Markdown打开

👨‍💼 需要管理员权限（Admin）

loading...

POST

/`api`/`user`/`manage`

Send

Body

## [Request Body](#request-body)

application/json

id?integer

action?string

Value in`"disable" | "enable" | "delete" | "promote" | "demote"`

## [Response Body](#response-body)

### 200

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/api/user/manage" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

这篇文档对您有帮助吗？

有帮助没帮助

最后更新于
