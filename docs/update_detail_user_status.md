### 修改用户状态接口

**请求地址**:
```
    GET    /api/v1/user_detail/update_status/
```

**请求参数**:
```
     {      
        "openid":"",       
        "status":"", (0-4)
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