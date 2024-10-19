import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False  


data = {
    '年份': [2022, 2019, 2018, 2017, 2016, 2015, 2014],
    'Count': [1, 1, 1, 2, 4, 2, 1],
    'qikan_count': [1, 1, 1, 0, 1, 1, 0],
    'huiyi_count': [0, 0, 0, 2, 3, 1, 1]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))

sns.lineplot(x='年份', y='Count', data=df, marker='o', label='总数量')

sns.lineplot(x='年份', y='qikan_count', data=df, marker='o', label='期刊论文数量')

# 绘制会议论文数量趋势线
sns.lineplot(x='年份', y='huiyi_count', data=df, marker='o', label='会议论文数量')

# 设置图表标题和坐标轴标签
plt.title('年份趋势图')
plt.xlabel('年份')
plt.ylabel('数量')

# 确保 X 轴显示所有年份
plt.xticks(df['年份'])

# 设置 Y 轴显示整数
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# 添加图例
plt.legend()

# 显示图表
plt.tight_layout()
plt.show()
