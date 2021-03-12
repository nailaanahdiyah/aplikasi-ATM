class kartuATM :
    def __init__(self, defaultPin, defaultSaldo) :
        self.defaultPin = defaultPin
        self.defaultSaldo = defaultSaldo

    def cekPinAwal(self) :
        return self.defaultPin

    def cekSaldoAwal(self) :
        return self.defaultSaldo
    
