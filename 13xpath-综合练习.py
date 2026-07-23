import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 1.创建浏览器驱动对象
service = Service(r"D:\test\driver\chromedriver.exe") # 创建一个 ChromeDriver 服务对象。 r"..." 中的 r 表示原始字符串，让 Python 将路径中的 \ 当作普通反斜杠处理。  
driver = webdriver.Chrome(service=service) # 启动 Chrome 浏览器，并将控制权交给 Selenium。webdriver.Chrome()：创建 Chrome 浏览器自动化对象。service=service：使用刚才指定路径的 chromedriver.exe。driver：后续操作浏览器时使用的变量。

driver.get("https://kdtx-test.itheima.net/#/login") # 3.打开测试网址

time.sleep(1) # 4.暂停1秒

# 使用xpath 属性定位策略定位账户输入框，输入：
driver.find_element("xpath", "//*[@placeholder='账号']").send_keys("admin")
time.sleep(1)
# 使用xpath 属性包含定位策略定位密码输入框，输入：
driver.find_element("xpath", "//*[contains(@type, 'passw')]").send_keys("HM_2023_test")
time.sleep(1)
# 使用xpath 属性与逻辑结合策略定位验证码输入框，输入：
driver.find_element("xpath", "//input[@placeholder='验证码' and @class='el-input__inner']").send_keys("2")
time.sleep(1)
# 使用xpath 属性与层级结合策略定位登录按钮，点击登录
driver.find_element("xpath", "//div[@class='el-form-item__content']//button").click()
time.sleep(3)