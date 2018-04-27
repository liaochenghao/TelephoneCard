### 获取用户微信信息接口

**请求地址**:
```
    GET    /api/v1/user_info/{openid}/
```

**请求参数**:
```
     {
        "openid": "XXXXXX"       
     }
```

**成功返回**：
```
{
    "code": null,
    "msg": "请求成功",
    "data": {
        "openid": "123",
        "nickname": "zhangsan",
        "gender": 1,
        "avatar_url": "http://12313123",
        "city": "wuhan",
        "country": "china",
        "province": "hubei",
        "unionid": "123456",
        "session_key": "dwfdwefwefew",
        "privilege": "dfwefew",
        "language": "cn",
        "last_login": null,
        "create_at": "2018-04-24T03:39:03.759889Z"
    },
    "field_name": ""
}
```

**失败返回**：
```

```