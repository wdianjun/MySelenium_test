
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# /Users/D1anJun/Downloads/test/driver
service = Service(r'/Users/D1anJun/Downloads/test/driver/chromedriver')  # Mac地址
driver = webdriver.Chrome(service = service)
driver.get("file:///Users/D1anJun/Downloads/test/UI%E8%87%AA%E5%8A%A8%E5%8C%96/web%E7%8E%AF%E5%A2%83/web/%E6%B3%A8%E5%86%8CA.html")

time.sleep(1)
# 最大化窗口
driver.maximize_window()
time.sleep(1)
# 点击页面alter按钮
driver.find_element(By.ID,"alerta").click()
time.sleep(1)
# 分析是否为js弹出框，通过右键检查，无检查选项测获取弹出框对象的方式处理
# 获取弹出框对象
alert = driver.switch_to.alert
# 获取弹出框文本
print(alert.text)
time.sleep(1)
# 点击弹出框确定按钮
alert.accept()
time.sleep(1)
# 输入账户A信息
driver.find_element(By.ID,"userA").send_keys("admin")
time.sleep(1)
driver.quit()

