# Q：wget是什么命令
`wget` 是 Linux 系统中常用的命令行工具之一，全称是 **"Web Get"**，意思是“从网页获取”。  
它的主要作用是：**从网络上下载文件**。

---

### 作用与用途：

- 从 HTTP、HTTPS 或 FTP 服务器下载文件到本地
    
- 支持断点续传
    
- 支持批量下载
    
- 可以递归下载整个网站
    

---

### 基本用法：

```bash
wget [选项] URL
```

比如：

```bash
wget https://example.com/file.zip
```

这条命令会把 `file.zip` 下载到当前目录。

---

### 常用参数说明：

|参数|作用|
|:--|:--|
|`-c`|断点续传（继续下载未完成的文件）|
|`-O 文件名`|将下载的文件保存成指定文件名|
|`-P 路径`|将下载的文件保存到指定目录|
|`-r`|递归下载整个网站或目录|
|`-np`|不往上层目录递归（配合 `-r` 用）|
|`--limit-rate=速度`|限制下载速度，例如 `--limit-rate=200k`|
|`-q`|安静模式，不输出信息|
|`--user=用户名 --password=密码`|需要认证的站点下载用|

---

### 运行输出结构示例（简要说明）：

执行 `wget https://example.com/file.zip` 时，会看到大致这样的输出：

```
--2025-04-28 19:32:00--  https://example.com/file.zip
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1234567 (1.2M) [application/zip]
Saving to: ‘file.zip’

file.zip           100%[===================>]   1.18M  1.23MB/s    in 0.9s    

2025-04-28 19:32:01 (1.23 MB/s) - ‘file.zip’ saved [1234567/1234567]
```

含义解释：

- **Resolving**：正在解析域名
    
- **Connecting**：正在建立连接
    
- **HTTP request sent**：已发送请求
    
- **Length**：文件大小
    
- **Saving to**：保存为哪个文件
    
- 下载进度条、速度和用时
    

---

要不要我顺便也给你列一下 `wget` 和 `curl` 的简单对比？很多时候也会一起提到。要的话告诉我！🌟
# Q：好的，你对比一下
好的，下面是 **`wget`** 和 **`curl`** 的一个简洁清晰的对比表：

|特性|`wget`|`curl`|
|:--|:--|:--|
|全称|**Web Get**|**Client URL**|
|主要用途|下载文件|下载、上传、测试各种协议数据传输|
|默认行为|下载并保存文件到磁盘|只把内容输出到终端（默认不保存，需要指定保存）|
|支持协议|HTTP, HTTPS, FTP 等|HTTP, HTTPS, FTP, FTPS, SCP, SFTP, LDAP, MQTT 等非常多|
|支持断点续传|是|是（需手动添加参数 `-C -`）|
|递归下载（整个网站）|支持（`-r` 参数）|不支持|
|上传功能|不支持|支持（比如 `-T` 上传文件）|
|使用复杂度|简单，适合下载场景|功能强大但命令略复杂，适合各种网络请求|
|是否默认安装|大部分 Linux 系统预装|大部分 Linux 系统预装|

---

### 常见用法示例：

- `wget` 下载文件：
    
    ```bash
    wget https://example.com/file.zip
    ```
    
- `curl` 下载文件（保存到本地）：
    
    ```bash
    curl -O https://example.com/file.zip
    ```
    
- `curl` 上传文件（例如上传到服务器）：
    
    ```bash
    curl -T localfile.txt ftp://example.com/
    ```
    

---

### 总结：

- **如果只是下载文件**，`wget` 更简单好用。
    
- **如果需要更复杂的控制（比如 API 测试、POST请求、上传文件等）**，`curl` 更强大。
    

---

要不要我再给你画一张更直观的小图或者思维导图？可以帮你以后一眼区分！要的话告诉我！🌟