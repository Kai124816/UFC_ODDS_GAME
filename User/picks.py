from ..Fight_Card.card_constructor import Card
from ..Fight_Card.fight import fight

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
    def __init__(self,picks:list[list],card:Card,remaining_budget:int,payout:int) -> None:
        self.picks = picks
        self.card = card
        self.remaining_budget = remaining_budget
        self.payout = payout

    def calculate_payout(self,odds, bet_amount):
        """
        Calculate the payout for a given bet amount and odds.

        Args:
        odds (int): The American odds (can be positive or negative).
        bet_amount (float): The amount of money placed on the bet.

        Returns:
        float: The total payout (including the original bet).
        """
        if odds < 0:
            # Negative odds (e.g., -200): You need to bet more to win $100
            win_amount = bet_amount * 100 / abs(odds)
        else:
            # Positive odds (e.g., +350): You win the amount based on a $100 bet
            win_amount = bet_amount * odds / 100

        # Total payout is the win amount + the initial bet
        bet_payout = bet_amount + win_amount
        self.payout += bet_payout
    
    def make_pick(self,fighter:str,method:str,amount:int):
        if self.remaining_budget - amount < 0:
            raise BetExceedsBudgetError(amount,self.remaining_budget)
        if self.remaining_budget - amount < (3 - len(self.picks) - 1):
            raise InsufficientBetsError(len(self.picks+1))
        for fight in self.card.fights:
            if fighter == fight.fighter1:
                opponent = fight.fighter2
                break
            elif fighter == fight.fighter2:
                opponent = fight.fighter1
                break
        for pick in self.picks:
            if pick[0] == opponent:
                raise ContradictoryBetsError(opponent,fighter)
        pick = []
        pick[0] = fighter
        pick[1] = method
        pick[2] = "TBD"
        pick[3] = amount
        self.picks.append(pick)
        self.remaining_budget -= amount

    def remove_picks(self,pick:list):
        self.picks.remove(pick)
    
    def update_picks(self,update:fight):
        if update.outcome[0] == "NC":
            for pick in self.picks:
                if pick[0] == update.fighter1 or pick[0] == update.fighter2:
                    pick[2] == "Miss"
                    self.payout += pick[3]
                    break
        elif update.outcome[0] == "Draw":
            for pick in self.picks:
                if pick[0] == update.fighter1 or pick[0] == update.fighter2:
                    pick[2] == "Miss"
                    if pick[1] == "ML":
                        self.payout += pick[3]
                    break
        else:
            if update.fighter1 == update.outcome[0]:
                winner = update.fighter1
                loser = update.fighter2
                ml = update.fighter1_ml
            else:
                winner = update.fighter2
                loser = update.fighter1
                ml = update.fighter2_ml
            for pick in self.picks:
                if pick[0] == winner:
                    if pick[1] == "ML" or pick[1] == update.outcome[1]:
                        pick[2] == "Hit"
                        self.calculate_payout(ml,pick[3])
                    else:
                        pick[2] = "Miss"
                elif pick[0] == loser:
                    pick[2] = "Miss"


        

        
        



        
        
        
        

        
        