### 用户扫码加话费接口

**请求地址**:
```
    GET     api/v1/telephone/get_telephone_charges/
```

**请求参数**:
```
    {
        "code": str
        "user_id": str
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