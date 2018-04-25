# coding: utf-8
import datetime
import json
import logging
import requests
from rest_framework import exceptions

from TelephoneCard.settings import WX_SMART_CONFIG
from user_info.models import UserInfo

logger = logging.getLogger('django')


class WxInterface:
    def __init__(self):
        self.appid = WX_SMART_CONFIG['appid']
        self.secret = WX_SMART_CONFIG['secret']

    def code_authorize(self, code):
        """
        微信code认证
        :param code: 
        :return: 
        """
        url = "https://api.weixin.qq.com/sns/jscode2session"
        params = {
            'appid': self.appid,
            'secret': self.secret,
            'js_code': code,
            'grant_type': 'authorization_code'
        }
        response = requests.get(url=url, params=params, verify=False)
        if response.status_code != 200:
            logger.info('X' * 70 + "Code Authorize Failure")
            logger.info('WxInterface code_authorize response: %s' % response.text)
            raise exceptions.ValidationError('连接微信服务器异常')
        res = response.json()
        if res.get('openid') and res.get('session_key'):
            # 首先查询数据库中是否存在该用户信息
            user = UserInfo.objects.filter(openid=res['openid']).first()
            if not user:
                # 如果用户不存在，则向数据库插入数据
                user = UserInfo.objects.create(openid=res['openid'], last_login=datetime.datetime.now(),
                                               session_key=res['session_key'])
            else:
                # 如果用户存在则修改最近登录时间
                user.last_login = datetime.datetime.now()
                user.save()
            return {'openid': user.openid}
        else:
            logger.info('微信认证异常 code_authorize response: %s' % response.text)
            raise exceptions.ValidationError('微信认证异常： %s' % json.dumps(res))

    # 调用微信接口向用户发送客服文本消息
    def send_customer_message(self, to_user, text, access_token):
        url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=" + access_token
        params = {
            "touser": to_user,
            "msgtype": "text",
            "text": {
                "content": text
            }
        }
        response = requests.post(url=url, data=json.dumps(params), headers={'Content-Type': 'application/json'})
        if response.status_code != 200:
            logger.info('WxInterface code_authorize response: %s' % response.text)
            raise exceptions.ValidationError('连接微信服务器异常')
        res = response.json()
        logger.info(res)
        return

    # 调用微信接口向用户发送模板消息
    def send_template_message(self, to_user, template_id, form_id, access_token):
        url = "https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token=" + access_token
        params = {
            "touser": to_user,
            "msgtype": "text",
            "text": {
                "content": "123"
            }
        }
        response = requests.post(url=url, data=json.dumps(params), headers={'Content-Type': 'application/json'})
        if response.status_code != 200:
            logger.info('WxInterface code_authorize response: %s' % response.text)
            raise exceptions.ValidationError('连接微信服务器异常')
        res = response.json()
        logger.info(res)
        return

    def get_access_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        params = {
            'appid': self.appid,
            'secret': self.secret,
            'grant_type': 'client_credential'
        }
        response = requests.get(url=url, params=params, verify=False)
        if response.status_code != 200:
            logger.info('WxInterface get_access_token response: %s' % response.text)
            raise exceptions.ValidationError('连接微信服务器异常')
        res = response.json()
        logger.info(res)
        return res['access_token']


WxInterfaceUtil = WxInterface()