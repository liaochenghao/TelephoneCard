# coding: utf-8
import random
import requests

from TelephoneCard.settings import TELEPHONE_MESSAGE_CONFIG
import logging

logger = logging.getLogger('django')


class TelephoneInterface:
    def __init__(self):
        self.id = TELEPHONE_MESSAGE_CONFIG['id']
        self.pwd = TELEPHONE_MESSAGE_CONFIG['pwd']

    def send_message(self, to_user):
        url = 'http://service.winic.org:8009/sys_port/gateway/index.asp'
        random_code = self.generate_code()
        content = "您好，您的验证码是" + str(random_code) + "【留学生福利社】"
        params = {
            'id': self.id,
            'pwd': self.pwd,
            'to': to_user,
            'content': content.encode('GB2312')
        }
        response = requests.post(url=url, data=params)
        content = str(response.content)
        logger.info(content)
        return random_code

    def generate_code(self):
        """
        生成6位数的验证码
        :param code_len: 
        :return: 
        """
        seed = random.random()
        code = str(int(seed * 1000000))
        if len(code) == 5:
            code += '8'
        return code


TelephoneInterfaceUtil = TelephoneInterface()
