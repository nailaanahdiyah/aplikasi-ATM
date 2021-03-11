from atm_card import ATMCard

class Customer :
    def __init__(self, id, custPin = 1234, custBalance = 10000):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance

    def cekId(self):
        return self.id

    def cekPin(self):
        return self.custPin

    def cekBalance(self):
        return self.custBalance

    def debetProses(self, nominal):
        self.custBalance -= nominal

    def simpanProses(self, nominal):
        self.custBalance += nominal
