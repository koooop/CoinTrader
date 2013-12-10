class Wallet(object):
    """Wallet!!!"""

    def __init__(self):
        self.money = {}

    def getCurNames(self):
        return self.money.keys()

    def getCurrency(self, name):
        return self.money[name][0]

    def addCurrency(self, name, currency, balance):
        self.money[name] = [currency, balance]

    def getTotalValBTC(self):
        total = 0
        for (name, entry) in self.money.items():
            total += self.getBalanceBTC(name)
        return total

    def withdraw(self, name, val):
        """withdraw given val of money (in btc) of given currency"""
        self.money[name][1] -= val / self.money[name][0].getCurrentExchangeRate()

    def deposit(self, name, val):
        """deposit given val of money (in btc) of given currency"""
        self.money[name][1] += val / self.money[name][0].getCurrentExchangeRate()

    def getBalanceBTC(self, name):
        return self.money[name][1] * self.money[name][0].getCurrentExchangeRate()

    def transfer(self, from_name, to_name, val):
       """Transfer given val of currency from one accont to another, val is in bitcoins
       Returns: "actually transfered amount" = (val - balance if val > balance, 0 otherwise)"""

       if self.getBalanceBTC(from_name) >= val:
           self.withdraw(from_name, val)
           self.deposit(to_name, val)
           return val
       else:
           transfer = self.getBalanceBTC(from_name)
           self.withdraw(from_name, transfer)
           self.deposit(to_name, transfer)
           return transfer

    def __str__(self):
        output = ""
        for (name, entry) in self.money.items():
            output += "{0} - {1} ({2} BTC)\n".format(name, entry[1], self.getBalanceBTC(name))
        output += "TOTAL: {0} BTC\n".format(self.getTotalValBTC())
        return output

