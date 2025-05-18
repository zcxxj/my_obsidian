def generate_large_text(input_file, output_file, repeat_times=1000):
    """
    将原始文本重复多次，生成一个大文本文件。
    每次将全文追加写入，形成重复内容。
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(output_file, 'w', encoding='utf-8') as out:
        for i in range(repeat_times):
            out.writelines(lines)

    print(f"✅ 生成完成：{output_file}，共写入 {len(lines) * repeat_times} 行")
generate_large_text(
    input_file="war_and_peace.txt",               # 你的原始文本（比如《傲慢与偏见》）
    output_file="bigtext_large.txt",
    repeat_times=100                          # 重复 1000 次，越大越耗时
)
