### 检查用户账户信息

**请求地址**:
```
    POST     api/v1/user_info/check_account/
```

**请求参数**:
```
    {
        "openid": str  必填,
        "nickname": str,
        "gender": str,
        "province": str,
        "country": str,
        "city": str,
        "avatar_url": str,
        "language": str,
    }
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
         
    },
    "field_name": ""
}
```

**失败返回**：
```

```