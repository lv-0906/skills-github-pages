from re import S
import re
from time import sleep
import minium
class TestDemo(minium.MiniTest):
    def test_demo(self):
        sleep(5)
        i = self.page.get_element("//view[contains(.,'分钟')]")
        print(f"获取到的文本：{i}") 
        mi = i.inner_text
        print(f"获取到的文本：{mi}")