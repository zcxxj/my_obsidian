
**根据分支名自动添加前缀且自动添加提交时间**

```bash
#!/bin/bash

msg_file="$1"
commit_type="$2"

# 跳过 merge/squash 提交
if [[ "$commit_type" == "merge" || "$commit_type" == "squash" ]]; then
    exit 0
fi

# 获取分支名，失败则显示 HEAD
branch=$(git symbolic-ref --short HEAD 2>/dev/null || echo "HEAD")

# 获取时间（Git Bash 兼容写法）
time_str=$(date "+%Y-%m-%d %H:%M:%S" 2>/dev/null || date)

# 插入前缀（首行），和时间（末行）
sed -i "1s|^|【$branch】 |" "$msg_file"
echo "🕒 $time_str" >> "$msg_file"

```


