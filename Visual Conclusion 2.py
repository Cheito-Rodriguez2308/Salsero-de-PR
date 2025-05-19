import matplotlib.pyplot as plt
import seaborn as sns

# Style settings
sns.set(style="whitegrid")
plt.rcParams["font.family"] = "DejaVu Sans"

# Data
labels = ['Production Cost (USD)', '10-Year Savings (USD)']
prototype_values = [195, 1000]
traditional_values = [2195, 300]  # Updated traditional values

# Plot setup
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
x = range(len(labels))

# Bar plots
bars1 = ax.bar(x, traditional_values, width=bar_width, label='Traditional', color='lightgray')
bars2 = ax.bar([p + bar_width for p in x], prototype_values, width=bar_width, label='Prototype', color='skyblue')

# Axis formatting
ax.set_ylabel('USD')
ax.set_title('Economic Comparison: Traditional vs. Solar Chip Prototype')
ax.set_xticks([p + bar_width / 2 for p in x])
ax.set_xticklabels(labels)

# Legend (original position)
ax.legend(loc='upper right')

# Annotate bars
for i in range(len(x)):
    ax.text(x[i], traditional_values[i] + 50, f"${traditional_values[i]:,.0f}", ha='center', va='bottom', fontsize=10)
    ax.text(x[i] + bar_width, prototype_values[i] + 50, f"${prototype_values[i]:,.0f}", ha='center', va='bottom', fontsize=10)

# Summary text box (below the chart)
stat_text = (
    "✔️ ANOVA: p < 0.001 (Significant Improvement)\n"
    "✔️ MLR: R² = 0.95 (Strong Correlation)\n"
    "✔️ External Components Eliminated\n"
    "✔️ Production Cost: $75\n"
    "✔️ 10-Year Savings: $1,000"
)
props = dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='black', alpha=0.9)
ax.text(0.9, 1400, stat_text, fontsize=10, bbox=props, transform=ax.transData)

# Add space at bottom for the text box
plt.subplots_adjust(bottom=0.3)

# Show the plot
plt.tight_layout()
plt.show()
