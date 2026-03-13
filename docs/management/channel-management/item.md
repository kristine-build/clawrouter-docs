# 管理多密鑰

管理介面通道管理

# 管理多密鑰

👨💼 需要管理員權限（Admin）



/`api`../`channel`../`multi_key`../`manage`..


Body

## [Request Body](#request-body)

application/json

channel\_id?integer

action?string

Value in`"get_key_status" | "disable_key" | "enable_key" | "delete_key" | "delete_disabled_keys" | "enable_all_keys" | "disable_all_keys"`..

key\_index?integer

## [Response Body](#response-body)

### 200

### cURL
### JavaScript
### Go
### Python
### Java
### C#

```
curl -X POST "https://clawrouter.com/api/channel/multi_key/manage" \  -H "Content-Type: application/json" \  -d '{}'
```..

200

Empty
