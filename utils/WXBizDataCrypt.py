import base64
import json
from Crypto.Cipher import AES


class WXBizDataCrypt:
    def __init__(self, appId, sessionKey):
        self.appId = appId
        self.sessionKey = sessionKey

    def decrypt(self, encryptedData, iv):
        # base64 decode
        sessionKey = base64.b64decode(self.sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.b64decode(iv)

        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)
        print(888888888888888888888888888888888)
        a = cipher.decrypt(encryptedData)
        print(a)
        b = self._unpad(a)
        print(b)
        decrypted = json.loads(b)
        print(decrypted)
        if decrypted['watermark']['appid'] != self.appId:
            raise Exception('Invalid Buffer')

        return decrypted

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]
