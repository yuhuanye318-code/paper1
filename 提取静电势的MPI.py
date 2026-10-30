import os
import re

# 定义路径
input_path = r"C:\Program Files\multiwfn\Multiwfn_3.8_dev_bin_Win64\Multiwfn_3.8_dev_bin_Win64\ESP_summary.txt"
output_dir = r"C:\Program Files\multiwfn\Multiwfn_3.8_dev_bin_Win64\Multiwfn_3.8_dev_bin_Win64"
output_path = os.path.join(output_dir, "ESP_summary_MPI.txt")

# 检查输入文件是否存在
if not os.path.exists(input_path):
    print(f"错误：找不到输入文件: {input_path}")
    exit(1)

# 创建输出目录（如果不存在）
os.makedirs(output_dir, exist_ok=True)

# 读取并处理文件
results = []
current_molecule = None
capture_next = False

print(f"正在处理文件: {input_path}")

with open(input_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

    for i, line in enumerate(lines):
        line = line.strip()

        # 搜索"Results for:"行
        if "Results for:" in line:
            # 提取分子名
            parts = line.split("Results for:")
            if len(parts) > 1:
                current_molecule = parts[1].strip(": ")
                print(f"找到分子: {current_molecule}")

        # 搜索"Molecular polarity index (MPI)"行
        elif "Molecular polarity index (MPI):" in line:
            # 使用正则表达式精确匹配MPI值
            # 匹配格式: "Molecular polarity index (MPI): 0.91219153 eV (     21.03566 kcal/mol)"
            match = re.search(
                r'Molecular polarity index \(MPI\):\s*[\d\.]+[eE]?[-+]?[0-9]*\s*(?:eV)?\s*\(([\d\.\s]+)\s*kcal/mol\)',
                line
            )

            if match:
                # 提取括号内的kcal/mol数值（去除空格）
                mpi_value = match.group(1).replace(' ', '')
                results.append((current_molecule, mpi_value))
                print(f"  - 提取MPI值: {mpi_value} kcal/mol")
            else:
                # 备用方案：如果正则不匹配，尝试更简单的分割
                parts = line.split('(')
                if len(parts) >= 2:
                    mpi_part = parts[-1].split(')')[0].strip()
                    # 移除"kcal/mol"并清理空格
                    mpi_value = mpi_part.replace('kcal/mol', '').replace(' ', '')
                    results.append((current_molecule, mpi_value))
                    print(f"  - 备用方法提取MPI值: {mpi_value} kcal/mol")
            capture_next = False

# 将结果写入新文件
with open(output_path, 'w', encoding='utf-8') as out_f:
    # 写入标题行（完整格式）
    out_f.write("分子名\tMPI (kcal/mol)\n")
    for molecule, mpi in results:
        # 使用制表符分隔，保持原始精度
        out_f.write(f"{molecule}\t{mpi}\n")

print(f"\n处理完成! 结果已保存到: {output_path}")
print(f"共提取了 {len(results)} 个分子的MPI数据")