import minium

class FindLocker(minium.MiniTest):
    def findLocker(self):
        self.app.navigate_to("/pages/v1/device-type/index")       
        # 定义柜型选择器列表（改为元组存储选择器）
        locker_selectors = [
            ("小柜", "//view[text()='小柜']"),
            ("中柜", "//view[text()='中柜']"),
            ("大柜", "//view[text()='大柜']")
        ]
        for locker_name, selector in locker_selectors:
            try:
                # 安全获取元素，不存在时跳过
                if not self.page.element_is_exists(selector, max_timeout=3):
                    print(f"{locker_name}元素不存在")
                    continue               
                locker = self.page.get_element(selector)
                locker.tap()
                print(f"已点击{locker_name}")               
                # 检查温馨提示
                if self.page.element_is_exists("//view[text()='温馨提示']", max_timeout=3):
                    print(f"{locker_name}不可用")
                    self.page.get_element("//button//view[text()='确定']").tap()
                    self.app.navigate_back()
                    continue               
                # 确认操作
                self.page.get_element("//button").tap()
                print(f"{locker_name}确认成功")
                break               
            except Exception as e:
                print(f"{locker_name}处理异常: {str(e)}")
                continue
        else:
            print("所有柜型均不可用")
