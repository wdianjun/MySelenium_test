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

# 打印当前窗口标题和地址
# 注意：当前窗口为webdriver.Chrome(),第一次打开的窗口为当前窗口，无论后续弹出多少个新的窗口，当前窗口始终为第一个
print(driver.title)
print(driver.current_url)
time.sleep(1)
# 设置窗口宽度500px，高度700px
driver.set_window_size(500,700)
time.sleep(1)
# 设置窗口位置x=0px，y=500px
driver.set_window_position(0,500)
time.sleep(1)
# 点击页面百度超链接
driver.find_element(By.CSS_SELECTOR,'#fwB').click()
time.sleep(1)
# 返回注册A页面
driver.back()
time.sleep(1)
# 前进到百度页面
driver.forward()
time.sleep(1)
# 刷新百度页面
driver.refresh()
time.sleep(1)
# 关闭浏览器
driver.quit()
time.sleep(1)