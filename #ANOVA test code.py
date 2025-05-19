# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create the dataset for THD
data_thd = {
    'Test': ['Test 1'] * 15 + ['Test 2'] * 15 + ['Test 3'] * 15,
    'THD (%)': [
        2.63, 3.17, 2.25, 3.70, 2.83, 2.56, 2.94, 2.75, 2.63, 2.83,
        2.67, 2.78, 2.83, 2.67, 2.42,  # Test 1
        4.02, 4.50, 4.17, 3.57, 3.70, 4.05, 4.31, 3.78, 4.37, 4.13,
        4.08, 4.34, 4.02, 4.00, 3.95,  # Test 2
        6.47, 6.11, 6.50, 7.00, 6.76, 6.89, 6.19, 6.41, 6.32, 6.76,
        7.00, 6.89, 6.50, 6.11, 6.19   # Test 3
    ]
}

# Step 2: Convert the data into a DataFrame
df_thd = pd.DataFrame(data_thd)

# Step 3: Group data by test
grouped_thd = df_thd.groupby('Test')['THD (%)']

# Step 4: Calculate descriptive statistics
summary_thd = grouped_thd.agg(['mean', 'std', 'min', 'max'])
print("THD Descriptive Statistics (by Test)")
print(summary_thd)

# Step 5: Visualize THD distribution across test groups
plt.figure(figsize=(10, 6))
df_thd.boxplot(column='THD (%)', by='Test', grid=False, boxprops=dict(color="blue"), medianprops=dict(color="red"))
plt.title("THD Distribution by Test Group")
plt.suptitle("")  # Remove automatic title
plt.ylabel("THD (%)")
plt.xlabel("Test Groups")
plt.show()
