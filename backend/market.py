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

        self.idCode = idCode
        self.timeOpen = timeOpenUTC
        self.timeClose = timeCloseUTC
        self.marketBias = initalMarketBias
        self.marketValue = 0.0
        self.stocks = [] # type: list[Stock]

    def isOpen(self) -> bool:
        '''
        Checks whether the market is currently open.

        Returns: Whether the market is open.
        '''

        current = datetime.now(timezone.utc).time()
        return self.timeOpen < current < self.timeClose
    
    def addStock(self, stock: Stock | list[Stock]) -> None:
        '''
        Adds a new stock to the market.
        
        stock: Stock | list[Stock] - Stock(s) to be added to the market.
        '''

        if type(stock) == list:
            self.stocks.extend(stock)
        else:
            self.stocks.append(stock)

    def updateAllStocks(self, excludedStocks: list[Stock] = []) -> float:
        '''
        Updates all stock values and updates market value.
        
        exludedStocks: list[Stock] - Stocks that will not be updated. They are still counted for market value.

        Returns: New market value.
        '''

        total = 0
        for stock in self.stocks:
            if stock in excludedStocks:
                total += stock.value * stock.amount
            else:
                total += stock.updateValue(self.marketBias) * stock.amount
                stock.centerScore(0.01, 0)
                stock.updateScore(0.1)

        self.marketValue = total

        return(self.marketValue)