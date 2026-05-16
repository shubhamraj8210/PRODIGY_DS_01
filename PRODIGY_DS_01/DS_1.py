import matplotlib.pyplot as plt
import numpy as np

# Data from the image (India's Population Distribution by Age in 2022)
age_groups = ['0 to 20 Years', '21 to 64 Years', '65+ Years']
population_mn = [512, 807, 98]  # in millions
percentages = [36.1, 57.0, 6.9]
colors = ['#FFEB3B', '#2196F3', '#E91E63']  # Yellow, Blue, Pink matching your image

# Create figure
fig, ax = plt.subplots(figsize=(12, 6))

# Create horizontal bar chart (better for age groups comparison)
bars = ax.barh(age_groups, population_mn, color=colors, edgecolor='black', height=0.6)

# Add value labels on bars
for i, (bar, pop, pct) in enumerate(zip(bars, population_mn, percentages)):
    width = bar.get_width()
    ax.text(width + 20, bar.get_y() + bar.get_height()/2, 
            f'{pop} Mn\n({pct}%)', 
            ha='left', va='center', fontsize=11, fontweight='bold')

# Styling
ax.set_xlabel('Population (Millions)', fontsize=12, fontweight='bold')
ax.set_title("India's Population Distribution by Age in 2022\nTotal: 1.42 Billion | Median Age: 28", 
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlim(0, 1000)

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add gridlines
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()

# Print summary statistics
print(f"Total Population: {sum(population_mn)} Million")
print(f"Median Age: 28 years")
