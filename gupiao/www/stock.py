import tushare as ts
import datetime
import time

class Stock():
  def __init__(self, q, stock_num='002736'):
    self.q=q
    self.stock_num=stock_num
    self._terminal=True
  
  def query_stock_real_price(self):
    df = ts.get_realtime_quotes(self.stock_num)
    df=df[['price','time']]
    price=df['price'].values[0]
    time=df['time'].values[0]
    print(df)
    return price,time

  def get_kline_data(self, ktype='ma5'):
    today=datetime.datetime.now().strftime('%Y-%m-%d')
    df = ts.get_hist_data(self.stock_num, start='2018-08-08', end=today)
    return (df[[ktype]])

  def start_run(self):
    while self._terminal:
      p,t=self.query_stock_real_price()
      print ('--->',t,p)
      # print (''.format(t, p))
      format(t, p)
      real_price=float(p)
      self.q = real_price
      time.sleep(3)
  
  def stop_run(self):
    self._terminal=False

s = Stock('a')
s.start_run()