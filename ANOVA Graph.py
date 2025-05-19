import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Data for ANOVA Summary
sources = ['Between Groups', 'Within Groups']
ss = [520.3, 276.45]
df = [2, 42]
ms = [260.15, 6.58]
f_stat = 38.54
p_val = "< 0.001"
total_ss = sum(ss)
eta_squared = ss[0] / total_ss  # Effect size

# Create the figure layout: 1x3 for SS, MS, F-distribution
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
plt.rcParams.update({'font.family': 'serif', 'font.size': 12})

# --- Plot 1: Sum of Squares ---
axes[0].bar(sources, ss, color=['#8C1C13', '#BF6B63'], edgecolor='black', linewidth=0.7)
axes[0].set_title('Sum of Squares (SS)')
axes[0].set_ylabel('SS Value')
axes[0].text(0, ss[0] + 20, f'{ss[0]:.2f}', ha='center')
axes[0].text(1, ss[1] + 20, f'{ss[1]:.2f}', ha='center')

# --- Plot 2: Mean Squares ---
axes[1].bar(sources, ms, color=['#4B6C9E', '#8FBAC8'], edgecolor='black', linewidth=0.7)
axes[1].set_title('Mean Squares (MS)')
axes[1].set_ylabel('MS Value')
axes[1].text(0, ms[0] + 5, f'{ms[0]:.2f}', ha='center')
axes[1].text(1, ms[1] + 0.5, f'{ms[1]:.2f}', ha='center')

# --- Plot 3: F-distribution ---
x = np.linspace(0, 10, 500)
f_dist = stats.f(df[0], df[1])
y = f_dist.pdf(x)
axes[2].plot(x, y, color='black', label='F-distribution')
axes[2].axvline(f_stat, color='red', linestyle='--', label=f'Observed F = {f_stat:.2f}')
axes[2].fill_between(x, 0, y, where=(x > f_stat), color='red', alpha=0.3)
axes[2].set_title('F-distribution with Critical Region')
axes[2].set_xlabel('F-value')
axes[2].set_ylabel('Probability Density')
axes[2].legend()

# Add a textbox with stats
stats_text = (f"df (Between) = {df[0]}\n"
              f"df (Within) = {df[1]}\n"
              f"F-statistic = {f_stat:.2f}\n"
              f"p-value = {p_val}\n"
              f"η² (Effect size) = {eta_squared:.3f}")
axes[2].text(0.95, 0.95, stats_text, transform=axes[2].transAxes,
             verticalalignment='top', horizontalalignment='right',
             bbox=dict(boxstyle='round', facecolor='whitesmoke', edgecolor='gray'))

# Layout and display
fig.suptitle('One-Way ANOVA Summary Visualization', fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
