import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv(r'D:/tools/workplace/python_work/crawler/EI_source.csv')


# Show the first few rows of the dataset to understand its structure
print(df.head())

# Data Cleaning (if necessary)
df['Count'] = pd.to_numeric(df['Count'], errors='coerce')

# Sort the data by count (descending)
df_sorted = df.sort_values(by='Count', ascending=False)

# Plot a bar chart of the top 10 sources by count
plt.figure(figsize=(10, 6))
sns.barplot(x='Count', y='Source title', data=df_sorted.head(10), palette='viridis')
plt.title('Top 10 Sources by Count')
plt.xlabel('Count')
plt.ylabel('Source Title')
plt.tight_layout()
plt.show()

# Analyze the distribution of counts (histogram)
plt.figure(figsize=(10, 6))
sns.histplot(df['Count'], bins=20, kde=True)
plt.title('Distribution of Source Counts')
plt.xlabel('Count')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Analyze the total number of sources and the distribution of counts
total_sources = df['Source title'].nunique()
print(f"Total number of unique sources: {total_sources}")

# Summarize the data
summary_stats = df['Count'].describe()
print(summary_stats)
