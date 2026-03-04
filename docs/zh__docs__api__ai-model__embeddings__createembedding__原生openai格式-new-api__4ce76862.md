> Migrated from NewAPI docs. Content will be adapted for ClawRouter.

# 原生OpenAI格式 | New API

AI 模型接口嵌入（Embeddings）

# 原生OpenAI格式

复制 Markdown打开

将文本转换为向量嵌入

loading...

POST

/`v1`/`embeddings`

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

application/json

model\*string

input\*string|array<string>

要嵌入的文本

encoding\_format?string

Default`"float"`

Value in`"float" | "base64"`

dimensions?integer

输出向量维度

## [Response Body](#response-body)

### 200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/embeddings" \  -H "Content-Type: application/json" \  -d '{    "model": "text-embedding-ada-002",    "input": "string"  }'
```

200

```
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [
        0
      ]
    }
  ],
  "model": "string",
  "usage": {
    "prompt_tokens": 0,
    "total_tokens": 0
  }
}
```

这篇文档对您有帮助吗？

有帮助没帮助

最后更新于
