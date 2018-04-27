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
        "status": 0,    (0-'提交资料', 1-'身份确认中',2-'身份验证失败',3-'身份通过',4-'待发卡',5-已发卡'),
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