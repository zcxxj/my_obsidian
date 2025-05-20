# Q：tmux是什么
`tmux` 是一个 **终端复用器**（terminal multiplexer），简单来说，它可以让你：

---

## ✅ 一句话解释：

> **在一个终端中开启多个“窗口”，并且这些会话在你退出终端后仍然持续运行。**

---

## ✅ tmux 能做什么？

|功能|说明|
|---|---|
|多窗口|一个终端中可以开多个“子终端”，像标签页一样切换|
|会话保持|即使你关闭 SSH 或终端，程序还在后台跑，之后可重新连接|
|分屏操作|同一屏幕可以上下左右分多个区域运行不同程序|
|后台挂起|程序运行中，你可以 detach（脱离）tmux，会话仍继续|
|远程协作|多人可以同时连接同一个 tmux 会话（像共享屏幕）|

---

## ✅ 使用场景举例

- 通过 SSH 连服务器运行一个脚本，**中途断网也不怕脚本中断**
    
- 训练模型、编译软件、跑定时任务等长期运行命令
    
- 运维工作中长期开着后台服务和实时日志
    
- 写代码 / 远程调试时分多个屏幕窗口同时工作
    

---

## ✅ 快速上手命令

|操作|命令|
|---|---|
|启动 tmux|`tmux`|
|断开会话（程序继续跑）|`Ctrl + B`，然后按 `D`（detach）|
|查看现有会话|`tmux ls`|
|重新连接会话|`tmux attach`|
|新建命名会话|`tmux new -s mysession`|
|连接指定会话|`tmux attach -t mysession`|
|杀掉会话|`tmux kill-session -t mysession`|

---

## ✅ 示例：挂后台任务

```bash
tmux new -s myjob        # 创建会话
python long_task.py      # 跑程序
Ctrl + B，然后按 D       # 脱离 tmux，会话仍在
tmux attach -t myjob     # 随时回来继续
```

---

## ✅ 和 `nohup`、`screen` 比较

|工具|是否支持交互|是否支持分屏|是否支持断点续连|是否推荐|
|---|---|---|---|---|
|`nohup`|❌ 否|❌ 否|❌ 否|简单任务|
|`screen`|✅ 是|✅ 有点繁琐|✅ 是|老工具|
|**`tmux`**|✅ 是|✅ 非常强大|✅ 是|✅ 强烈推荐|

---

## ✅ 安装方式

- Ubuntu/Debian: `sudo apt install tmux`
    
- CentOS/RHEL: `sudo yum install tmux`
    
- macOS (with Homebrew): `brew install tmux`
    

---

如果你想，我可以带你快速练一套 tmux 基本操作，用最直观的方式掌握它。是否需要？