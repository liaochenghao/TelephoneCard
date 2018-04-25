### 人工审核修改用户状态接口

**请求地址**:
```
    GET    /api/v1/user_detail/update_man_made_status/
```

**请求参数**:
```
     {      
        "operator":"后台操作人员编号",       
        "target_user_id":"被操作对象的openid",       
        "status":"", (0-审核失败  1-审核成功)
        "extra":"备注", 
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