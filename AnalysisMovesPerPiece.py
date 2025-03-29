import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import sys

# Pfad zur CSV-Datei (ggf. anpassen)
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

# Erwartete Spaltennamen für die Kennzahl MovesPerPiece
target_total    = "Total Correct Pieces"
target_sequence = "Sequence Length"

# Prüfen, ob beide Spalten vorhanden sind
for col in [target_total, target_sequence]:
    if col not in df.columns:
        print(f"Die Spalte '{col}' wurde nicht in den Daten gefunden.")
        sys.exit(1)

# Sicherstellen, dass beide Spalten als numerische Werte vorliegen
df[target_sequence] = pd.to_numeric(df[target_sequence], errors='coerce')
df[target_total] = pd.to_numeric(df[target_total], errors='coerce')

# Berechnung der Kennzahl: MovesPerPiece = Sequence Length / Total Correct Pieces
df['MovesPerPiece'] = df[target_sequence] / df[target_total]

# X-Achse: Zeilennummer (Index)
x = df.index

# Y-Achse: MovesPerPiece
y_moves = df['MovesPerPiece']

# Berechnung der Trendlinie mittels gleitendem Durchschnitt (Fenstergröße 100)
trend_moves = y_moves.rolling(window=100).mean()

# Plot erstellen
plt.figure(figsize=(10, 6))
plt.plot(x, y_moves, linestyle='-', label='MovesPerPiece Data')
plt.plot(x, trend_moves, color='red', linestyle='--', linewidth=3, label='Trend (100 rolling average)')
plt.xlabel('Index')
plt.ylabel('MovesPerPiece')
plt.title('Moves Per Piece Trend')
ax = plt.gca()
ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=10, integer=True))
plt.legend()
plt.tight_layout()
plt.show()