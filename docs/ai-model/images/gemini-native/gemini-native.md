# Gemini原生格式

Gemini 图片生成

## Endpoint

POST `/v1beta/models/{model}:generateContent`..

## Authorization

BearerAuth

Header 範例：

`Authorization: Bearer <token>`..

使用 Bearer Token 认证。 格式: Authorization: Bearer sk-xxxxxx

In: header

## Path Parameters

### model

string

模型名称

## Request Body

| Name | Type | Required | Description |
|---|---|---|---|
| contents | array<object> | yes |  |
| generationConfig | object | yes |  |
| generationConfig.responseModalities | array<string> | yes |  |
| generationConfig.imageConfig | object | yes |  |
| generationConfig.imageConfig.aspectRatio | string | yes |  |
| generationConfig.imageConfig.imageSize | string | yes |  |

## Response Body

### 200 application/json

```json
{
  "candidates": [
    {
      "content": {
        "role": "string",
        "parts": [
          {}
        ]
      },
      "finishReason": "string",
      "safetyRatings": [
        {}
      ]
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 0,
    "candidatesTokenCount": 0,
    "totalTokenCount": 0
  }
}
```..

## Example Request

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST "https://docs.newapi.pro/v1beta/models/string:generateContent/" \
  -H "Authorization: Bearer " \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {}
    ],
    "generationConfig": {
      "responseModalities": [
        "string"
      ],
      "imageConfig": {
        "aspectRatio": "string",
        "imageSize": "string"
      }
    }
  }'
```..

{% endtab %}
{% tab title="JavaScript" %}

```javascript
// 範例未提供
```..

{% endtab %}
{% tab title="Go" %}

```go
// 範例未提供
```..

{% endtab %}
{% tab title="Python" %}

```python
# 範例未提供
```..

{% endtab %}
{% tab title="Java" %}

```java
// 範例未提供
```..

{% endtab %}
{% tab title="C#" %}

```csharp
// 範例未提供
```..

{% endtab %}
{% endtabs %}

## Example Response

```json
{
  "candidates": [
    {
      "content": {
        "role": "string",
        "parts": [
          {}
        ]
      },
      "finishReason": "string",
      "safetyRatings": [
        {}
      ]
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 0,
    "candidatesTokenCount": 0,
    "totalTokenCount": 0
  }
}
```..
