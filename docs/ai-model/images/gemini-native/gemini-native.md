# Gemini原生格式

Gemini 图片生成

## Endpoint

POST `/v1beta/models/{model}:generateContent`

## Authorization

Bearer Token

Header 示例：

`Authorization: Bearer sk-xxxxxx`

## Path Parameters

### model

string

## Request Body

| Name | Type | Required | Description |
|---|---|---|---|
| contents | array<object> | yes | 请求内容列表。 |
| generationConfig | object | yes | 生成配置。 |
| generationConfig.responseModalities | array<string> | yes | 返回模态列表。 |
| generationConfig.imageConfig | object | yes | 图片参数配置。 |
| generationConfig.imageConfig.aspectRatio | string | yes | 图片宽高比。 |
| generationConfig.imageConfig.imageSize | string | yes | 图片尺寸。 |

## Response Body

### 200 application/json

```json
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "image generation result"
          }
        ]
      }
    }
  ]
}
```

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
```

{% endtab %}
{% tab title="JavaScript" %}

```javascript
// 示例未提供
```

{% endtab %}
{% tab title="Go" %}

```go
// 示例未提供
```

{% endtab %}
{% tab title="Python" %}

```python
# 示例未提供
```

{% endtab %}
{% tab title="Java" %}

```java
// 示例未提供
```

{% endtab %}
{% tab title="C#" %}

```csharp
// 示例未提供
```

{% endtab %}
{% endtabs %}

## Example Response

```json
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "image generation result"
          }
        ]
      }
    }
  ]
}
```
