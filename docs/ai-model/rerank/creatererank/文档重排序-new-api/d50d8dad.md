# 文件重排序 | ClawRouter

AI 模型介面重排序（Rerank）

# 文件重排序

根据查詢对文件清單进行相關性重排序



## Endpoint
&Authorization

Body

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | AuthorizationBearer <token> 使用 Bearer Token 驗證。 格式: `Authorization: Bearer sk-xxxxxx`.. In: `header`.. |## Request Body
application/json

| Name | Type | Required | Description |
|---|---|---|---|
| model | string | yes |  |
| query | string | yes | 查詢文本 documents\*array<string \| object> 要重排序的文件清單 |
| top_n | integer | no | 回傳前 N 个結果 |
| return_documents | boolean | no | Default`false`.. |## Response Body

### 200 application/json

### cURL
### JavaScript
### Go
### Python
### Java
### C#

```
curl -X POST "https://docs.newapi.pro/v1/rerank" \  -H "Content-Type: application/json" \  -d '{    "model": "rerank-english-v2.0",    "query": "string",    "documents": [      "string"    ]  }'
```..

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
```..
