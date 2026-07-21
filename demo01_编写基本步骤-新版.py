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
driver.get("https://chat.deepseek.com/")

# 4.暂停3秒 代替测试步骤
time.sleep(3)

# 5.关闭浏览器
driver.quit()
