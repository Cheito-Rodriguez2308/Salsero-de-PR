import matplotlib.pyplot as plt
import seaborn as sns

# Style settings
sns.set(style="whitegrid")
plt.rcParams["font.family"] = "DejaVu Sans"

# Data
labels = ['PCE (%)', 'Energy Loss (%)']
prototype_values = [79.3, 20]
traditional_values = [65, 30]

# Plot comparison bars
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
x = range(len(labels))

bars1 = ax.bar(x, traditional_values, width=bar_width, label='Traditional', color='lightgray')
bars2 = ax.bar([p + bar_width for p in x], prototype_values, width=bar_width, label='Prototype', color='skyblue')

# Add labels
ax.set_ylabel('Performance Metrics')
ax.set_title('Performance Comparison: Traditional vs. Solar Chip Prototype')
ax.set_xticks([p + bar_width / 2 for p in x])
ax.set_xticklabels(labels)
ax.legend()

# Annotate bars
for i in range(len(x)):
    ax.text(x[i], traditional_values[i] + 1, f"{traditional_values[i]}%", ha='center', va='bottom', fontsize=10)
    ax.text(x[i] + bar_width, prototype_values[i] + 1, f"{prototype_values[i]}%", ha='center', va='bottom', fontsize=10)

# Text box for statistical results
stat_text = (
    "✔️ ANOVA: p < 0.001 (Significant Improvement)\n"
    "✔️ MLR: R² = 0.95 (Strong Correlation)\n"
    "✔️ External Components Eliminated\n"
    "✔️ Production Cost: $75\n"
    "✔️ 10-Year Savings: $1,000"
)

props = dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='black', alpha=0.9)
ax.text(1.05, 55, stat_text, fontsize=10, bbox=props)

# Final layout
plt.tight_layout()
plt.show()
