import numpy
import math
import Clock

class Currency(object):
    """Represents a particular currency"""

    def __init__(self, name, data_provider):
       self.name = name
       self.data_provider = data_provider

    def getCurrentExchangeRate(self):
        return [entry[1] for entry in self.data_provider.getData() if entry and entry[0] <= Clock.Clock.getCurrentTime()][-1]

    def getTotalPerReturn(self, unit, period):
        """Get total return for given period (ending on current time)
        TotalReturn is calculated as "CloseValue for last unit of period"/"CloseValue for first unit of period" * 100"""

        units = self.data_provider.unitize(unit, period)
        if len(units[0])== 0:
            raise Exception("Not enough datapoints at begining for {0}".format(self.name))
        return ((units[-1][-1]/units[0][-1]) - 1) * 100

    def getAvgPerReturn(self, unit, period):
        units = self.data_provider.unitize(unit, period)
        if len(units[0])== 0:
            raise Exception("Not enough datapoints at begining for {0}".format(self.name))
        return numpy.mean([(unit[-1]/unit[0] - 1) * 100 for unit in units])

    def getAvgReturn(self, unit, period):
        units = self.data_provider.unitize(unit, period)
        result = []
        for i in range(len(units)):
            #first unit can have:
            #  0 members - throw exception
            #  1 member - skip this unit as we cannot determine return for it
            #  2 and more members - calculate return as last - first member of unit
            if i == 0:
                if len(units[i])== 0:
                    raise Exception("Not enough datapoints at begining for {0}".format(self.name))
                elif len(units) > 1:
                    result.append(units[i][-1] - units[i][0])
            else:
                # if second and later unit is empty, count with return = 0
                # prev always holds last value for last non-empty unit 
                if len(units[i])== 0:
                    if units[i-1]:
                        prev = units[i-1][-1]
                    result.append(0)
                # if second and later unit is not empty, return is:
                # "last val from current unit" - "last val from previous non-empty unit"  
                else:
                    if units[i-1]:
                        prev = units[i-1][-1]
                    result.append(units[i][-1] - prev)
        return numpy.mean(result)

    def getStdevReturn(self, unit, period):
        units = self.data_provider.unitize(unit, period)
        result = []
        for i in range(len(units)):
            # if first unit has 0 members, throw exception otherwise add last m. of unit
            if i == 0:
                if len(units[i])== 0:
                    raise Exception("Not enough datapoints at begining for {0}".format(self.name))
                else:
                    result.append(units[i][-1])    
            else:
                # if second and later unit is empty, add prev
                # prev always holds last value for last non-empty unit 
                if len(units[i])== 0:
                    if units[i-1]:
                        prev = units[i-1][-1]
                    result.append(prev)
                # if second and later unit is not empty, return is last val of unit  
                else:
                    if units[i-1]:
                        prev = units[i-1][-1]
                    result.append(units[i][-1])
        return numpy.std(result)

    def getSharpRatio(self, unit, period):
        units = self.data_provider.unitize(unit, period)
        k = math.sqrt(period / unit)
        return k * (self.getAvgReturn(unit, period)/self.getStdevReturn(unit, period))

    def getKeyFactorValue(self, unit, period, key_factor):
        if key_factor == "sharpe":
            return self.getSharpRatio(unit, period)
        elif key_factor == "total_return":
            return self.getTotalPerReturn(unit,period)
        elif key_factor == "avg_return":
            return self.getAvgReturn(unit,period)

class BitCoin(Currency):
    """Dummy constant currency"""

    def getCurrentExchangeRate(self):
        return 1

    def getTotalPerReturn(self, unit, period):
        return 0

    def getAvgPerReturn(self, unit, period):
        return 0

    def getAvgReturn(self, unit, period):
        return 0

    def getStdevReturn(self, unit, period):
        return 0

    def getSharpRatio(self, unit, period):
        return 0