# 点击操作类
import minium

class ClickOperations(minium.MiniTest):
    def click_store(self):
        # 点击存包按钮
        self.page.get_element('[class*="home-panel-button"][role="button"]').click()

    def click_VIP_phone(self):
        # 点击确认vip手机号
        self.page.get_element('//button[text()="确认"]').click()

    def click_privacy_protocol(self):
        # 点击同意隐私协议
        self.page.get_element('mot-modal>>>uni-popup>>>button').click()
    
