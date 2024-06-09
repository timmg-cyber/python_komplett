# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

### Aufgabenstellung:
# Sie arbeiten für einen Online-Shop, der verschiedene Produkte verkauft.
# Der Shop benötigt ein Python-Skript, das Bestellungen verwaltet
# und verschiedene Berechnungen durchführt. Ihre Aufgabe ist es,
# Funktionen zu schreiben, die dabei helfen, die Bestellungen zu verarbeiten.
# ###

### 1. Erstellen Sie eine Funktion die den Preis eines gegebenen Produkts zurückgibt.
# Verwenden Sie die dazu festgelegte Preisliste
# ###

### 2. Erstellen Sie eine Funktion die eine Bestellung (Liste von Produkten) entgegennimmt
# und die Gesamtkosten berechnet
# ###

### 3. Erstellen Sie eine Funktion, die den gegebenen Rabatt auf die Gesamtkosten anwendet
# und den neuen Gesamtbetrag zurückgibt.
# ###

### 4. Erstellen Sie eine Funktion, die eine Bestellbestätigung generiert. Die Bestätigung
# soll folgende Informationen enthalen:
# - Liste der Produkte mit Einzelpreisen
# - Gesamtkosten vor Rabatt
# - Rabattsumme
# - Gesamtkosten nach Rabatt
# ###

### Hinweis
# - Achten Sie darauf, dass Ihre Funktionen gut strukturiert und kommentiert sind.
# - Testen Sie Ihre Funktionen mit verschiedenen Bestellungen und Rabatten
# ###

global preisliste

preisliste = {
    "Apfel": 0.5,
    "Banane": 0.3,
    "Orange": 0.8,
    "Birne": 0.6,
    "Trauben": 1.5
}

## Ihr Code


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    bestellung = ["Apfel", "Banane", "Orange", "Trauben"]
    rabatt = 10  # 10% Rabatt


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
