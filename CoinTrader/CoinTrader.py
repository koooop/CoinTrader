import DataProvider
import datetime
import Currency
import Wallet
import Clock
import Trader
import TradingModel

btc = Currency.BitCoin("BTC", None)



currencies_s = [["LTC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=ltc-btc&market=cryptsy"],
              ["NMC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=nmc-btc&market=cryptsy"],
              ["FTC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=ftc-btc&market=cryptsy"],
              ["PPC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=ppc-btc&market=cryptsy"],
              ["XMP", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=xpm-btc&market=cryptsy"],
              ["WDC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=wdc-btc&market=cryptsy"],
              ["TRC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=trc-btc&market=cryptsy"],
              ["ZET", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=zet-btc&market=cryptsy"],
              #["PTS", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=pts-btc&market=cryptsy"],
              ["SBC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=sbc-btc&market=cryptsy"],
              ["ANC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=anc-btc&market=cryptsy"],
              ["DGC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=dgc-btc&market=cryptsy"],
              ["FST", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=fst-btc&market=cryptsy"],
              ["FRC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=frc-btc&market=cryptsy"],
              #["YAC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=yac-btc&market=cryptsy"],
              ["CGB", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=cgb-btc&market=cryptsy"],
              ["ARG", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=arg-btc&market=cryptsy"],
              #["BTB", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=btb-btc&market=cryptsy"],
              ["GLD", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=gld-btc&market=cryptsy"],
              ["SRC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=src-btc&market=cryptsy"],
              #["MNC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=mnc-btc&market=cryptsy"],
              #["NEC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=nec-btc&market=cryptsy"],
              ["LKY", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=lky-btc&market=cryptsy"],
              ##["CNC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=cnc-btc&market=cryptsy"],
              #["NRB", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=nrb-btc&market=cryptsy"],
              #["GDC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=gdc-btc&market=cryptsy"],
              #["FRK", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=frk-btc&market=cryptsy"],
              #["GLC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=glc-btc&market=cryptsy"],
              #["BTE", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=bte-btc&market=cryptsy"],
              #["ELC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=elc-btc&market=cryptsy"],
              #["JKC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=jkc-ltc&market=cryptsy"],
              #["IXC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=ixc-btc&market=cryptsy"],
              #["CAP", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=cap-btc&market=cryptsy"],
              #["PXC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=pxc-btc&market=cryptsy"],
              #["CRC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=crc-btc&market=cryptsy"],
              #["ALF", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=alf-btc&market=cryptsy"],
              #["KGC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=kgc-btc&market=cryptsy"],
              #["GLX", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=glx-btc&market=cryptsy"],
              #["BUK", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=buk-btc&market=cryptsy"],
              #["CMC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=cmc-btc&market=cryptsy"],
              #["AMC", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=amc-btc&market=cryptsy"],
              #["EMD", "http://www.cryptocoincharts.info/period-charts.php?period=2-weeks&resolution=hour&pair=emd-btc&market=cryptsy"]
              ]

wallet2 = Wallet.Wallet()
for cur in currencies_s:
    wallet2.addCurrency(cur[0], Currency.Currency(cur[0], DataProvider.CryptocoinProvider(cur[0], cur[1])), 10)

tr_model = TradingModel.TradingModel(240, 1440*5, "sharpe", [50, 30, 20], 10)
trader = Trader.Trader(wallet2, tr_model)

print wallet2

Clock.Clock.setCurrentTime(datetime.datetime.now() - datetime.timedelta(days=6))

while Clock.Clock.getCurrentTime() < (datetime.datetime.now() - datetime.timedelta(hours=24)):
    trader.update()
    Clock.Clock.setCurrentTime(Clock.Clock.getCurrentTime() + datetime.timedelta(hours=1))

print wallet2