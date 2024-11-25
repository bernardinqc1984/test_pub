import matplotlib.pyplot as plt
import numpy as np

# Data for the comparison
categories = [
    "Implementation Difficulty",
    "Complexity",
    "Resource Efficiency",
    "Scalability",
    "Performance",
    "Time to Deploy",
    "Automation Ease",
    "Maintenance Simplicity",
    "Cost Efficiency",
    "Flexibility",
    "Resilience",
]

bare_metal_scores = [7, 8, 9, 5, 9, 6, 5, 7, 7, 6, 5]
virtualization_scores = [5, 6, 7, 9, 6, 9, 8, 9, 6, 9, 8]

# Convert data for radar chart
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
bare_metal_scores += bare_metal_scores[:1]  # Close the loop
virtualization_scores += virtualization_scores[:1]  # Close the loop
angles += angles[:1]  # Close the loop

# Radar chart setup
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(angles, bare_metal_scores, color="blue", alpha=0.25, label="Bare Metal")
ax.fill(angles, virtualization_scores, color="green", alpha=0.25, label="Virtualization")
ax.plot(angles, bare_metal_scores, color="blue", linewidth=2)
ax.plot(angles, virtualization_scores, color="green", linewidth=2)

# Add labels for categories
ax.set_yticks(range(1, 11, 2))
ax.set_yticklabels([])  # Customize Y-axis labels if needed
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10)

# Add legend and title
ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
ax.set_title("Comparative Analysis: OpenShift on Bare Metal vs Virtualization", y=1.1, fontsize=14)

# Show and save the plot
plt.show()
