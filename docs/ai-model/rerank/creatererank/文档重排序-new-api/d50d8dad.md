# 文档重排序 | New API

AI 模型接口重排序（Rerank）

# 文档重排序

根据查询对文档列表进行相关性重排序

loading...


/`v1`/`rerank`

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

query\*string

查询文本

documents\*array<string | object>

要重排序的文档列表

top\_n?integer

返回前 N 个结果

return\_documents?boolean

Default`false`

## [Response Body](#response-body)

### 200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://loading/v1/rerank" \  -H "Content-Type: application/json" \  -d '{    "model": "rerank-english-v2.0",    "query": "string",    "documents": [      "string"    ]  }'
```

200

```
{
  "id": "string",
  "results": [
    {
      "index": 0,
      "relevance_score": 0,
      "document": {}
    }
  ],
  "meta": {}
}
```
