from time import sleep
import minium
class TestDemo(minium.MiniTest):
    def passWord(self):
        sleep(2)
        self.native.text_click("拒绝")
        try:
            sleep(5)
            self.native.text_click("0")
            sleep(0.5)
            self.native.text_click("8")
            sleep(0.5)
            self.native.text_click("1",iscontain=True)
            sleep(0.5)
            self.native.text_click("5",iscontain=True)
            sleep(0.5)
            self.native.text_click("1",iscontain=True)
            sleep(0.5)
            self.native.text_click("2")
            money = self.native.get_pay_value()
            print("已输入支付密码",money)
            sleep(5)
            self.native.text_click("完成")
        except:
            print('未输入密码')
