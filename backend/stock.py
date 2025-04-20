import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

import constants 
import random

class Stock:
    '''Class for a company's stock, not an individual stock.'''

    def __init__(self, symbol: str, name: str, initialValue: float, amount: int, initialScore: float = 0.0):
        '''
        market: MarketSimulation - The market that a stock is part of.

        symbol: str - Three letter stock ticker symbols.

        name: str - Name of stock company.

        initialValue: float - The initial value for a stock.

        amount: int - The number of stocks in the company.

        initialScore: float - The initial score that a stock has. The stock score determines how a stock performs.
        '''

        self.symbol = symbol
        self.name = name
        self.amount = amount
        self.score = initialScore
        self.value = initialValue
        self.history = [initialValue]

    def updateValue(self, bias: float = 0.0) -> float: 
        '''
        Updates stock value. Updates occur on a bell curve, based on the stock's score.
        
        bias: float - An additional bias that can be added on top of the stock's score.

        Returns: New stock value.
        '''

        change = max(-1, min(random.gauss(constants.MEAN + (self.score / 100) + (bias / 100), constants.STANDARD_DEVIATION), 1)) # Gauss produces a bell curve (IE: drastic changes are less likely.)
        self.value += change

        self.value = round(self.value, 2)
        self.history.append(self.value)

        if len(self.history) > 1000:
            self.history = self.history[-1000:]

        return self.value

    def split(self, splitAmount: int) -> None:
        '''
        Performs a stock split.

        splitAmount: int - The amount of stocks that each current stock will be split into.
        '''

        self.value / splitAmount
        self.amount * splitAmount

    def centerScore(self, amount: float, weight: float) -> float:
        '''
        Gradully recenters the stock score towards zero.

        amount: float - The amount that the score changes by towards zero.

        weight: float - Added weight towards positive or negative score. 
        
        Returns: The new score.
        '''

        if self.score < 0:
            self.score = min(0, self.score + amount) + weight
        else:
            self.score = max(0, self.score - amount) + weight    

        return self.score    

    def updateScore(self, chance: float) -> float:
        '''
        Randomly updates the stock's score

        chance: float - The chance that the stock gets updated.
        
        Returns: New stock score.
        '''

        if random.random() < chance:
            self.score = max(-1, min(self.score + random.gauss(constants.MEAN, constants.STANDARD_DEVIATION), 1)) # Changes the score on a bell curve. The new score has a slight bias from the current score. 
            return self.score