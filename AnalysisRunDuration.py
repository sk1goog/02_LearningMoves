import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import sys

# Path zur CSV-Datei (ggf. anpassen)
csv_file = 'Results.csv'

# CSV-Daten laden; der Trenner ist ein Semikolon
try:
    df = pd.read_csv(csv_file, sep=';')
except FileNotFoundError:
    print(f"File {csv_file} not found.")
    sys.exit(1)

# Verfügbare Spalten anzeigen
print("Available columns in the data:")
print(df.columns.tolist())

# Erwarteter Spaltenname (exakt so, wie in der CSV-Datei)
target_column = "Run Duration (hh:mm:ss)"

# Prüfen, ob die Zielspalte existiert
if target_column not in df.columns:
    print(f"The column '{target_column}' was not found in the data.")
    print("Please check the column name in your CSV file.")
    sys.exit(1)

# Konvertieren der Zeitspalte von hh:mm:ss in timedelta und anschließend in Sekunden
df['Duration_seconds'] = pd.to_timedelta(df[target_column]).dt.total_seconds()

# X-Achse: Zeilennummer (Index)
x = df.index

# Y-Achse: Run Duration in Sekunden
y = df['Duration_seconds']

# Berechnung der Trendlinie mittels gleitendem Durchschnitt über 100 Werte
trend = y.rolling(window=100).mean()

# Plot erstellen
plt.figure(figsize=(10, 6))
plt.plot(x, y, linestyle='-', label='Data')  # Linienplot ohne Datenmarker
plt.plot(x, trend, color='red', linestyle='--', linewidth=3, label='Trend (100 rolling average)')

plt.xlabel('Index')
plt.ylabel('Run Duration (seconds)')
plt.title('Run Duration Trend')

# x-Achsen-Beschriftungen in lesbaren Intervallen (max. 10 Ticks)
ax = plt.gca()
ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=10, integer=True))

plt.legend()
plt.tight_layout()
plt.show()