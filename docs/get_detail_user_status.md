### 获取用户状态信息

**请求地址**:
```
    GET    /api/v1/user_detail/get_user_status/
```

**请求参数**:
```
     {
        "openid": "XXXX" 
     }
```

**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "status": 1,    (0-'身份确认中',1-'身份验证失败',2-'待发卡',3-已发卡'),
        "activity_info": {
            "text1": "",
            "text2": "",
            "text3": "",
            "text4": "",
            "text5": ""
        }
    },
    "field_name": ""
}
```

**失败返回**：
```

```