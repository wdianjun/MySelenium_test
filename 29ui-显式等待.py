
from selenium.webdriver.support.ui import Select, WebDriverWait
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

# 显式等待：只针对指定元素或条件，超时异常：TimeoutException


driver.get("file:///D:/test/%E9%BB%91%E9%A9%AC24%E8%B5%84%E6%96%99/UI%E8%87%AA%E5%8A%A8%E5%8C%96/MyProject/test_selenium2607/%E6%B3%A8%E5%86%8CA.html")
# driver.get("https://www.jd.com/")

# 开始执行定位时的当前时间
print("开始时间：", time.strftime("%Y%m%d%H%M%S"))
# 定位延时加载框，当找不到时抛出异常并捕获异常，找到元素时则直接输入：admin
# WebDriverWait(driver, 10, 1)
# driver：浏览器驱动对象。
# 10：最多等待 10 秒。
# 1：每隔 1 秒检查一次。
try:
  res = WebDriverWait(driver,10,1).until(lambda x:x.find_element(By.CSS_SELECTOR,"[placeholder='请输入内容']"))
  res.send_keys('admin')
except Exception as e:
  print('显示等待定位超时')
  raise e
time.sleep(2)
# 结束执行定位时的当前时间
print("结束时间：", time.strftime("%Y%m%d%H%M%S"))
driver.quit()