
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
# 获取页面下拉框对象
select = Select(driver.find_element(By.ID,"sel"))
time.sleep(1)
# 选择浙江-通过下标
select.select_by_index(1)
time.sleep(1)
# 选择上海-通过value属性值
select.select_by_value("sh")
time.sleep(1)
# 选择江苏-通过选项文本选择
select.select_by_visible_text("江苏")
time.sleep(1)
driver.quit()

