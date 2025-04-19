**Q：python代码中怎么知道当前解释器和工作目录和PATH环境变量**
太棒了，你问的是：**在 Python 代码中怎么获取当前环境的详细信息**——包括：

1. 当前 Python 解释器路径 ✅
    
2. 当前工作目录 ✅
    
3. 当前 `PATH` 环境变量 ✅
    

---

下面这段代码直接可以打印出你想要的所有信息，适合在调试或定位环境时使用👇

---

## ✅ 一段 Python 代码搞定全部：

```python
import sys
import os
import pprint

print("✅ 当前 Python 解释器路径：")
print(sys.executable)

print("\n📁 当前工作目录 (working directory)：")
print(os.getcwd())

print("\n🌐 当前 PATH 环境变量：")
pprint.pprint(os.environ["PATH"].split(os.pathsep))
```

---

## ✅ 输出示例（你的环境可能类似）：

```
✅ 当前 Python 解释器路径：
D:\yixin\yixin_test\.venv\Scripts\python.exe

📁 当前工作目录 (working directory)：
C:\Users\zcxxj\Desktop\MyProject

🌐 当前 PATH 环境变量：
['D:\\yixin\\yixin_test\\.venv\\Scripts',
 'C:\\Program Files\\Python311\\Scripts',
 'C:\\Program Files\\Python311\\',
 'C:\\Windows\\System32',
 ...
]
```

---

## ✅ 如果你想获取更多：

|获取项|方法|
|---|---|
|Python 版本|`sys.version` 或 `sys.version_info`|
|当前平台 / 操作系统|`sys.platform` / `os.name` / `platform.system()`|
|环境变量（全部）|`os.environ`|
|`pip` 安装位置|`import pip; print(pip.__file__)`|

---

## 🔍 一句话速查版（适合你随时打印）

```python
import sys, os; print(sys.executable); print(os.getcwd()); print(os.environ["PATH"])
```

---

要不要我帮你封装一个 `check_env()` 工具函数，以后你随时 import 一行就能打印这些环境信息？✅