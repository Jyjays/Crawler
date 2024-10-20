import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load the Excel file
df = pd.read_excel('WOS_data.xlsx', engine='openpyxl')

# 1. Line Trend Plot of Year Count
def plot_year_trend(df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Publication Years', y='Publication Years_Count', data=df)
    plt.title('Publication Count by Year')
    plt.xlabel('Publication Years')
    plt.ylabel('Count')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 2. Word Cloud of Major Concepts
def plot_wordcloud(df):
    # Convert the Major Concepts into a single string
    major_concepts = ' '.join(df['Major Concepts'].dropna().astype(str))

    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(major_concepts)

    # Display the word cloud
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Major Concepts')
    plt.show()

# 3. Histogram of Research Domains
def plot_research_domains_histogram(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Research Domains'], bins=15, kde=False)
    plt.xticks(rotation=90)
    plt.title('Histogram of Research Domains')
    plt.xlabel('Research Domains')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

# Call the plotting functions
plot_year_trend(df)
plot_wordcloud(df)
plot_research_domains_histogram(df)
