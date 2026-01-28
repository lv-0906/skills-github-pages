import minium

class PagesOperation(minium.MiniTest):

    def page_go_index(self):
        # 进入首页
        self.app.go_to('pages/v1/index/index')
    
    def page_go_orderlist(self):
        # 进入订单列表页
        self.app.go_to('sub-pages/me/order/index')