#Aufgabenstellung:
#Testen Sie alle Funktionalitäten der Konto-Klassen ähnlich wie in der Übung zur
#Objektorientierung mit dem unittest-modul.
#Folgende Testcases sollten abgedeckt werden:
#- Erstellen Sie ein Privatkonto und ein Geschäftskonto (das Geschäftskonto soll einen verfuegungsrahmen von 5000 € haben)
#- Zahlen Sie jeweils 5000 und 100000 Euro in die Konten ein
#- Lassen Sie sich den Kontostand ausgeben
#- lassen Sie sich 2000 und 10000 Euro auszahlen (Was fehlt eventuell noch in der Klasse Konto?)
#- Ändern Sie den Firmennamen des Geschäftskontos

import unittest
from konto import Privatkonto, Geschaeftskonto

class Konto_Test(unittest.TestCase):
    def setUp(self):
        self.konto1 = Privatkonto(12345, "Timm", "Gieger")
        self.konto2 = Geschaeftskonto(23456, "GeekIT Data Solutions", 5000)


    def test_cases(self):
        self.konto1.einzahlen(5000)
        self.konto2.einzahlen(100000)

        self.assertEqual(self.konto1.kontostand, 5000)
        self.assertEqual(self.konto2.kontostand, 100000)

        self.konto1.auszahlen(2000)
        self.konto2.auszahlen(10000)

        self.assertEqual(self.konto1.kontostand, 3000)
        self.assertEqual(self.konto2.kontostand, 100000)

        self.konto2.firmenname = "GeekIT"
        self.assertEqual(self.konto2.firmenname, "GeekIT")

    def tearDown(self):
        del self.konto1
        del self.konto2

if __name__ == '__main__':
    unittest.main()
