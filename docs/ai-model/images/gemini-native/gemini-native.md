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

### Request Body

未提供明确字段信息。

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
curl -X POST "https://docs.newapi.pro/v1beta/models/string:generateContent" \
  -H "Authorization: Bearer " \
  -H "Content-Type: application/json"
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
