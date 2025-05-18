# preprocess.py

import re

# 停用词列表（可从文件加载，这里用示例）
tmp_list= [
    'the', 'is', 'in', 'at', 'of', 'and', 'a', 'to', 'on', 'for', 'with', 'as', 'by', 'an', 'be', 'this'
]
tmp_list += ['her', 'i', 'was', 'she', 'that', 'it', 'not', 'you', 'he', 'his', 'had', 'but', 'have', 'mr', 'him', 'my', 's', 'they']
stop_words = set(tmp_list)

def preprocess_line(line):
    """
    对文本行进行预处理：
    - 转为小写
    - 去除标点符号
    - 分词
    - 去除停用词
    """
    # 替换所有非字母字符为空格
    line = re.sub(r'[^a-zA-Z]', ' ', line)
    # 转为小写并分词
    words = line.lower().split()
    # 去除停用词
    return [word for word in words if word not in stop_words]
