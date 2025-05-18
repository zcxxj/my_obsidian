# parallel_count.py

from multiprocessing import Pool, cpu_count
from collections import Counter
from preprocess import preprocess_line
import time

def count_words_in_lines(lines):
    """
    处理文本行列表，统计所有词频，返回 Counter 对象。
    """
    counter = Counter()
    for line in lines:
        words = preprocess_line(line)
        counter.update(words)
    return counter

def parallel_count(file_path, num_processes=None):
    """
    并行统计关键词出现频率：
    - 按行读取文件
    - 将行分段分配给多个进程
    - 聚合结果
    """
    if num_processes is None:
        num_processes = cpu_count()

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 平均划分文本行
    chunk_size = len(lines) // num_processes
    chunks = [lines[i * chunk_size:(i + 1) * chunk_size] for i in range(num_processes)]

    # 若无法整除，补上最后一部分
    if len(lines) % num_processes != 0:
        chunks[-1].extend(lines[num_processes * chunk_size:])

    # 并行处理
    with Pool(processes=num_processes) as pool:
        results = pool.map(count_words_in_lines, chunks)

    # 合并所有子结果
    total_counter = Counter()
    for c in results:
        total_counter.update(c)

    return total_counter
