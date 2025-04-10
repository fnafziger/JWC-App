from market import MarketSimulation
import random

class Stock:
    '''Class for a company's stock, not an individual stock.'''

    def __init__(self, simulation: MarketSimulation, symbol: str, name: str, initalValue: float, amount: int, initalScore: float = 0.0):
        '''
        simulation: MarketSimulation - The market that a stock is part of.

        symbol: str - Three letter stock ticker symbols.

        name: str - Name of stock company.

        initalValue: float - The initial value for a stock.

        amount: int - The number of stocks in the company.

        initalScore: float - The initial score that a stock has. The stock score determines how a stock performs.
        '''

        self._simulation = simulation
        self._symbol = symbol
        self._name = name
        self._amount = amount
        self._score = initalScore
        self._value = initalValue

        self._simulation.addStock(self)

    def updateValue(self, bias: float = 0.0) -> float: 
        '''
        Updates stock value. Updates occur on a bell curve, based on the stock's score.
        
        bias: float - An additional bias that can be added on top of the stock's score.

        Returns: New stock value.
        '''

        change = self._value * max(-1, min(random.gauss(self._simulation.MEAN + (self._score / 10) + (bias / 10), self._simulation.STANDARD_DEVIATION), 1)) # Guass produces a bell curve (IE: drastic changes are less likely.)
        self._value += change
        return self._value

    def split(self, splitAmount: int) -> None:
        '''
        Performs a stock split.

        splitAmount: int - The amount of stocks that each current stock will be split into.
        '''

        self._value / splitAmount
        self._amount * splitAmount

    @property
    def symbol(self) -> str:
        return self._symbol
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def value(self) -> float:
        return self._value