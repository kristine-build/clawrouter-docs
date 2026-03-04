> Migrated from NewAPI docs. Content will be adapted for ClawRouter.

# 编辑标签渠道 | New API

管理接口渠道管理

# 编辑标签渠道

复制 Markdown打开

👨‍💼 需要管理员权限（Admin）

loading...

PUT

/`api`/`channel`/`tag`

Send

Body

## [Request Body](#request-body)

application/json

tag?string

new\_tag?string

priority?integer

weight?integer

## [Response Body](#response-body)

### 200

cURLJavaScriptGoPythonJavaC#

```
curl -X PUT "https://loading/api/channel/tag" \  -H "Content-Type: application/json" \  -d '{}'
```

200

Empty

这篇文档对您有帮助吗？

有帮助没帮助

最后更新于
