> Migrated from NewAPI docs. Content will be adapted for ClawRouter.

# 音频翻译 | New API

AI 模型接口音频（Audio）原生OpenAI格式

# 音频翻译

复制 Markdown打开

将音频翻译为英文文本

loading...

POST

/`v1`/`audio`/`translations`

Send

Authorization

Body

## [Authorization](#authorization)

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

## [Request Body](#request-body)

multipart/form-data

file\*file

Format`binary`

model\*string

prompt?string

response\_format?string

temperature?number

## [Response Body](#response-body)

### 200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/audio/translations" \  -F file="string" \  -F model="string"
```

200

```
{
  "text": "string"
}
```

这篇文档对您有帮助吗？

有帮助没帮助

最后更新于
