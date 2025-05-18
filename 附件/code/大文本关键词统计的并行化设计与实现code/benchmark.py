# benchmark.py

import time
from parallel_count import parallel_count
from preprocess import preprocess_line
from collections import Counter

def serial_count(file_path):
    """
    串行统计关键词频率，用作基线对比。
    """
    counter = Counter()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            words = preprocess_line(line)
            counter.update(words)
    return counter

def run_benchmark(file_path):
    """
    比较串行与并行两种实现的耗时。
    """
    print("🔍 正在执行串行统计...")
    start = time.time()
    serial_result = serial_count(file_path)
    end = time.time()
    print(f"⏱ 串行耗时：{end - start:.4f} 秒")

    print("⚙️ 正在执行并行统计...")
    start = time.time()
    parallel_result = parallel_count(file_path)
    end = time.time()
    print(f"⏱ 并行耗时：{end - start:.4f} 秒")

    return serial_result, parallel_result
