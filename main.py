import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data.csv")
data.dropna(subset=['Year', 'Publisher'], inplace=True)
data['Year'] = data['Year'].astype(int)

top_global_sales = data.nlargest(10, 'Global_Sales')
plt.figure(figsize=(10, 6))
sns.barplot(x='Global_Sales', y='Name', data=top_global_sales, palette='viridis')
plt.title('Top 10 Games by Global Sales')
plt.xlabel('Global Sales (in millions)')
plt.ylabel('Game Title')
plt.tight_layout()
plt.savefig('images/top_10_global_sales.png')
plt.close()

sales_by_year = data.groupby('Year')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum()
plt.figure(figsize=(12, 6))
sales_by_year.plot(ax=plt.gca(), marker='o')
plt.title('Sales Trends Over the Years')
plt.xlabel('Year')
plt.ylabel('Sales (in millions)')
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('images/sales_trends_over_years.png')
plt.close()

genre_sales = data.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=genre_sales.values, y=genre_sales.index, palette='coolwarm')
plt.title('Global Sales by Genre')
plt.xlabel('Global Sales (in millions)')
plt.ylabel('Genre')
plt.tight_layout()
plt.savefig('images/global_sales_by_genre.png')
plt.close()

platform_sales = data.groupby('Platform')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
platform_sales = platform_sales.div(platform_sales.sum(axis=1), axis=0)
platform_sales = platform_sales.loc[platform_sales.sum(axis=1).nlargest(10).index]
platform_sales.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='Set3')
plt.title('Regional Sales Distribution by Platform (Top 10)')
plt.xlabel('Platform')
plt.ylabel('Proportion of Sales')
plt.tight_layout()
plt.savefig('images/regional_sales_by_platform.png')
plt.close()

if 'Critic_Score' in data.columns:
    data.dropna(subset=['Critic_Score'], inplace=True)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Critic_Score', y='Global_Sales', hue='Genre', data=data, palette='husl', alpha=0.8)
    plt.title('Critic Scores vs. Global Sales')
    plt.xlabel('Critic Score')
    plt.ylabel('Global Sales (in millions)')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.savefig('images/critic_scores_vs_sales.png')
    plt.close()

data['NA_vs_Global'] = data['NA_Sales'] / data['Global_Sales']
data['EU_vs_Global'] = data['EU_Sales'] / data['Global_Sales']
data['JP_vs_Global'] = data['JP_Sales'] / data['Global_Sales']
plt.figure(figsize=(12, 6))
sns.boxplot(data=data[['NA_vs_Global', 'EU_vs_Global', 'JP_vs_Global']], palette='pastel')
plt.title('Sales Proportion by Region')
plt.xlabel('Region')
plt.ylabel('Proportion of Global Sales')
plt.tight_layout()
plt.savefig('images/sales_proportion_by_region.png')
plt.close()
