import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# 步骤1：加载数据
data = pd.read_csv('result_human/Salmon.csv')  # 替换为实际文件路径

# 步骤2：准备数据
X = data['Groundtruth'].values.reshape(-1, 1)  # 自变量（特征）
y = data['Salmon'].values                   # 因变量（目标）

# 步骤3：添加截距项并拟合模型
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

# 步骤4：计算预测区间
predictions = model.get_prediction(X)
pred_ci = predictions.conf_int(obs=True, alpha=0.05)  # 95%预测区间
lower, upper = pred_ci[:, 0], pred_ci[:, 1]

# 步骤5：识别异常点
data['is_outlier'] = (y < lower) | (y > upper)
outliers = data[data['is_outlier']]

# 步骤6：输出结果

print("="*50)
print(f"发现异常点数量: {len(outliers)}")
print("异常点详细信息：")
print(outliers[['Transcript', 'Groundtruth', 'Salmon']])
outliers.to_csv("abnormal_Salmon.csv", 
               columns=['Transcript', 'Groundtruth', 'Salmon', 'is_outlier'],
               index=False)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 正确显示负号cc
# 步骤7：可视化
plt.figure(figsize=(8,5))
plt.scatter(X[:,1], y, s=10, alpha=0.7)
plt.plot(X[:,1], model.predict(X), 'r-')
plt.xlim(0,2000)
plt.ylim(0,2000)

#filtered_outliers = outliers[(outliers['Groundtruth'] < 5000) & (outliers['Groundtruth'] > 1000)
#                             & (outliers['Salmon'] < 5000) & (outliers['Salmon'] > 1000)] # 筛选异常点
# 标注异常点名称

#for idx, row in filtered_outliers.iterrows():
#    plt.text(row['Groundtruth'], row['Salmon'], 
#             row['Transcript'], 
#             fontsize=9, ha='right', va='bottom',
#             color='red', weight='semibold')

plt.fill_between(X[:,1], lower, upper, color='grey', alpha=0.5, label='95% Confidence Interval')
plt.xlabel('Groundtruth(TPM)',fontsize=15)
plt.ylabel('Salmon(TPM)',fontsize=15)
plt.legend()
plt.savefig('Salmon.png',dpi=300, bbox_inches='tight')
plt.show()

groundtruth_percent = outliers['Groundtruth'].sum()/data['Groundtruth'].sum()
print("="*50)
print(f"{groundtruth_percent:.2f}")  # 保留两位小数
print("="*50)


groundtruth_percent = outliers['Salmon'].sum()/data['Salmon'].sum()
print("="*50)
print(f"{groundtruth_percent:.2f}")  # 保留两位小数
print("="*50)