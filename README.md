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
- [创建用户微信信息接口](docs/create_user_info.md)
- [通过code验证微信用户信息接口](docs/code_auth.md)
- [插入用户微信信息接口](docs/check_account.md)
- [获取短信验证码接口](docs/message_code.md)
- [获取用户详细信息列表接口](docs/get_detail_user_info_list.md)
- [创建用户详细信息接口](docs/create_detail_user_info.md)
- [修改用户详细信息接口](docs/update_detail_user_info.md)

