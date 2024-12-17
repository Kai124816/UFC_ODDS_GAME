from Fight_Card import card_constructor 
from card_constructor import Card


class BetExceedsBudgetError(Exception):
    """Raised when a bet exceeds the user's budget."""
    def __init__(self, bet, budget, message="Bet exceeds your current budget."):
        self.bet = bet
        self.budget = budget
        super().__init__(f"{message} Bet: {bet}, Budget: {budget}")


class ContradictoryBetsError(Exception):
    """Raised when contradictory bets are placed."""
    def __init__(self, fighter1, fighter2, message="Contradictory bets placed on fighters facing each other."):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        super().__init__(f"{message} Fighters: {fighter1} vs {fighter2}")


class InsufficientBetsError(Exception):
    """Raised when the user will not be able to place three bets with their current budget"""
    def __init__(self, total_bets, message="You will not be able to place three bets if you place this bet."):
        self.total_bets = total_bets
        super().__init__(f"{message} Total bets: {total_bets}")


class picks():
    def __init__(self,picks:list[tuple],remaining_budget:int,payout:int) -> None:
        self.picks = picks
        self.remaining_budget = remaining_budget
        self.payout = payout
    
    def make_pick(self,fighter:str,method:str,amount:int):
        if self.remaining_budget - amount < 0:
            raise BetExceedsBudgetError(amount,self.remaining_budget)
        if self.remaining_budget - amount < (3 - len(self.picks) - 1):
            raise InsufficientBetsError(len(self.picks+1))
        
        
        
        

        
        