import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = r"C:\Users\aarya\Desktop\AARYAN_PYTHON data visualisation\AARYAN_PYTHON\Diwali Sales Data.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Plot 1: Pie Chart - Total Sales by Zone
zone_sales = df.groupby('Zone')['Amount'].sum()
plt.figure(figsize=(8, 8))
plt.pie(zone_sales, labels=zone_sales.index, autopct='%1.1f%%', colors=sns.color_palette("Set3"))
plt.title('Total Sales by Zone')
plt.show()

# Plot 2: Pie Chart - Gender Distribution in Sales
gender_sales = df.groupby('Gender')['Amount'].sum()
plt.figure(figsize=(8, 8))
plt.pie(gender_sales, labels=gender_sales.index, autopct='%1.1f%%', colors=sns.color_palette("Set2"))
plt.title('Sales Distribution by Gender')
plt.show()

# Plot 3: Histogram - Age Distribution of Customers
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=10, kde=True, color='coral')
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Plot 4: Heatmap - Correlation Matrix
plt.figure(figsize=(8, 6))
corr_matrix = df[['Age', 'Orders', 'Amount']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# Plot 5: Bar Plot - Total Orders by State
state_orders = df.groupby('State')['Orders'].sum().nlargest(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=state_orders.values, y=state_orders.index, palette='Blues_d')
plt.title('Top 10 States by Total Orders')
plt.xlabel('Total Orders')
plt.ylabel('State')
plt.show()

# Plot 6: Bar Plot - Total Sales by Product Category
product_sales = df.groupby('Product_Category')['Amount'].sum().nlargest(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=product_sales.values, y=product_sales.index, palette='Oranges')
plt.title('Top 10 Product Categories by Sales')
plt.xlabel('Total Sales')
plt.ylabel('Product Category')
plt.show()

# Plot 7: Scatter Plot - Age vs Amount
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Amount', data=df, hue='Gender', palette='viridis', s=100, alpha=0.6)
plt.title('Scatter Plot of Age vs Purchase Amount')
plt.xlabel('Age')
plt.ylabel('Amount')
plt.show()

# Plot 8: Bar Plot - Total Sales by Occupation
occupation_sales = df.groupby('Occupation')['Amount'].sum().nlargest(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=occupation_sales.values, y=occupation_sales.index, palette='Purples')
plt.title('Top 10 Occupations by Sales')
plt.xlabel('Total Sales')
plt.ylabel('Occupation')
plt.show()
