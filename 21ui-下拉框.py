from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# /Users/D1anJun/Downloads/test/driver
# service = Service(r'/Users/D1anJun/Downloads/test/driver/chromedriver')  # Mac地址
service = Service(r"D:\test\driver\chromedriver.exe") # win地址
driver = webdriver.Chrome(service = service)
# driver.get("file:///Users/D1anJun/Downloads/test/UI%E8%87%AA%E5%8A%A8%E5%8C%96/web%E7%8E%AF%E5%A2%83/web/%E6%B3%A8%E5%86%8CA.html")
driver.get("file:///D:/test/%E9%BB%91%E9%A9%AC24%E8%B5%84%E6%96%99/UI%E8%87%AA%E5%8A%A8%E5%8C%96/web%E7%8E%AF%E5%A2%83/%E6%B3%A8%E5%86%8CA.html")
time.sleep(1)

time.sleep(1)
# 最大化窗口
driver.maximize_window()
time.sleep(1)
# 点击下拉框展开选项
driver.find_element(By.ID,'sel').click()
time.sleep(1)
# 点击浙江
driver.find_element(By.CSS_SELECTOR,"[value='zj']").click() 
time.sleep(1)
# 点击下拉框展开选项
driver.find_element(By.ID,'sel').click()
time.sleep(1)
# 点击上海
driver.find_element(By.CSS_SELECTOR,"[value='sh']").click() 
time.sleep(1)

driver.quit()

