# 原生OpenAI格式

AI 模型接口审查（Moderations）

# 原生OpenAI格式

检查文本内容是否违反使用政策



/`v1`/`moderations`


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

input\*string|array<string>

model?string

## [Response Body](#response-body)

### 200 application/json

cURLJavaScriptGoPythonJavaC#

```
curl -X POST "https://docs.newapi.pro/v1/moderations" \  -H "Content-Type: application/json" \  -d '{    "input": "string"  }'
```

200

```
{
  "id": "string",
  "model": "string",
  "results": [
    {
      "flagged": true,
      "categories": {},
      "category_scores": {}
    }
  ]
}
```
