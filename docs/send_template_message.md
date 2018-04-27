### 修改用户详细信息

**请求地址**:
```
    POST    /api/v1/user_detail/send_template_message
```

**请求参数**:
```
     {      
        "to_user": str(openid)
        "type": 1(用户提交资料消息推送), 2(用户信息审核失败)， 3(用户信息审核成功)
        "page": "点击模板卡片后的跳转页面，仅限本小程序内的页面。支持带参数,（示例index?foo=bar）。该字段不填则模板无跳转。"
        "form_id":  表单编号
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