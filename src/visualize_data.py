import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
data = pd.read_csv('data/cleaned_data.csv')

# Plot 1: Experiment Score vs Student ID
plt.figure()
plt.plot(data['student_id'], data['experiment_score'])
plt.xlabel('Student ID')
plt.ylabel('Experiment Score')
plt.title('Experiment Score vs Student ID')
plt.savefig('results/score_plot.png')

# Plot 2: Temperature vs Humidity
plt.figure()
plt.scatter(data['temperature'], data['humidity'])
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.title('Temperature vs Humidity')
plt.savefig('results/temp_humidity_plot.png')

print("Plots saved in results/ folder")

# Minor update for visualization PR