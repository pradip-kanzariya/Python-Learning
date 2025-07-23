import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# # 12. Intro to Libraries

# Practice Task : 1 | Use Pandas to read and analyze a CSV file.
students_csv = pd.read_csv("task12_dir/students.csv")
students_csv["Total"] = students_csv['Math'] + students_csv['Science'] + students_csv['English']
students_csv["Avg"] = students_csv["Total"] / 3
print(students_csv)
print(students_csv[students_csv['Passed'] == 'Yes'])
print(f"Total Passed Students : {len(students_csv[students_csv['Passed'] == 'Yes'])}")
male_passed = len(students_csv.query("Gender == 'Male' and Passed == 'Yes'"))
female_passed = len(students_csv.query("Gender == 'Female' and Passed == 'Yes'"))
if male_passed > female_passed:
    print("From result highest passed gender is Male.")
elif male_passed == female_passed:
    print("From result Male and Female both are equal.")
else:
    print("From result highest passed gender is Female.")


# Practice Task : 2 | Create a bar chart using matplotlib.
students_csv.plot(kind='bar', x='Name', y='Total')
plt.ylim(0, 300)
plt.ylabel("Total")
plt.xlabel("Students")
plt.show()


# Extra Task :
# Practice Task : 3 | Analyze and visualize student performance using NumPy, Pandas, and Matplotlib.
student_maths_score = np.random.randint(1, 100, size=10)
student_science_score = np.random.randint(1, 100, size=10)
student_english_score = np.random.randint(1, 100, size=10)
students = np.array(['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'zab', 'cde'])

students_data = {
    'Name': students,
    'Maths': student_maths_score,
    'Science': student_science_score,
    'English': student_english_score,
}

df = pd.DataFrame(students_data)
df['Total'] = df['Maths'] + df['Science'] + df['English']
df['Average'] = df['Total'] / 3
df['Result'] = df['Average'].apply(lambda x: 'Pass' if x >= 50 else 'Fail')
print(df)
total_passed = len(df[df['Result'] == 'Pass'])
total_failed = len(df[df['Result'] == 'Fail'])
print(f"Student with the highest total :\n{df[df['Total'] == df['Total'].max()]}")
print(f"Total number of Passed students : {total_passed} and Failed students : {total_failed}")

# Bar chart :
df.plot(kind='bar', x='Name', y='Total')
plt.title('Students With Total Marks')
plt.xlabel("Students", fontsize=12)
plt.ylabel("Total", fontsize=12)
plt.tight_layout()
plt.show()


# Line chart :
fig, ax = plt.subplots(figsize=(12, 6))
df.plot(kind='line', x='Name', y=['Maths', 'Science', 'English'], marker='o', ax=ax)

# Set all student names on X-axis
ax.set_xticks(range(len(df)))
ax.set_xticklabels(df['Name'], rotation=45, fontsize=10)

# Set major Y ticks every 10
ax.set_yticks(np.arange(0, 101, 10))

# Add minor ticks (every 1 unit)
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))

# Format minor ticks: small lines only
ax.tick_params(axis='y', which='minor', length=4, color='gray')
ax.tick_params(axis='y', which='major', length=7, color='gray')

# Grid: major + minor y lines
ax.grid(which='major', axis='y', linestyle='--', linewidth=0.5, color='gray', alpha=0.6)
ax.grid(which='minor', axis='y', linestyle=':', linewidth=0.3, color='gray', alpha=0.5)

# Labels
plt.title('Subject-wise Student Scores', fontsize=14)
plt.xlabel('Student Name', fontsize=12)
plt.ylabel('Marks', fontsize=12)

plt.tight_layout()
plt.show()


# Pie chart :
# Count occurrences of Pass and Fail
result_counts = df['Result'].value_counts()
# Create pie chart
plt.pie(result_counts, labels=result_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Pass vs Fail')
plt.axis('equal')  # Keep the pie circular
plt.show()
