import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set the visual style and context for a professional appearance
sns.set_style('whitegrid')
sns.set_context('talk')

# Generate realistic synthetic data for product performance
np.random.seed(42) # for reproducibility
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = np.random.randint(1000, 5000, size=len(products))
data = pd.DataFrame({'Product': products, 'Sales': sales})

# Create the figure with a specific size to control the output dimensions
plt.figure(figsize=(8, 8))

# Generate the bar plot using a professional color palette
barplot = sns.barplot(
    x='Sales',
    y='Product',
    data=data,
    palette='viridis'
)

# Set meaningful titles and labels for business context
plt.title('Product Sales Performance')
plt.xlabel('Sales (Units)')
plt.ylabel('Product')

# Save the chart to a file with specified dimensions (8 inches * 64 dpi = 512 pixels)
plt.savefig('chart.png', dpi=64, bbox_inches='tight')

plt.close()

print("chart.png with dimensions 512x512 has been successfully generated.")
