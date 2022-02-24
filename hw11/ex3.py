import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("SampleSuperstore.csv")
print(data.head(5))
print(data.tail(5))
print(data.info())
print(data.describe())
print(data.isnull().sum())
print(data.duplicated().sum())
print(data.drop_duplicates())
for column in data.columns:
    print(f"Column {column}\n{data[column].value_counts()}")

print(data.nunique())
data.drop(["Country", "Postal Code"], axis=1, inplace=True)
plt.figure(figsize=(10, 10), dpi=80)
corr = data.corr()
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns,
            cmap='magma', annot=True)
plt.show()

sns.pairplot(data, diag_kind='kde', hue='Sub-Category')
plt.show()

plt.figure(figsize=(15, 10), dpi=80)
sns.barplot(x=data['State'], y=data['Profit'], palette='pastel')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(15, 10), dpi=80)
sns.countplot(x='State', data=data)
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(15, 10), dpi=80)
sns.barplot(x=data['Sub-Category'], y=data['Profit'], palette='pastel')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(10, 8), dpi=80)
sns.lineplot(x='Discount', y='Profit', data=data,
             color='purple', label="Mean of profits for each discount")
sns.regplot(x='Discount', y='Profit', data=data,
            scatter=False, label="Regression line")
plt.legend()
plt.show()

plt.figure(figsize=(10, 8), dpi=80)
sns.lineplot(x='Quantity', y='Profit', data=data,
             color='purple', label="Mean of profits for each discount")
sns.regplot(x='Quantity', y='Profit', data=data,
            scatter=False, label="Regression line")
plt.legend()
plt.show()
