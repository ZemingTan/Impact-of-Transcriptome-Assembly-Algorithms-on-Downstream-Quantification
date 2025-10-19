import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import numpy as np

# 读取CSV文件
df = pd.read_csv('exons/transcript_exon_counts_cufflinks.csv')

# 计算每个exon_count的出现次数并按索引排序
exon_counts = df['exon_count'].value_counts().sort_index()

# 创建图形和主坐标轴
fig, ax1 = plt.subplots(figsize=(8, 4))

# 绘制条形图
bars = ax1.bar(exon_counts.index, exon_counts.values, 
               color='skyblue', edgecolor='black', 
               alpha=0.7, width=0.8)
ax1.set_xlabel('Exon Count', fontsize=10)
ax1.set_ylabel('Number of Transcripts', color='skyblue', fontsize=10)
ax1.tick_params(axis='y', labelcolor='skyblue')
ax1.set_xticks(exon_counts.index)  # 确保每个exon_count都有刻度标签
ax1.grid(True, linestyle='--', alpha=0.6)

# 计算概率密度曲线
data = df['exon_count'].values
kde = gaussian_kde(data)
# 可调整带宽以优化曲线平滑度
# kde.set_bandwidth(bw_method=kde.factor * 0.5)

# 生成横坐标范围
x_min = max(data.min() - 1, 0)  # 确保最小值不小于0
x_max = data.max() + 1
x = np.linspace(x_min, x_max, 1000)

# 计算密度并缩放到与计数相同的量纲
density = kde(x) * len(data)  # 使得曲线下面积等于总样本数

# 创建次坐标轴并绘制密度曲线
ax2 = ax1.twinx()
line = ax2.plot(x, density, color='orange', 
                linewidth=2, label='Density Curve')
ax2.set_ylabel('Probability Density (scaled)', color='orange', fontsize=10)
ax2.tick_params(axis='y', labelcolor='orange')

# 添加图例和标题
fig.legend([bars, line[0]], ['Transcript Count', 'Density Curve'], 
           loc='upper right', bbox_to_anchor=(0.88, 0.88),fontsize=10)

ax1.tick_params(axis='x', labelsize=8)  # 设置刻度标签字号
plt.tight_layout()
plt.savefig('Bar_Cufflinks.png',dpi=300, bbox_inches='tight')
plt.show()