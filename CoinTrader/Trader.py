import Clock
import TradingModel
import datetime

class Trader(object):
    """description of class"""

    def __init__(self, wallet, trading_model):
        self.wallet = wallet
        self.trading_model = trading_model
        self.last_trade = None

    def update(self):
        current_time = Clock.Clock.getCurrentTime()
        if not self.last_trade or current_time - datetime.timedelta(minutes=self.trading_model.getUnit()) > self.last_trade:
            currencies = self.getOrderedCurNames()
            for buy_index, buy_val in enumerate(self.getBuyAmountBTC()):
                to_buy_amount = buy_val
                while to_buy_amount > 0 and len(currencies) > buy_index:
                    if self.wallet.getBalanceBTC(currencies[-1]) == 0:
                        currencies.pop()
                    else:
                        transfered = self.wallet.transfer(currencies[-1],
                                             currencies[buy_index],
                                             to_buy_amount)
                        to_buy_amount -= transfered
            self.last_trade = current_time

    def getOrderedCurNames(self):
        result = list(self.wallet.getCurNames())
        result.sort(key = lambda x: self.wallet.getCurrency(x).getKeyFactorValue(self.trading_model.unit, self.trading_model.period, self.trading_model.key_factor), reverse=True)
        return result

    def getSellAmountBTC(self):
        return self.wallet.getTotalValBTC() * (self.trading_model.getSellPer()/100.0)

    def getBuyAmountBTC(self):
        result = []
        for entry in self.trading_model.getBuyDistribution():
            result.append(self.getSellAmountBTC() * (entry/100.0))
        return result