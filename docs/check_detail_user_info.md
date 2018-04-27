### 检查用户是否注册详细信息

**请求地址**:
```
    GET    /api/v1/user_detail/check_user_detail/
```

**请求参数**:
```
     {
        "openid": "openid",        
     }
```

**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
       true/false
    },
    "field_name": ""
}
```

**失败返回**：
```

```