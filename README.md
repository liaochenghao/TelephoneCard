# 后台接口文档

### 数据返回格式

**统一为 `json` 格式**:
```
    {
        "code": 0,
        "msg": "success",
        "data": {
            ... // 数据内容
        }
        field_name: ""
    }
```
- code `int` 0为成功，非0为失败
- msg `string` 成功或失败的消息
- data `dict` 返回的数据内容
- field_name: `str`  code为非0状态时，报错字段


**用户信息接口**:
- [获取活动信息接口](docs/get_activity_info.md)
- [获取用户信息接口](docs/get_user_info.md)