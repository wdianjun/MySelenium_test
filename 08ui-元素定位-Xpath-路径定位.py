# 1.导包
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service # 导入 Service 类。它用于告诉 Selenium：chromedriver.exe 在电脑上的哪个位置，以及如何启动这个驱动程序。
import time

# 2.创建浏览器驱动对象
service = Service(r"D:\test\driver\chromedriver.exe") # 创建一个 ChromeDriver 服务对象。 r"..." 中的 r 表示原始字符串，让 Python 将路径中的 \ 当作普通反斜杠处理。

# 启动 Chrome 浏览器，并将控制权交给 Selenium。
# webdriver.Chrome()：创建 Chrome 浏览器自动化对象。
# service=service：使用刚才指定路径的 chromedriver.exe。
# driver：后续操作浏览器时使用的变量。
driver = webdriver.Chrome(service=service)

# 3.打开测试网址
driver.get("file:///D:/test/%E9%BB%91%E9%A9%AC24%E8%B5%84%E6%96%99/UI%E8%87%AA%E5%8A%A8%E5%8C%96/web%E7%8E%AF%E5%A2%83/%E6%B3%A8%E5%86%8CA.html")

# 4.暂停3秒 
time.sleep(3)

# 使用xpath绝对路径定位用户名输入框输入admin
driver.find_element("xpath", "/html/body/form/div/fieldset/center/p[1]/input").send_keys("admin")
# 使用xpath相对路径定位用户名输入框输入123
# /：只能查找直接子元素
# //：可以查找任意层级的后代元素
driver.find_element("xpath", "//form//p[1]//input").send_keys("123")

time.sleep(3)
# 5.关闭浏览器
driver.quit()
