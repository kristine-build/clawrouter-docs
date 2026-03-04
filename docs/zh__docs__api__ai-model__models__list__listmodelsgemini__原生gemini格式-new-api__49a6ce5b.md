> Migrated from NewAPI docs. Content will be adapted for ClawRouter.

# 原生Gemini格式 | New API

AI 模型接口模型（Models）列出模型

# 原生Gemini格式

复制 Markdown打开

以 Gemini API 格式返回可用模型列表

loading...

GET

/`v1beta`/`models`

Send

Authorization

## [Authorization](#authorization)

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

## [Response Body](#response-body)

### 200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/v1beta/models"
```

200

```
{
  "models": [
    {
      "name": "models/gemini-pro",
      "version": "string",
      "displayName": "string",
      "description": "string",
      "inputTokenLimit": 0,
      "outputTokenLimit": 0,
      "supportedGenerationMethods": [
        "string"
      ]
    }
  ]
}
```

这篇文档对您有帮助吗？

有帮助没帮助

最后更新于
