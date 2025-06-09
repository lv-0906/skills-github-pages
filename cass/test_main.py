from re import S
from time import sleep
import minium

class Testorder(minium.MiniTest):
    def payfor_order(self):
        # locker_date = self.app.get_storage("__SITE_KEY__")
        # fetchTypes = locker_date.get("fetch_types")
        # if fetchTypes == "phone_pass":
        password = self.page.get_element("input[placeholder='输入4位数字，建议用生日']")
        if password:
            password.input("1111")
            self.capture("已输入密码")
            print("输入密码1111")
        else:
            print("未找到密码输入框")
            face = self.page.get_element("//view[text()=‘人脸认证']")
            if face:
                print('请手动识别人脸,暂不支持自动上传人脸')    
        pay_order = self.page.get_element("view.deposit-footer-pay")
        pay_order.tap()
        print("已点击确认下单")
        self.page.wait_for("button[text()='放弃添加‘]",max_timeout=3) 
        insurance = self.page.get_element("//button[text()='放弃添加']")
        if insurance:
            insurance.tap()
            print("已放弃添加保险")
        else:
            print("未开启保险业务")
        self.page.wait_for('pay-popup>>>uni-popup>>>button', max_timeout=2)
        pay_order2 = self.page.get_element('pay-popup>>>uni-popup>>>button')
        pay_order2.tap()
        print('已点击二次确认下单')
        # TestDemos = TestDemo()
        # TestDemos.passWord()
    def guocheng(self):
        try:
            self.page.wait_for('//button[text()="确认"]', max_timeout=5)
            button_VIPphone = self.page.get_element('//button[text()="确认"]')
            button_VIPphone.tap()
            print("已点击确认vip手机号")
        except:
            print("未配置VIP权益")
        # find_locker = TestFindLocker()
        # find_locker.test_find_locker()
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
    def test_order(self):
        # 点击存包按钮
        p = self.app.get_current_page()
        print(p.path)
        if p.path == "/pages/v1/index/index":
            self.capture("首页")
            sleep(3)
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
        self.guocheng()
