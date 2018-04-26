### 通过code认证接口

**请求地址**:
```
    GET    /api/v1/user_info/authorize/
```

**请求参数**:
```
     {
        "code": "XXXXXX"       
     }
```

**成功返回**：
```
{
    "code": null,
    "msg": "请求成功",
    "data": {
        "openid": "123"       
    },
    "field_name": ""
}
```

**失败返回**：
```

```