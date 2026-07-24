
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
# /Users/D1anJun/Downloads/test/driver
# service = Service(r'/Users/D1anJun/Downloads/test/driver/chromedriver')  # Mac地址
service = Service(r"D:\test\driver\chromedriver.exe") # win地址
driver = webdriver.Chrome(service = service)
driver.get("file:///D:/test/%E9%BB%91%E9%A9%AC24%E8%B5%84%E6%96%99/UI%E8%87%AA%E5%8A%A8%E5%8C%96/web%E7%8E%AF%E5%A2%83/drop.html")
# driver.get("https://www.jd.com/")
# 最大化窗口
driver.maximize_window()
time.sleep(2)
# 创建鼠标对象 需要导包
action = ActionChains(driver)
# 拖到红色框到绿色框位置
red1 = driver.find_element(By.ID,'div1')
green2 = driver.find_element(By.ID,'div2')
action.drag_and_drop(red1,green2)
time.sleep(1)
# 执行鼠标操作
action.perform()
time.sleep(1)
driver.quit()

