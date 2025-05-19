import matplotlib.pyplot as plt
import numpy as np

# Define time axis: 0 to 0.05 seconds
t = np.linspace(0, 0.05, 1000)

# Define waveforms for each test
# Test 1: 60.1 Hz, 12V peak-to-peak
v1 = 6 * np.sin(2 * np.pi * 60.1 * t)

# Test 2: 59.8 Hz, 11.8V peak-to-peak + slight jitter (simulated with phase mod)
v2 = 5.9 * np.sin(2 * np.pi * 59.8 * t + 0.05 * np.sin(2 * np.pi * 5 * t))

# Test 3: 59.2 Hz, 10.2V peak-to-peak + more distortion (simulated with amplitude mod)
v3 = (5.1 + 0.5 * np.sin(2 * np.pi * 120 * t)) * np.sin(2 * np.pi * 59.2 * t)

# Create subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

# Plot each waveform with colors and updated label positions
axs[0].plot(t, v1, color='blue', label='Test 1: 60.1 Hz, 12.0 V p-p')
axs[1].plot(t, v2, color='red', label='Test 2: 59.8 Hz, 11.8 V p-p')
axs[2].plot(t, v3, color='green', label='Test 3: 59.2 Hz, 10.2 V p-p')

# Titles and labels
axs[0].set_title('Test 1 Waveform')
axs[1].set_title('Test 2 Waveform')
axs[2].set_title('Test 3 Waveform')
for ax in axs:
    ax.set_ylabel('Voltage (V)')
    ax.grid(True)
    ax.legend(loc='upper right')

axs[2].set_xlabel('Time (s)')

plt.tight_layout()
plt.show()