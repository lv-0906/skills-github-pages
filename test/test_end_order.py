import re
import minium
from time import sleep

class End_order(minium.MiniTest):
    def movabel(self):
        # 判断订单是否大于10分钟，是则滑动结束
        huadong = self.page.wait_for("//view[text()='开门后，寄存将结束']")
        if huadong:
            img = self.page.get_element("//movable-view[contains(@class,'popup-index--validation-box')]")
            img.move(220, 0, 800, smooth=True)
    def unlocker(self):
        # 中途开门
        one_button = self.page.get_element("//button[contains(@class,'mot-button--mot-button-normal-square')]")
        button_class = one_button.__getattribute__("class")
        if "disabled" in button_class:
            print("不支持中途开门")
        else:
            self.page.wait_for("//view[text()='继续租用柜子']")
            open_locker = self.page.get_element("//view[text()='继续租用柜子']")
            open_locker.tap()
            sleep(2)
            carry_on = self.page.get_element("//view[text()='还要用']")
            carry_on.tap()
            self.page.wait_for("//button[text()='中途存取完成']")
            print("中途开门成功")
            sleep(2)
            accomplish = self.page.get_element("//button[text()='中途存取完成']")
            accomplish.tap()
            print("已返回首页")
        # open_lockers = self.page.wait_for("//view[text()='不可中途开门']",max_timeout=3)
        # if open_lockers:
        #     print("不支持中途开门")
        # else:
        #     self.page.wait_for("//view[text()='继续租用柜子']")
        #     open_locker = self.page.get_element("//view[text()='继续租用柜子']")
        #     open_locker.tap()
        #     carry_on = self.page.get_element("//view[text()='还要用']")
        #     carry_on.tap()
        #     self.page.wait_for("//button[text()='中途存取完成']")
        #     print("中途开门成功")
        #     accomplish = self.page.get_element("//button[text()='中途存取完成']")
        #     accomplish.tap()
        #     print("已返回首页")
    def end_order(self):
        self.unlocker()
        # 结束寄存，只能结束寄存大于10分钟的订单
        try:
            self.page.wait_for("//view[text()='开门并结束']",max_timeout=3)
            end_o = self.page.get_element("//view[text()='开门并结束']")
            end_o.tap()
            sleep(2)
            try:
                self.page.wait_for("//view[text()='不用了']",max_timeout=3)
                dis_use = self.page.get_element("//view[text()='不用了']")
                dis_use.tap()
                try:
                    self.movabel()
                    try:
                        # self.page.wait_for("//button[contains(@class,'mot-button-primary')]")
                        sleep(5)
                        fan = self.page.get_element("//button[contains(@class,'mot-button-primary')]")
                        fan.tap()
                        print("订单已结束")
                        sleep(3)
                    except:
                        print('未结束订单')
                except:
                    print('无法结束10分钟之内订单，即将退出')
                # try:
                #     self.page.wait_for("//button[text()='确认结束']",max_timeout=3)
                #     queren = self.page.get_element("//button[text()='确认结束']")
                #     queren.tap()
                #     try:
                #         fan = self.page.get_element("//button[text()='完成']")
                #         fan.tap()
                #     except:
                #         print("未正常进入结束页")
                # except:
                #     print("未进入弹出二次确认页")
            except:
                print("未弹出二次确认弹窗")
        except:
            print("未识别到订单")
    def test_end_orders(self):
        for i in range(5):
            order_card = self.page.wait_for('//view[contains(@class,"home-order-list")]',max_timeout=3)
            if order_card:
                print("已找到订单")
                print(f"第 {i + 1} 次操作")
                try:
                    order_time = self.page.get_element("//view[contains(@class,'card-content')and contains(.,'分钟')]")
                    order_mi = order_time.text
                    match = re.search(r'(?:(\d+)小时)?(?:(\d+)分钟)?', order_mi)
                    if match:
                        hours = int(match.group(1)) if match.group(1) else 0
                        minutes = int(match.group(2)) if match.group(2) else 0
                        total_minutes = hours * 60 + minutes
                        
                        if total_minutes >= 10:
                            print(f"订单使用时间 {total_minutes} 分钟，大于10分钟")
                            self.end_order()
                        else:
                            print(f"订单使用时间 {total_minutes} 分钟，小于10分钟，执行中途开门操作")
                            self.unlocker()
                    else:
                        print("无法匹配有效时间信息")
                except Exception as e:
                    print(f"已结束{i}个订单，停止循环：{str(e)}")
            else:
                print("未发现订单，跳过")
                break


