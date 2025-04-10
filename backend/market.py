from stock import Stock
from datetime import time, datetime, timezone

class MarketSimulation:
    '''Class for simulated market that handles all the stocks delecated to it.'''

    # Constants for stock updates.
    MEAN = 0.00
    STANDARD_DEVIATION = 0.03

    def __init__(self, idCode: str, timeOpenUTC: time, timeCloseUTC: time, initalMarketBias: float = 0.0):
        '''
        idCode: str - Four letter code to identify stock market.

        timeOpenUTC: time - The time that the market opens.

        timeCloseUTC: time - The time that the market closes.

        initalMarketBias: float - The initial bias for the market. All stocks will be effected by this.
        '''

        self._idCode = idCode
        self._timeOpen = timeOpenUTC
        self._timeClose = timeCloseUTC
        self._marketBias = initalMarketBias
        self._marketValue = 0.0
        self._stocks = [] # type: list[Stock]

    def isOpen(self) -> bool:
        '''
        Checks whether the market is currently open.

        Returns: Whether the market is open.
        '''

        current = datetime.now(timezone.utc).time()
        return self._timeOpen < current < self._timeClose
    
    def addStock(self, stock: Stock | list[Stock]) -> None:
        '''
        Adds a new stock to the market.
        
        stock: Stock | list[Stock] - Stock(s) to be added to the market.
        '''

        if type(stock) == list:
            self._stocks.extend(stock)
        else:
            self._stocks.append(stock)

    def updateAllStocks(self, excludedStocks: list[Stock] = None) -> float:
        '''
        Updates all stock values and updates market value.
        
        exludedStocks: list[Stock] - Stocks that will not be updated. They are still counted for market value.

        Returns: New market value.
        '''

        total = 0
        for stock in self._stocks:
            if stock in excludedStocks:
                total += stock.value
            else:
                total += stock.updateValue(self._marketBias)

        self._marketValue = total

        return(self._marketValue)
    
    @property
    def idCode(self) -> str:
        return self._idCode
    
    @property
    def timeOpen(self) -> datetime:
        return self._timeOpen
    
    @property
    def timeClose(self) -> datetime:
        return self._timeClose
    
    @property
    def timeClose(self) -> datetime:
        return self._timeClose
        
    @property
    def marketBias(self) -> float:
        return self._marketBias
    
    @property
    def marketValue(self) -> float:
        return self._marketValue
    
    @property
    def stocks(self) -> list[Stock]:
        return self._stocks