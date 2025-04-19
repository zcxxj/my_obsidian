
[[selenium常用代码|示例代码]]


**✅ 一句话解释 Selenium 是什么？**

> **Selenium 是一个可以自动操作浏览器的软件工具**，它能像人一样点网页、输东西、点按钮，甚至抓网页数据。

你可以理解成：

> 🧠「用 Python 控制鼠标和键盘去操作浏览器，就像你手动浏览网页一样！」

---

**✅ 为什么我们需要 Selenium？**

因为很多现代网站（比如 GBIF）：

- 用 JavaScript 动态加载内容（传统爬虫看不到）；
    
- 表格、图表数据在页面加载后才从后台 API 获取；
    
- 有复杂的交互（如：搜索下拉框、分页、点击按钮等）；
    

🛠️ 这时候像 `requests` 或 `BeautifulSoup` 这样的传统爬虫就“看不见”数据，**必须“模拟浏览器行为”**——这正是 Selenium 的强项！

---

**✅ Selenium 能做什么？**

|功能|说明|
|---|---|
|打开网页|自动打开浏览器访问指定网址|
|输入内容|自动往输入框输入文本|
|模拟点击|点击按钮、下拉框、选择列表|
|获取网页内容|提取 HTML、表格、图片等|
|页面滚动、等待、截图、上传文件|✅ 支持！可以和真实用户操作一样|

---

**✅ 支持哪些语言和浏览器？**

|编程语言|✅ 支持|
|---|---|
|Python|✅ 最常用|
|Java / JavaScript / C# / Ruby|✅ 都有 SDK|

|浏览器|✅ 支持|
|---|---|
|Chrome（最常用）|✅ 用 `chromedriver`|
|Firefox|✅ 用 `geckodriver`|
|Edge / Safari|✅ 也可以用|

---

**✅ 用 Python 操作浏览器的简单例子**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# 启动 Chrome 浏览器
driver = webdriver.Chrome()

# 打开 GBIF 出现记录页面
driver.get("https://www.gbif.org/occurrence/search")

# 找到搜索框，输入文字
search_box = driver.find_element(By.CSS_SELECTOR, "input[placeholder='搜索']")
search_box.send_keys("Guangzhou")

# 点击第一个弹出的候选项
suggestion = driver.find_element(By.CSS_SELECTOR, "ul[role='listbox'] li")
suggestion.click()

# 等待表格加载后提取数据 ...
```

---

**✅ 安装方式（以 Python 为例）**

```bash
pip install selenium
```

还要下载浏览器驱动：

- Chrome 用户需下载 [ChromeDriver](https://sites.google.com/chromium.org/driver/)
    
- Firefox 用户下载 [GeckoDriver](https://github.com/mozilla/geckodriver)
    

⚠️ 驱动版本必须与你的浏览器版本匹配。

---

**✅ 应用场景总结**

|使用场景|传统爬虫能否做|Selenium 是否适合|
|---|---|---|
|静态网页，页面一打开就有数据|✅ 能做|可选|
|动态网页，JavaScript 加载数据|❌ 无法|✅ 推荐|
|搜索框、弹出框、下拉选择等操作|❌ 无法|✅ 必须用 Selenium|

---

**🧠 类比说明**

> - `requests` + `BeautifulSoup` 是爬虫的“快递小哥”：按地址搬快递，不理门铃。
>     
> - `Selenium` 是爬虫的“真人扮演者”：能敲门、说话、点按钮、刷脸登录，全能选手。
>     

---

如果你现在已经安装好 Python 和浏览器，我可以帮你一步一步搭好 Selenium 环境，也可以写出一个可运行的 demo，要不要？👨‍💻