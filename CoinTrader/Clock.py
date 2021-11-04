import datetime

class Clock(object):
    """Clock"""
    current_time = datetime.datetime.now()

    @staticmethod
    def getCurrentTime():
        #return datetime.datetime.now() - datetime.timedelta(hours=8) asd
        return Clock.current_time

    @staticmethod
    def setCurrentTime(time):
        Clock.current_time = time




