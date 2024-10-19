import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
from wordcloud import WordCloud

# 设置高 DPI 以提高图片质量
plt.rcParams['savefig.dpi'] = 1000
plt.rcParams['figure.dpi'] = 1000
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 读取数据
df = pd.read_csv('WANFANG.csv')

# 获取唯一的类别
categories = df['Category'].unique()

for category in categories:
    category_data = df[df['Category'] == category]  # 筛选当前类别的数据

    plt.figure(figsize=(10, 6))

    if category == "年份":
        # 如果类别是年份，绘制线性图
        sns.lineplot(x='Keyword', y='Count', data=category_data, marker='o')
        plt.title(f'{category} 趋势图')
        plt.xlabel('年份')
        plt.ylabel('数量')
        plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))  # 确保 Y 轴是整数

    elif category == "文献来源":
        # 如果类别是文献来源，绘制扇形图
        plt.pie(category_data['Count'], labels=category_data['Keyword'], autopct='%1.1f%%', startangle=90)
        plt.axis('equal')  # 保证饼图是圆形
        plt.title(f'{category} 分布图')

    elif category == "主题":
        # 如果类别是主题，绘制词云
        wordcloud = WordCloud(width=800, height=400, background_color='white', font_path='simhei.ttf').generate(' '.join(category_data['Keyword']))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')  # 不显示坐标轴
        plt.title(f'{category} 词云图')

    else:
        # 其他类别绘制条形图
        sns.barplot(x='Keyword', y='Count', data=category_data)
        plt.title(f'{category} 分布图')
        plt.xticks(rotation=45)
        plt.xlabel('关键词')
        plt.ylabel('数量')
        plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))  # 确保 Y 轴是整数

    plt.tight_layout()  # 自动调整布局
    plt.show()
