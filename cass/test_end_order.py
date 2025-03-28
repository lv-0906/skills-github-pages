import re
import minium
from time import sleep
from minium.native.wx_native.basenative import T
from test_passwrod import TestDemo


class test_End_order(minium.MiniTest):
    def Renewal(self):
        # 判断订单是否欠费，如果欠费则进行续费
        renewal = self.page.wait_for('//view[contains(class,warning-plain)]')
        if renewal:
            print("订单已欠费")
            self.page.get_element("//view[text()='不开门续费']").click()
            print("已点击不开门续费")
            overMoney = self.page.get_element_by_xpath("(//view[contains(@class, 'list')])[2]")
            om = overMoney.inner_text
            if om:
                mon = r"欠费 ¥(\d+(?:\.\d+)?)\s*.*?余额支付\s*¥(\d+(?:\.\d+)?)\s*.*?微信支付\s*¥(\d+(?:\.\d+)?)"
                money = re.search(mon, om,re.DOTALL)
                if money:
                    wechartMoney = float(money.group(3))
                    print(f'需要支付的金额为：{money.group(1)}')
                    print(f"余额支付金额：{money.group(2)}")
                    print(f"微信支付金额：{wechartMoney}")
                    try:
                        paybutton = self.page.get_element("//button//view[text()='支付']")
                        paybutton.tap()
                        print("已点击支付按钮")
                        sleep(2)
                        if wechartMoney > 0:
                            print("使用微信支付")
                            sleep(2)
                            TestDemos = TestDemo()
                            TestDemos.passWord()
                            return True
                        else:
                            print("使用余额支付")
                            return True
                    except:
                        print("未支付成功")
                        return False
            else:
                print("未获取到金额")
                return False
        else:
            print("订单未欠费")
            return True
    def movabel(self):
        # 判断订单是否大于10分钟，是则滑动结束
        huadong = self.page.wait_for("//view[text()='开门后，寄存将结束']")
        if huadong:
            img = self.page.get_element("//movable-view[contains(@class,'popup-index--validation-box')]")
            img.move(220, 0, 800, smooth=True)
    def scan_Code(self):
        sleep(3)
        scan_code = self.page.wait_for("//view[text()='请扫描您存包的储物柜二维码']",max_timeout=3)
        if scan_code:
            scan = self.page.get_element("//button[contains(., '扫码取包')]")
            scan.tap()
            print("请手动识别二维码")
            self.page.wait_for("//view[text()='还要用']",max_timeout=10)
        else:
            print("未开启二次扫码确认或未扫码")
    def unlocker(self):
        # 中途开门
        one_button = self.page.get_element("//button[contains(@class,'mot-button--mot-button-normal-square')]")
        button_class = one_button.__getattribute__("class")
        if "disabled" in button_class:
            print("不支持中途开门")
        else:
            open_locker = self.page.get_element("//view[text()='继续租用柜子']")
            open_locker.tap()
            sleep(2)
            self.scan_Code()
            carry_on = self.page.get_element("//view[text()='还要用']")
            carry_on.tap()
            self.page.wait_for("//button[text()='中途存取完成']")
            print("中途开门成功")
            sleep(2)
            accomplish = self.page.get_element("//button[text()='中途存取完成']")
            accomplish.tap()
            print("已返回首页")
    def end_order(self):
        self.unlocker()
        # 结束寄存，暂时只能结束寄存大于10分钟的订单
        try:
            self.page.wait_for("//view[text()='开门并结束']",max_timeout=3)
            end_o = self.page.get_element("//view[text()='开门并结束']")
            end_o.tap()
            try:
                self.scan_Code()
                dis_use = self.page.get_element("//view[text()='不用了']")
                dis_use.tap()
                try:
                    self.movabel()
                    try:
                        sleep(3)
                        fan = self.page.get_element("//button[contains(@class,'mot-button-primary')]")
                        fan.tap()
                        print("订单已结束")
                        sleep(3)
                    except:
                        print('未结束订单')
                except:
                    print('无法结束10分钟之内订单，即将退出')
            except:
                print("未弹出二次确认弹窗")
        except:
            print("未识别到订单")
    def test_end_orders(self):
        order_card = self.page.wait_for('//view[contains(@class,"home-order-list")]',max_timeout=3)
        if order_card:
            print("已找到订单")
            self.Renewal()
            if self.Renewal == True:
                print("订单已续费或订单未欠费")
                total_minutes = 0
                order_time = self.page.get_element("//view[contains(@class,'card-content')and contains(.,'分钟')]")
                order_mi = order_time.inner_text
                print(f"获取到的文本：{order_mi}")
                order_mi = str(order_mi)
                # 匹配时间
                if order_mi:
                    match = re.search(r'(?:(\d+)天)?((\d+)小时)?(\d+)分钟', order_mi)
                    if match:
                        days = int(match.group(1)) if match.group(1) else 0  # 天数可能为空
                        hours = int(match.group(2)) if match.group(2) else 0  # 小时可能为空
                        minutes = int(match.group(3))  # 分钟一定存在
                        total_minutes = days * 24 * 60 + hours * 60 + minutes  # 计算总时间
                        print(f"总共使用：{total_minutes}分钟")
                    else:
                        print("未匹配到时间")
                else:
                    print("order_mi 为空")
                if  total_minutes >= 10:
                    print("订单使用时间大于10分钟")
                    self.end_order()
                else:
                    print("订单使用时间小于10分钟,执行中途开门操作")
                    self.unlocker()
            else:
                print("订单未成功续费，跳过")
        else:
            print("未发现订单,跳过")


