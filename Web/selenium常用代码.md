```python
from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys  
import time  
  
# 启动 Chrome 浏览器（确保你已安装 chromedriver）  
driver = webdriver.Chrome()  
  
# 打开网页  
driver.get("https://www.baidu.com")  
  
# 找到输入框（通过 name 属性）  
search_box = driver.find_element(By.NAME, "wd")  
  
# 输入关键词  
search_box.send_keys("Python Selenium 入门")  
  
# 模拟按下回车键  
search_box.send_keys(Keys.RETURN)  
  
# 等待 3 秒（等待页面加载）  
time.sleep(3)  
  
# 截图保存  
driver.save_screenshot("search_result.png")  
print("✅ 搜索完成，截图已保存为 search_result.png")  
  
# 关闭浏览器  
driver.quit()
```
