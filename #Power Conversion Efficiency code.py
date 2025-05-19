import pandas as pd

# Step 1: Create the dataset
data = {
    'Test': ['Test 1'] * 15 + ['Test 2'] * 15 + ['Test 3'] * 15,
    'PCE (%)': [
        80.00, 74.36, 81.35, 76.60, 79.01, 79.89, 78.57, 79.24, 79.75, 79.01,
        79.57, 79.16, 79.01, 79.57, 80.43,  # Test 1
        69.60, 64.88, 66.29, 71.43, 69.05, 65.77, 64.77, 67.30, 64.53, 65.60,
        65.80, 64.65, 65.88, 65.99, 66.17,  # Test 2
        50.31, 51.89, 50.00, 48.05, 49.03, 48.48, 51.52, 50.57, 50.93, 49.03,
        48.05, 48.48, 50.00, 51.89, 51.52   # Test 3
    ]
}

df = pd.DataFrame(data)

# Step 2: Group data by test
grouped = df.groupby('Test')['PCE (%)']

# Step 3: Calculate descriptive statistics
summary = grouped.agg(['mean', 'std', 'min', 'max'])
print("PCE Descriptive Statistics (by Test)")
print(summary)

# Step 4: Plot the PCE distribution 
import matplotlib.pyplot as plt

df.boxplot(column='PCE (%)', by='Test', grid=False)
plt.title("PCE Distribution by Test")
plt.suptitle("")  # Remove automatic title
plt.ylabel("PCE (%)")
plt.show()
