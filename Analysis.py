import pandas as pd
import matplotlib.pyplot as plt
import sys

# Pfad zur CSV-Datei
csv_file = 'Results.csv'

# CSV-Daten laden, Trennzeichen ist ein Semikolon
try:
    df = pd.read_csv(csv_file, sep=';')
except FileNotFoundError:
    print(f"Datei {csv_file} wurde nicht gefunden.")
    sys.exit(1)

# Verfügbare Spalten ausgeben
print("Verfügbare Spalten in den Daten:")
print(df.columns.tolist())

# Erwarteter Spaltenname (genau so, wie in der CSV-Datei)
target_column = "Total Correct Pieces"

# Überprüfen, ob die Spalte existiert
if target_column not in df.columns:
    print(f"Die Spalte '{target_column}' wurde in den Daten nicht gefunden.")
    print("Bitte überprüfe den Spaltennamen in deiner CSV-Datei.")
    sys.exit(1)

# X-Achse: Zeilennummer (Index)
x = df.index

# Y-Achse: Anzahl der gefundenen korrekten Steine
y = df[target_column]

# Grafik erstellen
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-')
plt.ylabel(target_column)
plt.title('Anzahl der gefundenen korrekten Steine')

# X-Achse ohne Beschriftung
plt.xticks([])

plt.tight_layout()
plt.show()