# 点击操作类
import minium

class ClickOperations(minium.MiniTest):
    def click_confirm(self):
        # 点击同意用户隐私协议
        confirm_btn = self.page.wait_for('//button[text()="确认"]', max_timeout=3)
        self.page.get_element('//button[text()="确认"]').click()

    def click_store(self):
        # 点击存包按钮
        store_btn = self.page.wait_for('[class*="main-panel-button"][role="button"]', max_timeout=3)
        self.page.get_element('[class*="main-panel-button"][role="button"]').click()

    def click_VIP_phone(self):
        # 点击确认vip手机号
        confirm_btn = self.page.wait_for('//button[text()="确认"]', max_timeout=3)
        self.page.get_element('//button[text()="确认"]').click()
    
    def click_find_locker(self):      
        # 柜门类型选择器（循环点击类型）
        locker_selectors = [
            ("小柜", "[style='z-index:2'][text()='小柜']"),
            ("中柜", "[style='z-index:2'][text()='中柜']"),
            ("大柜", "[style='z-index:2'][text()='大柜']")
        ]
        for locker_name, selector in locker_selectors:
            try:
                if not self.page.element_is_exists(selector, max_timeout=3):
                    print(f"{locker_name}元素不存在")
                    continue               
                locker = self.page.get_element(selector)
                locker.tap()
                print(f"已点击{locker_name}")               
                if self.page.element_is_exists("//view[text()='温馨提示']", max_timeout=3):
                    print(f"{locker_name}不可用")
                    self.page.get_element("//button//view[text()='确定']").tap()
                    self.app.navigate_back()
                    continue               
                self.page.get_element("//button").tap()
                print(f"{locker_name}确认成功")
                break               
            except Exception as e:
                print(f"{locker_name}处理异常: {str(e)}")
                continue
        else:
            print("所有柜型均不可用")

    def click_privacy_protocol(self):
        # 点击同意隐私协议
        privacy_btn = self.page.wait_for('mot-modal>>>uni-popup>>>button', max_timeout=3)
        self.page.get_element('mot-modal>>>uni-popup>>>button').click()
    
    def click_insurance_service(self):
        # 点击添加保险
        insurance_btn = self.page.wait_for("[class*='icon iconfontcabinet motcabinet-huibiankuang'][]style='font-size:17px']", max_timeout=3)
        self.page.get_element("[class*='icon iconfontcabinet motcabinet-huibiankuang'][]style='font-size:17px']").click()
    
    def click_confirm_order(self):
        # 点击确认下单
        confirm_order_btn = self.page.wait_for("view.deposit-footer-pay", max_timeout=3)
        self.page.get_element("view.deposit-footer-pay").click()

    def click_refuse_insurance_service(self):
        # 点击放弃添加
        refuse_btn = self.page.wait_for("[class*='t-font-normal'][text()='放弃添加']", max_timeout=3)
        self.page.get_element("[class*='t-font-normal'][text()='放弃添加']").click()

    def click_pay_order_2(self):
        # 点击二次确认下单
        pay_order_btn = self.page.wait_for("[hover-stay-time='200'][text()='确认下单']", max_timeout=3)
        self.page.get_element("[hover-stay-time='200'][text()='确认下单']").click()

    def click_create_order_done(self):
        # 点击寄存完成
        done_btn = self.page.wait_for("//button[text()='寄存完成']", max_timeout=3)
        self.page.get_element("//button[text()='寄存完成']").click()

    def click_renewal(self):
        # 点击续费延长
        renewal_btn = self.page.wait_for("//view[text()='不开门续费']", max_timeout=3)
        self.page.get_element("//view[text()='不开门续费']").click()
    
    def click_payforopen(self):
        # 点击支付开门
        payforopen_btn = self.page.wait_for("///view[text()='打开柜门']", max_timeout=3)
        self.page.get_element("///view[text()='打开柜门']").click()
    
    def end_order(self):
        # 结束订单
        end_order_btn = self.page.wait_for("//view[text()='开门并结束']", max_timeout=3)
        self.page.get_element("//view[text()='开门并结束']").click()
    
    def click_halfway_check(self):
        # 二次确认弹窗选择不用了
        halfway_check_btn = self.page.wait_for("//view[text()='不用了']", max_timeout=3)
        self.page.get_element("//view[text()='不用了']").click()

    def click_halfway_check_done(self):
        # 二次确认弹窗选择还要用
        halfway_done_btn = self.page.wait_for("//view[text()='还要用']", max_timeout=3)
        self.page.get_element("//view[text()='还要用']").click()
        
    def click_halfway_open(self):
        # 点击中途开门
        halfway_open_btn = self.page.wait_for("//view[text()='中途开门']", max_timeout=3)
        self.page.get_element("//view[text()='中途开门']").click()

    def click_tips_confirm(self):
        # 点击温馨提示确认
        tips_confirm_btn = self.page.wait_for("//button//view[text()='确定']", max_timeout=3)
        self.page.get_element("//button//view[text()='确定']").click()