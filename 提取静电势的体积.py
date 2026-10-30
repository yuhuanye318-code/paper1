import os
import re

# 定义路径
input_path = r"C:\Program Files\multiwfn\Multiwfn_3.8_dev_bin_Win64\Multiwfn_3.8_dev_bin_Win64\ESP_summary.txt"
output_dir = r"C:\Program Files\multiwfn\Multiwfn_3.8_dev_bin_Win64\Multiwfn_3.8_dev_bin_Win64"
output_path = os.path.join(output_dir, "ESP_summary_Volume.txt")

# 检查输入文件是否存在
if not os.path.exists(input_path):
    print(f"错误：找不到输入文件: {input_path}")
    exit(1)

# 创建输出目录（如果不存在）
os.makedirs(output_dir, exist_ok=True)

# 读取并处理文件
results = []
current_molecule = None

print(f"正在处理文件: {input_path}")

with open(input_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

    for i, line in enumerate(lines):
        line = line.strip()

        # 搜索 "Results for:" 行以获取分子名
        if "Results for:" in line:
            # 提取分子名
            parts = line.split("Results for:")
            if len(parts) > 1:
                current_molecule = parts[1].strip().strip(":").strip()
                print(f"找到分子: {current_molecule}")

        # 搜索 "Volume:" 行
        elif "Volume:" in line and "Bohr^3" in line:
            # 使用正则表达式精确匹配括号内的 Angstrom^3 数值
            # 匹配格式: "Volume:  1259.35076 Bohr^3  ( 186.61653 Angstrom^3)"
            # 我们的目标是提取第一个数字 186.61653
            match = re.search(r'\(\s*([\d\.]+)\s*Angstrom\^3\)', line)

            if match:
                volume_value = match.group(1)
                results.append((current_molecule, volume_value))
                print(f"  - 提取体积值: {volume_value} Angstrom^3")
            else:
                print(f"  - 警告: 未在行中找到体积数值: {line}")

# 将结果写入新文件
with open(output_path, 'w', encoding='utf-8') as out_f:
    # 写入标题行
    out_f.write("分子名\t体积 (Angstrom^3)\n")
    for molecule, volume in results:
        # 使用制表符分隔
        out_f.write(f"{molecule}\t{volume}\n")

print(f"\n处理完成! 结果已保存到: {output_path}")
print(f"共提取了 {len(results)} 个分子的体积数据")