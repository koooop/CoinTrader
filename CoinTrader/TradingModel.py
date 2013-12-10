class TradingModel(object):
    """Trading Model"""

    def __init__(self, unit, period, key_factor, buy_distribution, sell_per):
        self.unit = unit
        self.period = period
        self.key_factor = key_factor
        self.buy_distribution = buy_distribution
        self.sell_per = sell_per

    def getUnit(self):
        return self.unit

    def getPeriod(self):
        return self.period

    def getKeyFactor(self):
        return self.key_factor

    def getBuyDistribution(self):
        return self.buy_distribution

    def getSellPer(self):
        return self.sell_per




