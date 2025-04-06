
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file (adjust path if necessary)
df = pd.read_csv("Results.csv", sep=";")

# Convert duration column from hh:mm:ss to seconds
df['Duration_seconds'] = pd.to_timedelta(df['Run Duration (hh:mm:ss)']).dt.total_seconds()

# Calculate rolling sum over 30 runs
df['Sum_30'] = df['Duration_seconds'].rolling(window=30).sum()

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Sum_30'], label="Rolling Sum (30 runs)")
plt.xlabel("Run Index")
plt.ylabel("Total Duration (seconds)")
plt.title("Rolling Total Duration over 30 Runs")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
