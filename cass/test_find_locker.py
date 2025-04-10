import minium

class TestFindLocker(minium.MiniTest):
    def test_find_locker(self):
        self.app.navigate_to("/pages/v1/device-type/index")
        Slocker = self.page.get_element("//view[text()='小柜']")
        Mlocker = self.page.get_element("//view[text()='中柜']")
        Llocker = self.page.get_element("//view[text()='大柜']")
        locker_types = [
            ("小柜", Slocker),
            ("中柜", Mlocker),
            ("大柜", Llocker)]
        for locker_name, locker_element in locker_types:
            try:
                locker_element.tap()
                print(f"已点击{locker_name}")
                if self.page.element_is_exists("//view[text()='温馨提示']", max_timeout=3):
                    print(f"{locker_name}未配置收费规则，尝试下一个")
                    self.page.get_element("//button//view[text()='确定']").tap()
                    self.app.navigate_back()
                    continue
                self.page.get_element("//button").tap()
                print(f"{locker_name}可用，已确认柜门编号")
                break 
            except Exception as e:
                print(f"{locker_name}元素操作失败: {str(e)}")
                continue
        else:
            print("所有柜门类型均未配置收费规则")