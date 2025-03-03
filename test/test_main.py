import minium
from time import sleep
import json
import test_end_order

class Testorder(minium.MiniTest):
    def test_ceart_order(self):
        for i in range(5):
            print(f"第 {i + 1} 次下单")
            self.order()
        self.logger.info("下单操作已执行 5 次，停止循环")
        print("下单操作已执行 5 次，停止循环")
        test_end_order.End_order
        # 1
#     def scan_result(self):
#         mock_result = {
#   "RequestId": "ad55ee72",
#   "Result": {
#     "shop": {
#       "id": "1848721103114694656",
#       "name": "唐总测试网点",
#       "use_balance_enable": False,
#       "use_balance_deposit_enable": False,
#       "force_choose_enable": False,
#       "fetch_confirm_enable": True,
#       "coupon_enable": True,
#       "mt_coupon_enable": False,
#       "vip_coupon_enable": True,
#       "vip_type": "maytek",
#       "auto_get_phone_enable": False,
#       "pos_pay_enable": False,
#       "h5_pay_config": {
#         "default_pay_channel": "alipay",
#         "pay_channel": ["alipay"]
#       },
#       "status": 1,
#       "area_code": "+86",
#       "country": "CN",
#       "currency": {
#         "value": "CNY",
#         "label": "人民币",
#         "symbol": "￥"
#       },
#       "no_problem_coupon_enabled": False
#     },
#     "site": {
#       "id": "1848721843749089280",
#       "name": "【小铁测试网点】",
#       "status": 1,
#       "open_time": 0,
#       "close_time": 0,
#       "fetch_types": ["phone_pass"],
#       "require_phone": [],
#       "related_sites": {
#         "iamge_url": "https://admin-file.xironiot.com/xiaoiconadmin/1737201989552_939394_13050707859489.jpg",
#         "sites": [
#           {
#             "id": "1783404189537189888",
#             "name": "【测试】小梅沙网点"
#           }
#         ]
#       },
#       "follow_enable": False,
#       "identity_enable": False,
#       "location_overview_enable": False,
#       "user_privacy_enable": True,
#       "user_privacy_html": {
#         "en": "https://admin-file.xironiot.com/privacy/1737026720681_144741_en.html",
#         "ms": "https://admin-file.xironiot.com/privacy/1737026720777_569095_ms.html",
#         "zh": "https://admin-file.xironiot.com/privacy/1737026720628_859834_zh.html",
#         "zh_tw": "https://admin-file.xironiot.com/privacy/1737026720729_387282_zh_tw.html"
#       },
#       "force_select_locker_enable": False,
#       "locker_type_text": {
#         "1": {
#           "en": "Designed to accommodate small bags and shopping bags",
#           "ms": "Boleh simpan beg kecil dan beg belanja",
#           "zh": "可存放小包、购物袋",
#           "zh_tw": "可存放小包、購物袋"
#         },
#         "2": {
#           "en": "Suitable for storing large backpacks and 18-inch suitcases.",
#           "ms": "Boleh menyimpan beg besar dan koper 18 inci.",
#           "zh": "可存放大型背包，18寸行李箱",
#           "zh_tw": "可存放大型背包、18寸行李箱"
#         },
#         "3": {
#           "en": "Able to accommodate a 26-inch suitcase",
#           "ms": "Boleh simpan beg 26 inci",
#           "zh": "可存放26寸行李箱",
#           "zh_tw": "可存放26寸行李箱"
#         },
#         "4": {
#           "en": "Capable of storing large luggage",
#           "ms": "Boleh simpan beg besar",
#           "zh": "可存放大件行李",
#           "zh_tw": "可存放大件行李"
#         }
#       },
#       "business_model": "locker",
#       "disclaimer_enabled": True,
#       "province": "广东省",
#       "city": "深圳市",
#       "region": "南山区",
#       "address": "智恒产业园"
#     },
#     "cabinet": {
#       "id": "1801151630067064832",
#       "name": "c82629870916",
#       "type": 1,
#       "status": 1,
#       "online": False,
#       "address": "A",
#       "fake": True,
#       "free_locker_count": 8,
#       "locker_types": [1],
#       "locker_count_map": {
#         "1": 8
#       },
#       "binding_cabinet_id": "",
#       "is_reverse": False,
#       "binding_config": "",
#       "max_unlock_count": 1000,
#       "rental_period_map": {
#         "1": [1]
#       }
#     },
#     "lockers": [
#       {
#         "id": "1826589696739819520",
#         "name": "008",
#         "status": 1,
#         "type": 1,
#         "door_status": 1
#       },
#       {
#         "id": "1801151902662639616",
#         "name": "005",
#         "status": 1,
#         "type": 1,
#         "door_status": 1
#       },
#       {
#         "id": "1801151902675222528",
#         "name": "006",
#         "status": 1,
#         "type": 1,
#         "door_status": 1
#       },
#       {
#         "id": "1826589696714653696",
#         "name": "007",
#         "status": 1,
#         "type": 1,
#         "door_status": 1
#       },
#       {
#         "id": "1801151902650056704",
#         "name": "004",
#         "status": 1,
#         "type": 1,
#         "door_status": 1
#       },
#       {
#         "id": "1803318309469659136",
#         "name": "002",
#         "status": 1,
#         "type": 1,
#         "door_status": 1
#       },
#       {
#         "id": "1801151902553587712",
#         "name": "003",
#         "status": 1,
#         "type": 1,
#         "door_status": 1
#       },
#       {
#         "id": "1803318309448687616",
#         "name": "001",
#         "status": 1,
#         "type": 1,
#         "door_status": 1
#       }
#     ],
#     "face": {
#       "face_url": "",
#       "face_id": ""
#     }
#   }
# }
#         raw_data = json.dumps(mock_result["Result"])
#
#         self.mini.mock_wx_method(
#             "scanCode",
#             result={
#                 "success":True,
#                 "charSet": "UTF-8",
#                 "rawData": raw_data
#             }
#         )
    def payfor_order(self):
        password = self.page.get_element("input[placeholder='输入4位数字，建议用生日']")
        password.input("1111")
        print("输入密码1111")
        self.logger.info("输入密码1111")
        pay_order = self.page.get_element("view.deposit-footer-pay.data-v-a75e3b3c")
        pay_order.tap()
        print("已点击确认下单")
        self.logger.info("已点击确认下单")
        self.page.wait_for('pay-popup>>>uni-popup>>>button', max_timeout=2)
        pay_order2 = self.page.get_element('pay-popup>>>uni-popup>>>button')
        pay_order2.tap()
        print('已点击二次确认下单')
        self.logger.info('已点击二次确认下单')
    def guocheng(self):
        try:
            self.page.wait_for('//button[text()="确认"]', max_timeout=5)
            button_VIPphone = self.page.get_element('//button[text()="确认"]')
            button_VIPphone.tap()
            print("已点击确认vip手机号")
            self.logger.info("已点击确认vip手机号")
        except:
            print("未配置VIP权益")
            self.logger.info("未配置VIP权益")
        try:
            self.page.wait_for("[class*='data-v-e63e22f7'][role='img']", max_timeout=3)
            li_locker = self.page.get_element("[class*='data-v-e63e22f7'][role='img']")
            li_locker.tap()
            print("点击第一个柜门类型")
            self.logger.info("点击第一个柜门类型")
        except:
            print("仅有一种柜门类型")
            self.logger.info("仅有一种柜门类型")
        try:
            button_ty = self.page.get_element("//button[text()='确认']")
            button_ty.tap()
        except:
            print("未打开强制选择柜门")
            self.logger.info("未打开强制选择柜门")
        try:
            self.page.wait_for('mot-modal>>>uni-popup>>>button', max_timeout=3)
            button_xieyi = self.page.get_element('mot-modal>>>uni-popup>>>button')
            button_xieyi.tap()
            print("同意隐私协议")
            self.logger.info("同意隐私协议")
        except:
            print("用户注册协议未开启")
            self.logger.info("用户注册协议未开启")
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
                self.logger.info('暂不支持下单人脸')
        found = self.page.wait_for("//button[text()='寄存完成']", max_timeout=3)
        if found:
            button_wc = self.page.get_element("//button[text()='寄存完成']")
            button_wc.tap()
        else:
            print("未成功下单")
            self.logger.info("未成功下单")
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
            self.logger.info("柜门已满，请更换二维码")
            self.page.wait_for("//button[text()='返回']",max_timeout=3)
            button_sao = self.page.get_element("//button[text()='返回']")
            button_sao.tap()
        else:
            self.guocheng()
