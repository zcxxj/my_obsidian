# main.py

from benchmark import run_benchmark
from visualize import plot_top_words, plot_wordcloud

if __name__ == "__main__":
    file_path = "data/bigtext_large.txt"

    # 执行统计
    serial_result, parallel_result = run_benchmark(file_path)

    # 显示前20个高频词
    print("\n🔝 并行统计 Top 30:")
    for word, count in parallel_result.most_common(30):
        print(f"{word}: {count}")

    # 可视化
    plot_top_words(parallel_result, top_n=30)
    plot_wordcloud(parallel_result)

