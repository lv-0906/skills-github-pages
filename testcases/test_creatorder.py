# 创建订单测试用例

import minium
import time
from core import BaseOperation,ClickOperations,PagesOperation

class TestCreatOrder(minium.MiniTest):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_creat_order(self):
        ClickOperations.click_store(self)
        ClickOperations.click_VIP_phone(self)
        ClickOperations.click_find_locker(self)
        ClickOperations.click_privacy_protocol(self)
        BaseOperation.input_password(self)
        ClickOperations.click_confirm_order(self)
        ClickOperations.click_refuse_insurance_service(self)
        ClickOperations.click_pay_order_2(self)
        BaseOperation.input_wechat_pay_password(self)