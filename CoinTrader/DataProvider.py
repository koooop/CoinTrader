import urllib2
import re
import datetime
import Clock

class DataProvider(object):
    """Base-class data provider for accessing currency statistics"""

    def __init__(self, currency, source):
        self.currency = currency
        self.source = source
        self.data = []
        self.cache_unitize = []
        self.cache_unitize_period = None
        self.cache_unitize_unit = None

    def getData(self):
        return self.data

    def update(self):
        pass

    def unitize(self, unit, period):
        if self.cache_unitize_period == period and self.cache_unitize_unit == unit and self.cache_unitize:
            return self.cache_unitize
        else:
            period_start_time = Clock.Clock.getCurrentTime() - datetime.timedelta(minutes=period)

            current_unit_time = period_start_time
            result = []

            while (current_unit_time + datetime.timedelta(minutes=unit)) <= Clock.Clock.getCurrentTime():
                result.append([entry[1] for entry in self.data 
                 if entry and (current_unit_time <= entry[0] <= current_unit_time + datetime.timedelta(minutes=unit))])
                current_unit_time += datetime.timedelta(minutes=unit)

            # if first unit is empty add there last entry prior of period
            if len(result[0]) == 0:
                try:
                    last_before = [entry[1] for entry in self.data if entry[0] < current_unit_time][-1] #.sort(key=lambda x: [entry[0]])
                    result[0].append(last_before)
                except IndexError:
                    raise IndexError("Not enough datapoints at begining for {0}".format(self.currency))
        
            # initialize cache
            self.cache_unitize = result
            self.cache_unitize_period = period
            self.cache_unitize_unit = unit

            return result

class CryptocoinProvider(DataProvider):
    """Cryptocoin data provider (http://www.cryptocoincharts.info/)}"""

    def __init__(self, currency, source):
        DataProvider.__init__(self, currency, source)
        self.update()

    def update(self):
        
        # get source code of particular cryptocoinchart page
        response = urllib2.urlopen(self.source)
        html = response.read()

        # parse 
        temp_array = eval(re.search('google\.visualization\.arrayToDataTable(.*);', html).group(1))
        temp_array.pop(0)

        self.data = [[datetime.datetime.strptime(entry[0],'%Y-%m-%d %Hh'), entry[3]] for entry in temp_array]