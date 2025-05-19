import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Data
df = pd.DataFrame({
    "Temperature": [32]*15 + [36]*15 + [40]*15,
    "THD": [2.63, 3.17, 2.25, 3.70, 2.83, 2.56, 2.94, 2.75, 2.63, 2.83, 2.67, 2.78, 2.83, 2.67, 2.42,
            3.57, 4.02, 3.70, 4.50, 4.17, 4.02, 4.05, 4.31, 3.70, 3.78, 4.37, 4.13, 4.08, 3.70, 4.34,
            6.47, 6.11, 6.50, 7.00, 6.76, 6.89, 6.19, 6.41, 6.32, 6.76, 7.00, 6.89, 6.50, 6.11, 6.19],
    "Duration": [10]*15 + [30]*15 + [60]*15,
    "PCE": [79.75, 77.68, 81.35, 76.60, 79.01, 79.89, 78.57, 79.24, 79.75, 79.01, 79.57, 79.16, 79.01, 79.57, 80.43,
            67.85, 65.88, 67.60, 64.88, 66.29, 65.88, 65.77, 64.77, 67.60, 67.30, 64.53, 65.60, 65.80, 67.60, 64.65,
            50.17, 51.89, 50.00, 48.05, 49.03, 48.48, 51.52, 50.57, 50.93, 49.03, 48.05, 48.48, 50.00, 51.89, 51.52]
})

# Set up figure
fig, axes = plt.subplots(3, 3, figsize=(18, 14))
sns.set(style="whitegrid")

# Panel a: Correlation heatmap
corr_matrix = df[["Temperature", "THD", "Duration"]].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=axes[0,0])
axes[0,0].set_title("a. Correlation Matrix")

# Panel b1: PCE ~ Temperature
model_temp = sm.OLS(df["PCE"], sm.add_constant(df["Temperature"])).fit()
sns.regplot(x="Temperature", y="PCE", data=df, ax=axes[0,1], color='orange')
axes[0,1].set_title("b1. PCE ~ Temperature")
axes[0,1].text(0.05, 0.9, f"coef = {model_temp.params[1]:.2f}", transform=axes[0,1].transAxes)

# Panel b2: PCE ~ THD
model_thd = sm.OLS(df["PCE"], sm.add_constant(df["THD"])).fit()
sns.regplot(x="THD", y="PCE", data=df, ax=axes[0,2], color='dodgerblue')
axes[0,2].set_title("b2. PCE ~ THD")
axes[0,2].text(0.05, 0.9, f"coef = {model_thd.params[1]:.2f}", transform=axes[0,2].transAxes)

# Panel b3: PCE ~ Duration
model_dur = sm.OLS(df["PCE"], sm.add_constant(df["Duration"])).fit()
sns.regplot(x="Duration", y="PCE", data=df, ax=axes[1,0], color='mediumseagreen')
axes[1,0].set_title("b3. PCE ~ Duration")
axes[1,0].text(0.05, 0.9, f"coef = {model_dur.params[1]:.2f}", transform=axes[1,0].transAxes)

# Partial regression: Temperature (controlling for THD & Duration)
resid_y = sm.OLS(df["PCE"], sm.add_constant(df[["THD", "Duration"]])).fit().resid
resid_x = sm.OLS(df["Temperature"], sm.add_constant(df[["THD", "Duration"]])).fit().resid
sns.regplot(x=resid_x, y=resid_y, ax=axes[1,1], color='orange')
axes[1,1].set_title("c1. Partial Effect: Temp | THD, Dur")
axes[1,1].set_xlabel("Temp residuals")
axes[1,1].set_ylabel("PCE residuals")

# Partial regression: THD (controlling for Temp & Duration)
resid_y2 = sm.OLS(df["PCE"], sm.add_constant(df[["Temperature", "Duration"]])).fit().resid
resid_x2 = sm.OLS(df["THD"], sm.add_constant(df[["Temperature", "Duration"]])).fit().resid
sns.regplot(x=resid_x2, y=resid_y2, ax=axes[1,2], color='dodgerblue')
axes[1,2].set_title("c2. Partial Effect: THD | Temp, Dur")

# Partial regression: Duration (controlling for Temp & THD)
resid_y3 = sm.OLS(df["PCE"], sm.add_constant(df[["Temperature", "THD"]])).fit().resid
resid_x3 = sm.OLS(df["Duration"], sm.add_constant(df[["Temperature", "THD"]])).fit().resid
sns.regplot(x=resid_x3, y=resid_y3, ax=axes[2,0], color='seagreen')
axes[2,0].set_title("c3. Partial Effect: Duration | Temp, THD")

# Actual vs predicted PCE
model_all = sm.OLS(df["PCE"], sm.add_constant(df[["Temperature", "THD", "Duration"]])).fit()
df["PCE_pred"] = model_all.predict(sm.add_constant(df[["Temperature", "THD", "Duration"]]))
sns.scatterplot(x="PCE", y="PCE_pred", data=df, ax=axes[2,1], color='purple')
axes[2,1].plot([df["PCE"].min(), df["PCE"].max()], [df["PCE"].min(), df["PCE"].max()], 'k--')
axes[2,1].set_title("d. Actual vs Predicted PCE")

# Empty subplot (for symmetry)
axes[2,2].axis('off')

plt.tight_layout()
plt.show()
