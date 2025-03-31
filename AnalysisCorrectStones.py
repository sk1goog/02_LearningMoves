import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import sys

# Path to the CSV file (adjust if necessary)
csv_file = 'Results.csv'

# Load CSV data; the delimiter is a semicolon
try:
    df = pd.read_csv(csv_file, sep=';')
except FileNotFoundError:
    print(f"File {csv_file} not found.")
    sys.exit(1)

# Print available columns in the data
print("Available columns in the data:")
print(df.columns.tolist())

# Expected column name (exactly as in the CSV file)
target_column = "Total Correct Pieces"

# Check if the target column exists
if target_column not in df.columns:
    print(f"The column '{target_column}' was not found in the data.")
    print("Please check the column name in your CSV file.")
    sys.exit(1)

# X-axis: Row number (index)
x = df.index

# Y-axis: Total Correct Pieces
y = df[target_column]

# Calculate the trend line using a rolling average over 100 values
trend = y.rolling(window=100).mean()

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, linestyle='-', label='Data')  # Line plot without data markers
plt.plot(x, trend, color='red', linestyle='-', linewidth=2, label='Trend (100 rolling average)')

plt.ylabel(target_column)
plt.title('Number of Correct Pieces Found')

# Set x-axis tick labels at readable intervals using MaxNLocator (maximum 10 ticks)
ax = plt.gca()
ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=10, integer=True))

plt.legend()
plt.tight_layout()
plt.show()