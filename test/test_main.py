from time import sleep
import minium
import sys
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("test.log"),  # 记录到文件
        logging.StreamHandler()  # 显示在终端
    ]
 )
# 把 print() 重定向到 logging
class LoggerWriter:
    def __init__(self, level):
        self.level = level
    def write(self, message):
        if message.strip():  # 过滤空行
            self.level(message)
    def flush(self):
        pass
# 让 print() 输出到日志
sys.stdout = LoggerWriter(logging.info)  
sys.stderr = LoggerWriter(logging.error)  
class Testorder(minium.MiniTest):
    def test_ceart_order(self):
        for i in range(5):
            print(f"第 {i + 1} 次下单")
            self.order()
        print("下单操作已执行 5 次，停止循环")
    def payfor_order(self):
        password = self.page.get_element("input[placeholder='输入4位数字，建议用生日']")
        password.input("1111")
        print("输入密码1111")
        pay_order = self.page.get_element("view.deposit-footer-pay")
        pay_order.tap()
        print("已点击确认下单")
        self.page.wait_for("button[text()='放弃添加‘]",max_timeout=3) 
        insurance = self.page.get_element("//button[text()='放弃添加']")
        insurance.tap()
        print("已放弃添加保险")
        self.page.wait_for('pay-popup>>>uni-popup>>>button', max_timeout=2)
        pay_order2 = self.page.get_element('pay-popup>>>uni-popup>>>button')
        pay_order2.tap()
        print('已点击二次确认下单')
        self.passWord()
    def guocheng(self):
        try:
            self.page.wait_for('//button[text()="确认"]', max_timeout=5)
            button_VIPphone = self.page.get_element('//button[text()="确认"]')
            button_VIPphone.tap()
            print("已点击确认vip手机号")
        except:
            print("未配置VIP权益")
        try:
            self.page.wait_for("[class*='data-v-e63e22f7'][role='img']", max_timeout=3)
            li_locker = self.page.get_element("[class*='data-v-e63e22f7'][role='img']")
            li_locker.tap()
            print("点击第一个柜门类型")
        except:
            print("仅有一种柜门类型")
        try:
            button_ty = self.page.get_element("//button[text()='确认']")
            button_ty.tap()
            print("已确认柜门编号")
        except:
            print("未打开强制选择柜门")
        try:
            sleep(3)
            button_xieyi = self.page.get_element('mot-modal>>>uni-popup>>>button')
            button_xieyi.tap()
            print("同意隐私协议")
        except:
            print("用户注册协议未开启")
        try:
            self.page.wait_for("input[placeholder='输入4位数字，建议用生日']", max_timeout=3)
            self.payfor_order()
        except:
            try:
                self.page.wait_for("input[placeholder='输入4位数字，建议用生日']",max_timeout=2)
                self.payfor_order()
            except:
                self.page.wait_for("//button[text()='点击上传']", max_timeout=3)
                print('暂不支持下单人脸')
        found = self.page.wait_for("//button[text()='寄存完成']", max_timeout=5)
        if found:
            button_wc = self.page.get_element("//button[text()='寄存完成']")
            button_wc.tap()
        else:
            print("未成功下单")
    def order(self):
        # 点击存包按钮
        self.page.wait_for('[class*="home-panel-button"][role="button"]',max_timeout=5)
        button_cunb1 = self.page.get_element('[class*="home-panel-button"][role="button"]')
        button_cunb1.tap()
        print("请手动识别机柜二维码")
        self.logger.info("请手动识别机柜二维码")
        full = self.page.wait_for("//button[text()='扫码存包']",max_timeout=3)
        if full:
            print("柜门已满，请更换二维码")
            self.page.wait_for("//button[text()='返回']",max_timeout=3)
            button_sao = self.page.get_element("//button[text()='返回']")
            button_sao.tap()
        else:
            self.guocheng()
    def passWord(self):
        try:
            sleep(10)
            self.native.text_click("0",iscontain=True)
            sleep(0.5)
            self.native.text_click("8",iscontain=True)
            sleep(0.5)
            self.native.text_click("1",iscontain=True)
            sleep(0.5)
            self.native.text_click("5",iscontain=True)
            sleep(0.5)
            self.native.text_click("1",iscontain=True)
            sleep(0.5)
            self.native.text_click("2",iscontain=True)
            money = self.native.get_pay_value()
            print("已输入支付密码",money)
            sleep(5)
            self.native.text_click("完成",iscontain=True)
        except:
            print('未输入密码')
