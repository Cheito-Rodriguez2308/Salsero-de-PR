import matplotlib.pyplot as plt
import numpy as np

# Crear carpetas para guardar los gráficos
output_folder = "/mnt/data/"
charts = []

# Gráfico 1: Pérdidas energéticas en sistemas tradicionales vs integrados
fig, ax = plt.subplots()
labels = ['Tradicional', 'Integrado']
losses = [30, 10]  # Pérdidas energéticas en porcentaje
ax.bar(labels, losses, color=['red', 'green'])
ax.set_title('Pérdidas Energéticas por Tipo de Sistema')
ax.set_ylabel('Pérdidas (%)')
ax.set_ylim(0, 35)
for i, v in enumerate(losses):
    ax.text(i, v + 1, f"{v}%", ha='center', fontweight='bold')
file_path_1 = output_folder + "perdidas_energeticas.png"
plt.savefig(file_path_1)
charts.append(file_path_1)
plt.close()

# Gráfico 2: Eficiencia de conversión (Tradicional vs Integrado)
fig, ax = plt.subplots()
efficiency = [70, 95]  # Eficiencia en porcentaje
ax.bar(labels, efficiency, color=['blue', 'orange'])
ax.set_title('Eficiencia de Conversión Energética')
ax.set_ylabel('Eficiencia (%)')
ax.set_ylim(0, 100)
for i, v in enumerate(efficiency):
    ax.text(i, v + 1, f"{v}%", ha='center', fontweight='bold')
file_path_2 = output_folder + "eficiencia_conversion.png"
plt.savefig(file_path_2)
charts.append(file_path_2)
plt.close()

# Gráfico 3: Calidad de la onda (forma de onda tradicional vs integrada)
x = np.linspace(0, 2 * np.pi, 1000)
wave_traditional = np.sin(x) + 0.3 * np.sin(3 * x)
wave_integrated = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, wave_traditional, label="Tradicional (Distorsionada)", linestyle="--", color="red")
ax.plot(x, wave_integrated, label="Integrado (Senoidal)", color="green")
ax.set_title("Calidad de la Onda AC")
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Amplitud")
ax.legend()
file_path_3 = output_folder + "calidad_onda.png"
plt.savefig(file_path_3)
charts.append(file_path_3)
plt.close()

# Gráfico 4: Distribución de temperatura
fig, ax = plt.subplots()
temperatures = [70, 50]  # Temperaturas máximas en °C
ax.bar(labels, temperatures, color=['purple', 'cyan'])
ax.set_title('Distribución de Temperatura')
ax.set_ylabel('Temperatura Máxima (°C)')
ax.set_ylim(0, 80)
for i, v in enumerate(temperatures):
    ax.text(i, v + 1, f"{v}°C", ha='center', fontweight='bold')
file_path_4 = output_folder + "temperatura_maxima.png"
plt.savefig(file_path_4)
charts.append(file_path_4)
plt.close()

charts