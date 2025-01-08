import sys
sys.path.append("../")
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


class ContradictoryMethodsError(Exception):
    """Raised when contradictory bets are placed."""
    def __init__(self, fighter, method1, method2, message="Contradictory bets placed on the same fighter by different methods."):
        self.fighter1 = fighter
        self.method1 = method1
        self.method2 = method2
        super().__init__(f"{message} {fighter} by {method1} and {fighter} by {method2}")


class Picks:
    def __init__(self, picks: list[list] = None, card: Card = None, remaining_budget: int = 0, payout: int = 0) -> None:
        """
        Initialize Picks with betting data.

        Args:
            picks (list): List of user picks. Each pick is a list containing fighter, method, outcome, and amount.
            card (Card): The associated Card object, which contains the details of the fights.
            remaining_budget (int): The user's remaining budget for betting.
            payout (int): Total payout amount accumulated from all bets.

        Returns:
            None
        """
        self.picks = picks if picks else []
        self.card = card
        self.remaining_budget = remaining_budget
        self.payout = payout

    def calculate_payout(self, odds: int, bet_amount: float) -> None:
        """
        Calculate and add the payout for a given bet amount and odds.

        Args:
            odds (int): The odds of the bet, positive for favorites, negative for underdogs.
            bet_amount (float): The amount of money placed on the bet.

        Returns:
            None
        """
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
            ContradictoryBetsError: If contradictory bets are placed on the same fighter's opponent.
            InsufficientBetsError: If placing this bet prevents the user from making at least three bets.

        Returns:
            None

        Description of the pick list:
            Pick[0] = Fighter name
            Pick[1] = Method (e.g., "ML", "TKO", "Submission", "Rounds")
            Pick[2] = Outcome ("Hit", "Miss", or "TBD")
            Pick[3] = Amount placed on bet
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
            elif pick[0] == fighter:
                if pick[1] != method:
                    raise ContradictoryMethodsError(fighter,pick[1],method)
                else:
                    pick[3] += amount
        
        new_pick = [fighter, method, "TBD", amount]
        if new_pick not in self.picks:
            self.picks.append(new_pick)
            self.remaining_budget -= amount

    def remove_pick(self, pick: list) -> None:
        """
        Remove a specific pick from the list of user picks.

        Args:
            pick (list): The pick to be removed from the list.

        Returns:
            None
        """
        self.remaining_budget += pick[3]
        self.picks.remove(pick)

    def update_picks(self, update: Fight) -> None:
        """
        Update picks based on the outcomes of a fight.

        Args:
            update (Fight): The fight object containing the outcome of the fight.

        Returns:
            None
        """
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
