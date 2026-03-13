# 文档重排序

AI 模型介面重排序（Rerank）

# 文档重排序

根据查詢对文档清單进行相关性重排序



## Endpoint
&Authorization

Body

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | AuthorizationBearer <token> 使用 Bearer Token 认证。 格式: `Authorization: Bearer sk-xxxxxx` In: `header` |## Request Body
application/json

| Name | Type | Required | Description |
|---|---|---|---|
| model | string | yes |  |
| query | string | yes | 查詢文本 documents\*array<string \| object> 要重排序的文档清單 |
| top_n | integer | no | 回傳前 N 个结果 |
| return_documents | boolean | no | Default`false` |## Response Body

### 200 application/json

### cURL
### JavaScript
### Go
### Python
### Java
### C#

```
curl -X POST "https://docs.newapi.pro/v1/rerank" \  -H "Content-Type: application/json" \  -d '{    "model": "rerank-english-v2.0",    "query": "string",    "documents": [      "string"    ]  }'
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
