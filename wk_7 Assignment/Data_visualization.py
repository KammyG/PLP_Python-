
# Task 1: Load and Explore the Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris(as_frame=True)

# Convert to pandas DataFrame
df = iris.frame
print("✅ Iris dataset loaded successfully!\n")

# Display first few rows
print("--- First 5 rows ---")
print(df.head(), "\n")

# Structure of dataset
print("--- Info ---")
print(df.info(), "\n")

# Missing values check
print("--- Missing Values ---")
print(df.isnull().sum(), "\n")

# Clean dataset (Iris has no missing values, but just in case)
df = df.dropna()

# Task 2: Basic Data Analysis
print("--- Statistical Summary ---")
print(df.describe(), "\n")

# Group by target (species) and compute mean of numerical columns
grouped = df.groupby("target").mean()
print("--- Grouped Mean by Species ---")
print(grouped, "\n")

# Map species target numbers to names
df['species'] = df['target'].map(dict(enumerate(iris.target_names)))

# Task 3: Data Visualization

# 1. Line Chart (Trend over index for sepal length)
plt.figure(figsize=(8,5))
plt.plot(df.index, df['sepal length (cm)'], color='blue')
plt.title("Line Chart: Sepal Length Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.show()

# 2. Bar Chart (Average petal length per species)
plt.figure(figsize=(8,5))
sns.barplot(x='species', y='petal length (cm)', data=df, ci=None, palette="viridis")
plt.title("Bar Chart: Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram (Distribution of sepal width)
plt.figure(figsize=(8,5))
plt.hist(df['sepal width (cm)'], bins=20, color='skyblue', edgecolor='black')
plt.title("Histogram of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot (Sepal length vs Petal length)
plt.figure(figsize=(8,5))
sns.scatterplot(
    x='sepal length (cm)', 
    y='petal length (cm)', 
    hue='species', 
    data=df,
    palette="deep",
    alpha=0.7
)
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
