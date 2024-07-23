class User:
    def __init__(self, vorname, nachname, email):
        self.vorname = vorname
        self.nachname = nachname
        self.email = email
        self.logged_in = False

    def login(self):
        print("Logging In")
        self.logged_in = True

    def logout(self):
        print("Logging Out")
        self.logged_in = False


class Mitarbeiter(User):
    def __init__(self, personalnummer, abteilung, vorname, nachname, email):
        self.personalnummer = personalnummer
        self.abteilung = abteilung
        self.isworking = False
        super().__init__(vorname, nachname, email)

    def arbeiten(self):
        print("Arbeit läuft")
        self.isworking = True

    def feierabend(self):
        print("Arbeit wird beendet")
        self.isworking = False