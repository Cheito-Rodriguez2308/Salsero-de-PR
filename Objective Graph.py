import matplotlib.pyplot as plt
import numpy as np

# Sample data for a conceptual academic graph
components = ['Baseline Solar Cell', 'With Micro Capacitor', 'With Micro Converter', 'Integrated System']
efficiency = [15.2, 17.8, 18.3, 20.1]  # in percent
losses = [12.5, 10.1, 9.3, 7.4]  # in percent

x = np.arange(len(components))
width = 0.35

fig, ax1 = plt.subplots(figsize=(10, 6))

bar1 = ax1.bar(x - width/2, efficiency, width, label='Energy Conversion Efficiency (%)', color='skyblue')
bar2 = ax1.bar(x + width/2, losses, width, label='Energy Losses (%)', color='salmon')

# Labels and title
ax1.set_ylabel('Percentage (%)')
ax1.set_title('Impact of Internalized Energy Conversion on Solar Cell Chip Performance')
ax1.set_xticks(x)
ax1.set_xticklabels(components, rotation=15)
ax1.legend(loc='upper left')
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Annotate bars
for i in range(len(components)):
    ax1.text(x[i] - width/2, efficiency[i] + 0.5, f'{efficiency[i]}%', ha='center', va='bottom')
    ax1.text(x[i] + width/2, losses[i] + 0.5, f'{losses[i]}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()
