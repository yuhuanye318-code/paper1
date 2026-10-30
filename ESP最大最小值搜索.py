import os

# 输入基础文件名（用空格分隔）
input_names = input("请输入基础文件名（用空格分隔，例如: bl fn）: ")
base_names = input_names.split()  # 分割成列表

# 构建完整文件名列表
files = [f"{name}-surfanalysis.pdb" for name in base_names]

for fname in files:
    path = os.path.join(r"C:\Program Files\VMD", fname)

    print(f"\n{'=' * 50}")
    print(f"文件: {fname}")
    print('=' * 50)

    if not os.path.exists(path):
        print("文件不存在！")
        continue

    with open(path) as f:
        hetatm = [l.strip() for l in f if l.startswith('HETATM')]

    # C(静电势极大值点)
    c_atoms = [l for l in hetatm if l.endswith('C')]
    print(f"\nC极大值点({len(c_atoms)}个):")
    for c in c_atoms:
        print(f"  {c}")
    if c_atoms:
        c_vals = []
        for l in c_atoms:
            bf = l.split()[-2]
            # 和O原子一样处理粘连情况
            c_vals.append(float(bf[4:]) if '1.00' in bf else float(bf))
        print(f"极大值点中max（ESP）: {max(c_vals):.2f}")

    # O(静电势极小值点)
    o_atoms = [l for l in hetatm if l.endswith('O')]
    print(f"\nO极小值点({len(o_atoms)}个):")
    for o in o_atoms:
        print(f"  {o}")
    if o_atoms:
        o_vals = []
        for l in o_atoms:
            bf = l.split()[-2]
            o_vals.append(float(bf[4:]) if '1.00' in bf else float(bf))
        print(f"极小值点中min（ESP）: {min(o_vals):.2f}")