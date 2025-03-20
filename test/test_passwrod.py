from time import sleep
from minium.native.wx_native.androidnative import WXAndroidNative
import minium
class TestDemo(minium.MiniTest):
    def passWord(self):
        try:
            passwords = WXAndroidNative(json_conf={})
            passwords.input_pay_password(psw="081512")
            return True
        except Exception as e:
            print(f'未输入密码  异常{e}')
            return False
