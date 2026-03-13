# 鉴权体系说明（Auth）

管理介面

# 鉴权体系说明（Auth）

后台管理介面鉴权方式与权限级别说明

## [说明](#说明)

后台管理介面采用多级鉴权机制，常见为：**公开**、**用户**、**管理员**、**Root**。

## [认证方式（二选一）](#认证方式二选一)

### [Session](#session)

通过登录介面取得 Session：

- `POST /api/user/login`

### [Access Token（推荐）](#access-token推荐)

在請求头中携带：

```
Authorization: Bearer {token}
```

Token 可在「个人设置 - 安全设置 - 系统访问令牌」中生成。

## [必需請求头](#必需請求头)

部分介面要求携带用户标识請求头：

```
New-Api-User: {user_id}
```

其中 `{user_id}` 必须与当前登录用户匹配。

## [权限级别](#权限级别)

- **公开（Public）**：无需鉴权
- **用户（User）**：需要登录或 Access Token
- **管理员（Admin）**：需要管理员权限
- **Root**：最高权限
