> Migrated from NewAPI docs. Content will be adapted for ClawRouter.

# 原生OpenAI格式 | New API

AI 模型接口模型（Models）列出模型

# 原生OpenAI格式

复制 Markdown打开

获取当前可用的模型列表。

根据请求头自动识别返回格式：

- 包含 `x-api-key` 和 `anthropic-version` 头时返回 Anthropic 格式
- 包含 `x-goog-api-key` 头或 `key` 查询参数时返回 Gemini 格式
- 其他情况返回 OpenAI 格式

loading...

GET

/`v1`/`models`

Send

Authorization

Header

Query

## [Authorization](#authorization)

BearerAuth

AuthorizationBearer <token>

使用 Bearer Token 认证。
格式: `Authorization: Bearer sk-xxxxxx`

In: `header`

## [Query Parameters](#query-parameters)

key?string

Google API Key (用于 Gemini 格式)

## [Header Parameters](#header-parameters)

x-api-key?string

Anthropic API Key (用于 Claude 格式)

anthropic-version?string

Anthropic API 版本

x-goog-api-key?string

Google API Key (用于 Gemini 格式)

## [Response Body](#response-body)

### 200 application/json

### 401 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X GET "https://loading/v1/models"
```

200401

```
{
  "object": "list",
  "data": [
    {
      "id": "gpt-4",
      "object": "model",
      "created": 0,
      "owned_by": "openai"
    }
  ]
}
```

```
{
  "error": {
    "message": "string",
    "type": "string",
    "param": "string",
    "code": "string"
  }
}
```

这篇文档对您有帮助吗？

有帮助没帮助

最后更新于
