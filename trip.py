class Trip:
    _all = []

    def __init__(self, start, destination, driver):
        self._start = str(start)
        self._destination = str(destination)
        self._driver = driver
        Trip._all.append(self)
       
    @property
    def start(self):
        return self._start
    
    @start.setter
    def start(self, start):
        self._start = start
        
    @property
    def destination(self):
        return self._destination
    
    @destination.setter
    def destination(self, destination):
        self._destination = destination
    
    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, driver):
        self._driver = driver
        
    @classmethod
    def all(cls):
        return cls._all