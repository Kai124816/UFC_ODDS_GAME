import sys
sys.path.append('/Users/kaihogan/Projects/Odds_Game_2')
from Fight_Card.card_constructor import Card
from Fight_Card.fight import Fight



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
    """Raised when the user will not be able to place three bets with their current budget."""
    def __init__(self, total_bets, message="You will not be able to place three bets if you place this bet."):
        self.total_bets = total_bets
        super().__init__(f"{message} Total bets: {total_bets}")


class Picks:
    def __init__(self, picks: list[list] = None, card: Card = None, remaining_budget: int = 0, payout: int = 0) -> None:
        """
        Initialize Picks with betting data.

        Args:
        picks (list): List of user picks.
        card (Card): The associated Card object.
        remaining_budget (int): User's remaining budget for betting.
        payout (int): Total payout amount.
        """
        self.picks = picks if picks else []
        self.card = card
        self.remaining_budget = remaining_budget
        self.payout = payout

    def calculate_payout(self, odds: int, bet_amount: float) -> None:
        """Calculate and add the payout for a given bet amount and odds."""
        if odds < 0:
            win_amount = bet_amount * 100 / abs(odds)
        else:
            win_amount = bet_amount * odds / 100
        self.payout += bet_amount + win_amount

    def make_pick(self, fighter: str, method: str, amount: int) -> None:
        """
        Add a new pick for a fighter.

        Args:
        fighter (str): The fighter's name.
        method (str): The method of victory (e.g., KO, Decision).
        amount (int): The bet amount.

        Raises:
        BetExceedsBudgetError: If the bet exceeds the remaining budget.
        ContradictoryBetsError: If contradictory bets are placed.
        InsufficientBetsError: If placing this bet prevents the user from making three bets.
        """
        if self.remaining_budget - amount < 0:
            raise BetExceedsBudgetError(amount, self.remaining_budget)
        if self.remaining_budget - amount < (3 - len(self.picks) - 1):
            raise InsufficientBetsError(len(self.picks) + 1)

        # Find the opponent of the chosen fighter
        opponent = None
        for fight in self.card.fights:
            if fighter == fight.fighter1:
                opponent = fight.fighter2
                break
            elif fighter == fight.fighter2:
                opponent = fight.fighter1
                break

        # Check for contradictory bets
        for pick in self.picks:
            if pick[0] == opponent:
                raise ContradictoryBetsError(opponent, fighter)

        # Add the new pick
        new_pick = [fighter, method, "TBD", amount]
        self.picks.append(new_pick)
        self.remaining_budget -= amount

    def remove_pick(self, pick: list) -> None:
        """Remove a specific pick."""
        self.picks.remove(pick)

    def update_picks(self, update: Fight) -> None:
        """Update picks based on fight outcomes."""
        if update.outcome[0] == "NC":
            for pick in self.picks:
                if pick[0] in [update.fighter1, update.fighter2]:
                    pick[2] = "Miss"
                    self.payout += pick[3]
        elif update.outcome[0] == "Draw":
            for pick in self.picks:
                if pick[0] in [update.fighter1, update.fighter2]:
                    pick[2] = "Miss"
                    if pick[1] == "ML":
                        self.payout += pick[3]
        else:
            winner, loser, ml = (update.fighter1, update.fighter2, update.fighter1_ml) if update.fighter1 == update.outcome[0] else (update.fighter2, update.fighter1, update.fighter2_ml)
            for pick in self.picks:
                if pick[0] == winner:
                    if pick[1] == "ML" or pick[1] == update.outcome[1]:
                        pick[2] = "Hit"
                        self.calculate_payout(ml, pick[3])
                    else:
                        pick[2] = "Miss"
                elif pick[0] == loser:
                    pick[2] = "Miss"
