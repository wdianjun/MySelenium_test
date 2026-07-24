# 1.导包
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
# 最大化窗口
time.sleep(1)
driver.maximize_window()
# 4.暂停1秒 
time.sleep(1)
# 获取账户输入框大小
print(f"获取账户输入框大小:{driver.find_element(By.ID,'userA').size}")
# 获取第一个超链接文本内容
print(f"获取第一个超链接文本内容:{driver.find_element(By.TAG_NAME,'a').text}")
# 获取第一个超链接的 href 属性值
print(f"获取第一个超链接的 href 属性值:{driver.find_element(By.TAG_NAME,'a').get_attribute('href')}")
# 判断span标签是否隐藏
print(f"判断span标签是否隐藏:{driver.find_element(By.ID,'span1').is_displayed()}")
# 判断按钮是否可用
res = driver.find_element(By.XPATH,"//button[@value='取消']").is_enabled()
print("判断按钮是否可用",res)
# 判断复选框是否选中
print(f"判断复选框是否选中:{driver.find_element(By.ID,'checkboxB').is_selected()}")

time.sleep(1)
# 5.关闭浏览器
driver.quit()
