### 获取用户详细信息接口

**请求地址**:
```
    GET    /api/v1/user_detail/{openid}
```

**请求参数**:
```
     {
        "openid": "XXXX" (可选)
        "status":  (0, '提交资料'), (1, '身份确认'), (2, '身份验证失败'), (3, '身份通过'), (4, '待发卡'), (5, '已发卡'),      
     }
```

**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "user": 1,
                "c_name": "1",
                "country": "1",
                "university": "1",
                "email": "1",
                "grade": "1",
                "wechat": "1",
                "invite_code": "1",
                "abroad_time": "2018-04-25",
                "recipients_name": "fe",
                "recipients_phone": "fe",
                "recipients_address": "",
                "status": 0,
                "create_at": null
            }
        ]
    },
    "field_name": ""
}
```

**失败返回**：
```

```