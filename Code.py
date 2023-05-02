import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('data.csv', index_col=0)

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Create the heatmap
heatmap = sns.heatmap(data, cmap='YlOrRd', ax=ax, linewidths=0.5, linecolor='gray', annot=True, fmt='d', cbar=True)

# Rotate the numbers 90 degrees in each cell
# for i, t in enumerate(heatmap.texts):
#         t.set_rotation(90)

# Customize the plot
ax.set_title('Gene numbers across chromosomes and genotypes')
ax.set_xlabel('Chromosomes')
ax.set_ylabel('Genotypes')
plt.xticks(rotation=90)

# Show the plot
plt.show()
