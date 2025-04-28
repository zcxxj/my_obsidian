
# Q：激活虚拟环境

你已经找到了虚拟环境的路径：

```
D:\yixin\yixin_test\.venv\Scripts\python.exe
```

那你在 Windows 的 `cmd`（命令提示符）中运行虚拟环境的方式有以下几种 ✅：

---

## ✅ 方法一：**激活虚拟环境**（推荐方式）

在 `cmd` 中运行：

```cmd
D:\yixin\yixin_test\.venv\Scripts\activate.bat
```

如果成功，你会看到前面出现 `(venv)` 或类似提示：

```
(venv) C:\Users\yourname>
```


---


## ✅ 方法三：进入虚拟环境目录 + 激活

```cmd
cd D:\yixin\yixin_test\.venv\Scripts
activate.bat
```

然后你就在虚拟环境中了。

---

## ❗ 如果你看到错误：“activate.bat 无法运行”

可能原因：

- 你当前是 **PowerShell**，而不是 `cmd`，建议切回 cmd 运行
    
- 也可以在 PowerShell 中用：
    

```powershell
.\activate
```

---

## ✅ 验证是否进入虚拟环境

输入：

```cmd
where python
```

应该显示路径是：

```
D:\yixin\yixin_test\.venv\Scripts\python.exe
```

✅ 那就说明你成功使用了虚拟环境。

---

需要我帮你写一个 `.bat` 文件，每次点击就激活虚拟环境并执行某个脚本吗？💡 只要你说“来一个自动运行脚本”，我马上写。

---
---
# Q：路由路径跟踪
```cmd
tracert <对方 IP>
```

# Q： 时间戳脚本

```cmd
:: 在文件名前面添加当前时间（把文件拖到该.bat脚本上使用）

@echo off
setlocal enabledelayedexpansion

:: 获取当前时间信息（兼容多语言系统）
for /f "tokens=1-3 delims=/- " %%a in ("%date%") do (
    set "yyyy=%%a"
    set "mm=%%b"
    set "dd=%%c"
)

for /f "tokens=1-3 delims=:." %%a in ("%time%") do (
    set "hh=%%a"
    set "mi=%%b"
    set "ss=%%c"
)

:: 补零，避免1位数导致格式混乱
set "hh=0!hh!"
set "hh=!hh:~-2!"
set "mi=0!mi!"
set "mi=!mi:~-2!"
set "ss=0!ss!"
set "ss=!ss:~-2!"

:: 组装最终时间戳
set "timestamp=!yyyy!!mm!!dd!_!hh!!mi!!ss!"

:: 重命名文件：加时间戳前缀
ren "%~1" "!timestamp!_%~nx1"

```