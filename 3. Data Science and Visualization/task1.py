import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 3. Data Science and Visualization

# Practice Task : 1 | Analyze a dataset and create visualizations (e.g., scatter plots, histograms, heatmaps).
def create_dataframe():
    df = pd.read_csv("3. Data Science and Visualization/student_performance.csv")
    return df
df = create_dataframe()

# Scatter Plots
plt.scatter(x=df["Study_Hours"], y=df["Final_Score"])
plt.title('Study Hours vs Final Score')
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.show()

# Scatter Plots
sns.scatterplot(x='Study_Hours', y='Final_Score', data=df)
plt.title('Study Hours vs Final Score')
plt.xlabel('Study Hours')
plt.ylabel('Final Score')
plt.show()

# Histograms
plt.hist(df['Final_Score'], bins=10, color='lightgreen', edgecolor='black')
plt.title("Distribution of Final Scores")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.show()

# Histograms
sns.histplot(df["Final_Score"], bins=10)
plt.title("Distribution of Final Scores")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.show()

numeric_data = df.drop(columns=["Student_Name", "Gender"])
corr_matrix = numeric_data.corr()

# Plot heatmap
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Heatmap of Student Performance Metrics")
plt.show()