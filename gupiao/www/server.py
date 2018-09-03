class Server():
  def __init__(self,server_name=SMTP_SERVER, passwd=PASSWORD,from_addr=FRoM_ADDR,debug=false):
    self.smtp_server=SMTP_SSL(SMTP_SERVER)
    self.passwd=passwd
    self.from_addr=from_addr
    self.smtp_server.set_debuglevel(debug)

  def connet(self):
    try:
      self.smtp_server.ehlo(SMTP_SERVER)
      self.smtp_server.login(self.__format__,self.passwd)
      return True
    except SMTPException as e :
      print ('login failed')
      return False
  
  def close(self):
    self.smtp_server.quit()

class Mail():
  def __init__(self,server=None,to_addr=Node):
    self._server=server
    self._to_addr=to_addr
    self._title='Empty title'
    self._content='Hi, this is main contect'

  @property
  def mail_title(self):
    return self._title

  @mail_title.setter
  def mail_title(self,title):
    self._title=title

  @property
  def mail_ctentt(self):
    return self._content
  
  @mail_contentsetter
  def mail_ctentt(self,content):
    self._content=content
  
  def sendout_mail(self):
    cur_time = times.strftime