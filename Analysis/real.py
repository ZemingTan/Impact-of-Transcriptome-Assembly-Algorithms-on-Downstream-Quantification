import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取CSV文件（请替换为你的文件路径）
file_path = 'pairwise_correlation_results.csv'  # 修改为你的文件路径
df = pd.read_csv(file_path)

# 检查数据列是否正确（假设列名与示例一致）
print("CSV文件列名验证:", df.columns.tolist())

# 定义工具顺序
tools = ['stringtie', 'scallop', 'cufflinks', 'salmon']
n_tools = len(tools)

# 创建图形
fig, axes = plt.subplots(n_tools, n_tools, figsize=(10, 10))
plt.subplots_adjust(wspace=0, hspace=0)

# 存储所有数据用于散点图
pair_data = {}

# 处理列名配对（直接从CSV的header获取）
for col in df.columns[1:]:  # 跳过第一列(sample列)
    a, b = col.split('-')
    pair_data[(a, b)] = df[col].values.astype(float)

# 绘制每个子图
for i in range(n_tools):
    for j in range(n_tools):
        ax = axes[i, j]
        ax.set_xticks([])
        ax.set_yticks([])
        
        for spine in ax.spines.values():
            spine.set_visible(True)
        
        # 绘制对角线
        if i == j:
            ax.plot([0, 1], [1, 0], transform=ax.transAxes, color='gray', lw=1)
            continue
            
        # 下三角显示平均值
        if i > j:
            a, b = tools[j], tools[i]
            if (a, b) in pair_data:
                avg = np.mean(pair_data[(a, b)])
                ax.text(0.5, 0.5, f'{avg:.3f}', 
                       ha='center', va='center', fontsize=15)
                ax.set_facecolor('#f0f0f0')
        
        # 上三角绘制散点图
        if i < j:
            a, b = tools[i], tools[j]
            if (a, b) in pair_data:
                # 使用相同工具对的列
                values = pair_data[(a, b)]
                
                # 绘制散点
                ax.scatter(np.random.normal(0, 0.05, len(values)) + 0.5, 
                          values, s=20, alpha=0.7, color='#1f77b4')
                
                # 设置坐标轴范围
                ax.set_ylim(0.6, 1.05)
                ax.set_xlim(0, 1)
                
                
                # 显示边界的刻度
                if i == 0:
                    ax.spines['top'].set_visible(True)

                
                if j == n_tools-1:
                    ax.spines['right'].set_visible(True)
                    ax.yaxis.set_ticks_position('right')
                    ax.set_yticks([0.6, 0.8, 1.0])
                    ax.set_yticklabels([0.6, 0.8, 1.0], fontsize=15)
ax.set_xticks([])
# 添加矩阵外侧标签
for idx, tool in enumerate(tools):
    # 顶部标签
    fig.text((idx*0.75+0.9)/n_tools, 0.9, tool, 
            ha='center', va='center', fontsize=15)
    # 右侧标签
    fig.text(0.1, (n_tools - idx*0.8 - 0.9)/n_tools, tool, 
            ha='center', va='center', fontsize=15, rotation=-90)
plt.savefig('real.png')
plt.show()
