# 基础操作类
import minium
from minium.native.wx_native.androidnative import WXAndroidNative

class BaseOperation(minium.MiniTest):
    def __init__(self, app):
        self.app = app
    
    def input_password(self):
        # 输入取物密码
        password_input = self.page.get_element("input[placeholder='输入4位数字，建议用生日']")
        if password_input:
            password_input.input("1111")
        else:
            return False
    
    def input_wechat_pay_password(self):
        # 微信支付密码输入
        passwords = WXAndroidNative(json_conf={})
        passwords.input_pay_password(psw="981512")
        return True

    def end_order_slide(self):
        # 滑动结束订单
        self.page.get_element("//movable-view[contains(@class,'popup-index--validation-box')]").move(220, 0, 800, smooth=True)

 
    