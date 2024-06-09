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
def get_product_price(product):
    """Gibt den Preis für das gegebene Produkt zurück."""
    return preisliste.get(product, 0)

def calculate_total_cost(order):
    """Berechnet die Gesamtkosten einer Bestellung."""
    total_cost = 0
    for product in order:
        total_cost+= (get_product_price(product))
        #total_cost = sum(get_product_price(product) for product in order)
    return total_cost

def apply_discount(total_cost, discount_percentage):
    """Wendet den Rabatt auf die Gesamtkosten an und gibt den neuen Gesamtbetrag zurück."""
    discount_amount = total_cost * (discount_percentage / 100)
    return total_cost - discount_amount


def generate_receipt(order, discount_percentage):
    """Generiert eine Bestellbestätigung."""
    receipt = []
    total_cost_before_discount = calculate_total_cost(order)

    for product in order:
        price = get_product_price(product)
        receipt.append(f"{product}: {price:.2f} €")

    total_cost_after_discount = apply_discount(total_cost_before_discount, discount_percentage)
    discount_amount = total_cost_before_discount - total_cost_after_discount

    receipt.append(f"\nGesamtkosten vor Rabatt: {total_cost_before_discount:.2f} €")
    receipt.append(f"Rabatt: {discount_amount:.2f} €")
    receipt.append(f"Gesamtkosten nach Rabatt: {total_cost_after_discount:.2f} €")

    return "\n".join(receipt)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    bestellung = ["Apfel", "Banane", "Orange", "Trauben"]
    rabatt = 10  # 10% Rabatt

    ##Ihr Code
    # Generiere und drucke die Bestellbestätigung
    print(generate_receipt(bestellung, rabatt))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
