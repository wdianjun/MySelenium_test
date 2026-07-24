
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
# 最大化窗口
driver.maximize_window()

# 隐式等待：在定位元素时，定位到元素则直接返回元素，定位不到则间隔一段时间重新定位，到最大超时时长还没找到元素则直接抛出异常：NoSuchElementException
# 设置最大超时时长
driver.implicitly_wait(20) # 20s

driver.get("file:///D:/test/%E9%BB%91%E9%A9%AC24%E8%B5%84%E6%96%99/UI%E8%87%AA%E5%8A%A8%E5%8C%96/MyProject/test_selenium2607/%E6%B3%A8%E5%86%8CA.html")
# driver.get("https://www.jd.com/")

# 开始执行定位时的当前时间
print("开始时间：", time.strftime("%Y%m%d%H%M%S"))
# 定位延时加载输入框输入123456
driver.find_element(By.ID,'delayedInput').send_keys(123456)
time.sleep(2)
# 结束执行定位时的当前时间
print("结束时间：", time.strftime("%Y%m%d%H%M%S"))
driver.quit()