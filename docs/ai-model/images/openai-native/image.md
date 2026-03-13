# 編輯影像

AI 模型介面影像（Images）原生OpenAI格式

# 編輯影像

在给定原始影像和提示的情况下建立編輯或扩展影像。



/`v1`/`images`/`edits`/


Authorization

Body

## Authorization
| Name | Type | Required | Description |
|---|---|---|---|
| Authorization | string | yes | AuthorizationBearer <token> In: `header` |
## Request Body
multipart/form-data

| Name | Type | Required | Description |
|---|---|---|---|
| image | file | yes | 要編輯的影像。必須是有效的 PNG 檔案，小于 4MB，并且是方形的。如果未提供遮罩，影像必須具有透明度，将用作遮罩。 Format`binary` |
| mask | file | no | 附加影像，其完全透明区域（例如，alpha 为零的区域）指示image应編輯的位置。必須是有效的 PNG 檔案，小于 4MB，并且尺寸与原始image相同。 Format`binary` |
| prompt | string | yes | 所需影像的文本描述。最大长度为 1000 个字符。 |
| n | string | no | 要生成的影像数。必須介于 1 和 10 之间。 |
| size | string | no | 生成影像的大小。必須是`256x256`、`512x512`或 `1024x1024`之一。 |
| response_format | string | no | 生成的影像回傳的格式。必須是`url`或`b64_json`。 |
| user | string | no | 代表您的最终使用者的唯一标识符，可以帮助 OpenAI 监控和检测滥用行为。[了解更多](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids)。 |
| model | string | no |  |
## Response Body

### 200 application/json

### cURL
### JavaScript
### Go
### Python
### Java
### C#

```
curl -X POST "https://docs.newapi.pro/v1/images/edits/" \  -F image="cmMtdXBsb2FkLTE2ODc4MzMzNDc3NTEtMjA=/31225951_59371037e9_small.png" \  -F prompt="A cute baby sea otter wearing a beret."
```

```
{}
```
