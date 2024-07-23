class Konto:
    def __init__(self, iban: str) -> None:
        self.__iban: str
        self.__iban = iban
        self.__kontostand: float
        self.__kontostand = 0

    @property
    def kontostand(self) -> float:
        return self.__kontostand

    def einzahlen(self, betrag: float) -> None:
        self.__kontostand += betrag

    def auszahlen(self, betrag: float) -> bool:
        if (self.__kontostand - betrag) >= 0:
            self.__kontostand -= betrag
            return True
        else:
            return False


class Privatkonto(Konto):

    def __init__(self, iban, vorname: str, nachname: str) -> None:
        super().__init__(iban)
        self.__vorname: str
        self.__vorname = vorname
        self.__nachname: str
        self.__nachname = nachname

    @property
    def privatkundenname(self) -> str:
        return self.__vorname + " " + self.__nachname


class Geschaeftskonto(Konto):
    def __init__(self, iban, firmenname: str, verfuegungsrahmen: float) -> None:
        super().__init__(iban)
        self.__firmenname: str
        self.__firmenname = firmenname
        self.__verfuegungsrahmen: float
        self.__verfuegungsrahmen = verfuegungsrahmen

    @property
    def verfuegungsrahmen(self) -> float:
        return self.__verfuegungsrahmen

    @verfuegungsrahmen.setter
    def verfuegungsrahmen(self, verfuegungsrahmen):
        self.__verfuegungsrahmen = verfuegungsrahmen

    @property
    def firmenname(self) -> str:
        return self.__firmenname

    @firmenname.setter
    def firmenname(self, firmenname):
        self.__firmenname = firmenname

    def auszahlen(self, betrag: float) -> bool:
        if (betrag) > self.__verfuegungsrahmen:
            print("Verfügungsrahmen reicht nicht aus")
            return False
        else:
            return super().auszahlen(betrag)