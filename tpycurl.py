import pycurl
from io import BytesIO
c = pycurl.Curl()
c.setopt(pycurl.SSL_VERIFYPEER, 0)
c.setopt(pycurl.SSL_VERIFYHOST, 0)
c.setopt(pycurl.URL, "https://www.baidu.com/")
buffer = BytesIO()
buffer_header = BytesIO()
c.setopt(pycurl.WRITEHEADER,buffer_header )
c.setopt(pycurl.WRITEDATA,buffer )
c.perform()
print(buffer_header.getvalue().decode()) #输出网页源代码
print(buffer.getvalue().decode()) #输出 响应头信息
HTTP_CODE = c.getinfo(pycurl.HTTP_CODE) #输出 响应 http状态
print(HTTP_CODE)