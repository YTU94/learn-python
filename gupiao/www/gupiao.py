class Stock():
  def __init__(self,q,stock_num='10000'):
    self.q=q
    self.stock_num=stock_num
    self._terminal=True
  
  def query_stock_real_price(self):