# Import necessary libraries
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Step 1: Create the dataset
data_mlr = {
    'Temperature (°C)': [32] * 15 + [36] * 15 + [40] * 15,
    'THD (%)': [
        2.63, 3.17, 2.25, 3.70, 2.83, 2.56, 2.94, 2.75, 2.63, 2.83,
        2.67, 2.78, 2.83, 2.67, 2.42,  # Test 1
        4.02, 4.50, 4.17, 3.57, 3.70, 4.05, 4.31, 3.78, 4.37, 4.13,
        4.08, 4.34, 4.02, 4.00, 3.95,  # Test 2
        6.47, 6.11, 6.50, 7.00, 6.76, 6.89, 6.19, 6.41, 6.32, 6.76,
        7.00, 6.89, 6.50, 6.11, 6.19   # Test 3
    ],
    'Duration (min)': [10] * 15 + [30] * 15 + [60] * 15,
    'PCE (%)': [
        80.00, 74.36, 81.35, 76.60, 79.01, 79.89, 78.57, 79.24, 79.75, 79.01,
        79.57, 79.16, 79.01, 79.57, 80.43,  # Test 1
        69.60, 64.88, 66.29, 71.43, 69.05, 65.77, 64.77, 67.30, 64.53, 65.60,
        65.80, 64.65, 65.88, 65.99, 66.17,  # Test 2
        50.31, 51.89, 50.00, 48.05, 49.03, 48.48, 51.52, 50.57, 50.93, 49.03,
        48.05, 48.48, 50.00, 51.89, 51.52   # Test 3
    ]
}
# Step 2: Convert the data into a DataFrame
df_mlr = pd.DataFrame(data_mlr)

# Step 3: Define independent and dependent variables
# Independent variables (Temperature, THD, Duration)
X = df_mlr[['Temperature (°C)', 'THD (%)', 'Duration (min)']]
X = sm.add_constant(X)  # Adds an intercept term to the model

# Dependent variable (PCE)
y = df_mlr['PCE (%)']

# Step 4: Fit the regression model
model = sm.OLS(y, X).fit()

# Step 5: Display regression results
print("Multiple Linear Regression Results")
print(model.summary())

# Step 6: Visualize relationships between variables (optional)
plt.figure(figsize=(10, 6))

# Scatter plot for Temperature vs. PCE
plt.subplot(1, 3, 1)
plt.scatter(df_mlr['Temperature (°C)'], df_mlr['PCE (%)'], color='blue', alpha=0.7)
plt.title("Temperature vs. PCE")
plt.xlabel("Temperature (°C)")
plt.ylabel("PCE (%)")

# Scatter plot for THD vs. PCE
plt.subplot(1, 3, 2)
plt.scatter(df_mlr['THD (%)'], df_mlr['PCE (%)'], color='green', alpha=0.7)
plt.title("THD vs. PCE")
plt.xlabel("THD (%)")
plt.ylabel("PCE (%)")

# Scatter plot for Duration vs. PCE
plt.subplot(1, 3, 3)
plt.scatter(df_mlr['Duration (min)'], df_mlr['PCE (%)'], color='red', alpha=0.7)
plt.title("Duration vs. PCE")
plt.xlabel("Duration (min)")
plt.ylabel("PCE (%)")
plt.tight_layout()
plt.show()
