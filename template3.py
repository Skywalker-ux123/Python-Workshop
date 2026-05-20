import pandas as pd
import matplotlib.pyplot as plt

print("📊 Data Science Mini-Challenge")

# Imagine we have a simple dictionary of student data (usually this is a CSV!)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Math_Score": [85, 92, 78, 65, 98],
    "Science_Score": [90, 88, 80, 70, 95]
}

# 1. Load data into a Pandas DataFrame
df = pd.DataFrame(data)
print("Here is our raw dataset:\n", df)

# 2. Calculate Statistics
# TODO: Use pandas to find the average (mean) of the Math_Score column
average_math = "YOUR_CODE_HERE"
print(f"\nAverage Math Score: {average_math}")

# 3. Visualize the Data
# TODO: Use matplotlib to create a simple bar chart of Names vs Math_Score
plt.bar("YOUR_X_DATA_HERE", "YOUR_Y_DATA_HERE", color='skyblue')

plt.title("Student Math Scores")
plt.xlabel("Student")
plt.ylabel("Score")

# Show the plot
plt.show()