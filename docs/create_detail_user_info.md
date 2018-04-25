### 创建用户详细信息

**请求地址**:
```
    POST    /api/v1/user_detail/
```

**请求参数**:
```
     {
        "user": "openID",
        "c_name":"",
        "country":"",
        "university":"",
        "email":"",
        "grade":"",
        "wechat":"",
        "invite_code":"",
        "abroad_time":"",
        "recipients_name":"",
        "recipients_phone": "",
        "recipients_address":"",
        "status":"",
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