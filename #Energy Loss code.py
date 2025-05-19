#Energy Loss code

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create the dataset
data_energy_loss = {
    'Test': ['Test 1'] * 15 + ['Test 2'] * 15 + ['Test 3'] * 15,
    'V_Input (V)': [9] * 45,  # Constant input voltage from the battery
    'I_Input (A)': [
        10.1, 10.2, 10.0, 10.3, 10.2, 10.1, 10.2, 10.1, 10.0, 10.2,
        10.1, 10.0, 10.2, 10.3, 10.1,  # Test 1
        10.0, 9.9, 9.8, 10.1, 9.9, 9.8, 9.7, 9.9, 9.8, 9.7,
        9.9, 9.8, 9.7, 9.9, 9.8,  # Test 2
        9.5, 9.4, 9.3, 9.5, 9.4, 9.3, 9.2, 9.4, 9.3, 9.2,
        9.5, 9.4, 9.3, 9.2, 9.4   # Test 3
    ],
    'V_Output (V)': [
        12.0, 12.1, 11.9, 12.2, 12.0, 12.0, 12.1, 12.0, 11.9, 12.0,
        12.0, 12.1, 12.0, 12.2, 12.0,  # Test 1
        11.5, 11.4, 11.3, 11.5, 11.4, 11.3, 11.2, 11.4, 11.3, 11.2,
        11.4, 11.3, 11.2, 11.4, 11.3,  # Test 2
        10.5, 10.4, 10.3, 10.5, 10.4, 10.3, 10.2, 10.4, 10.3, 10.2,
        10.5, 10.4, 10.3, 10.2, 10.4   # Test 3
    ],
    'I_Output (A)': [
        9.8, 9.9, 9.7, 9.9, 9.8, 9.7, 9.8, 9.7, 9.6, 9.8,
        9.7, 9.6, 9.8, 9.9, 9.7,  # Test 1
        9.5, 9.4, 9.3, 9.5, 9.4, 9.3, 9.2, 9.4, 9.3, 9.2,
        9.4, 9.3, 9.2, 9.4, 9.3,  # Test 2
        9.0, 8.9, 8.8, 9.0, 8.9, 8.8, 8.7, 8.9, 8.8, 8.7,
        9.0, 8.9, 8.8, 8.7, 8.9   # Test 3
    ]
}

# Step 2: Convert the data into a DataFrame
df_energy_loss = pd.DataFrame(data_energy_loss)

# Step 3: Calculate input and output power
df_energy_loss['P_Input (W)'] = df_energy_loss['V_Input (V)'] * df_energy_loss['I_Input (A)']
df_energy_loss['P_Output (W)'] = df_energy_loss['V_Output (V)'] * df_energy_loss['I_Output (A)']

# Step 4: Calculate energy loss percentage
df_energy_loss['Energy Loss (%)'] = ((df_energy_loss['P_Input (W)'] - df_energy_loss['P_Output (W)']) / df_energy_loss['P_Input (W)']) * 100

# Step 5: Group by test and calculate descriptive statistics
grouped_energy_loss = df_energy_loss.groupby('Test')['Energy Loss (%)']
summary_energy_loss = grouped_energy_loss.agg(['mean', 'std', 'min', 'max'])
print("Energy Loss Descriptive Statistics (by Test)")
print(summary_energy_loss)

# Step 6: Visualize energy loss across tests
plt.figure(figsize=(10, 6))
df_energy_loss.boxplot(column='Energy Loss (%)', by='Test', grid=False, boxprops=dict(color="blue"), medianprops=dict(color="red"))
plt.title("Energy Loss Distribution by Test Group")
plt.suptitle("")  # Remove automatic title
plt.ylabel("Energy Loss (%)")
plt.xlabel("Test Groups")
plt.show()
