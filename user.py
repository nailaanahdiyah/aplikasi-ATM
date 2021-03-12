from kartu_atm import kartuATM

class User :
    def __init__(self, id, userPin = 1234, userSaldo = 10000):
        self.id = id
        self.userPin = userPin
        self.userSaldo = userSaldo

    def cekId(self):
        return self.id

    def cekPin(self):
        return self.userPin

    def cekSaldo(self):
        return self.userSaldo

    def debetProses(self, nominal):
        self.userSaldo -= nominal

    def simpanProses(self, nominal):
        self.userSaldo += nominal
