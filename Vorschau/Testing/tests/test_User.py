import pytest
from users import User, Mitarbeiter

class TestUser:

    #2
    def setup_method(self, method):
        print(f"Setting Up {method}")
        self.simple_User = User("Timm","Gieger","timmgieger@abc.de")
        self.worker = Mitarbeiter(1234,"IT", "Timm", "Gieger", "timmgieger@workmail.de")


    #1
    def test_one(self):
        assert True
    #3
    def test_user(self):
        self.simple_User.login()
        assert self.simple_User.logged_in == True
        self.simple_User.logout()
        assert self.simple_User.logged_in == False
    #4
    def test_worker(self):
        self.worker.login()
        assert self.worker.logged_in == True
        assert self.worker.isworking == False
        self.worker.arbeiten()
        assert self.worker.isworking == True
        self.worker.feierabend()
        assert self.worker.isworking == False
        self.worker.logout()
        assert self.worker.logged_in == False

    #2
    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.simple_User
        del self.worker

