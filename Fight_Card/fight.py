class Fight:
    """
    Represents a fight between two fighters with associated details and outcome.

    Attributes:
        name (str): The name of the fight.
        fighter1 (str): The name of the first fighter.
        fighter2 (str): The name of the second fighter.
        fighter1_ml (int): The moneyline odds for the first fighter.
        fighter2_ml (int): The moneyline odds for the second fighter.
        fighter1_props (dict): A dictionary of proposition bets for the first fighter.
        fighter2_props (dict): A dictionary of proposition bets for the second fighter.
        rounds (float): The number of rounds scheduled for the fight.
        outcome (list): The outcome of the fight as a list [winner, method, round].
                       If there is no winner, the first element is None.
    """

    def __init__(self, name: str, fighter1: str, fighter2: str, fighter1_ml: int, fighter2_ml: int, 
                 fighter1_props: dict, fighter2_props: dict, rounds: float, outcome: list) -> None:
        """
        Initializes a Fight object with details of the fighters, odds, and initial outcome.

        Args:
            name (str): The name of the fight.
            fighter1 (str): The name of the first fighter.
            fighter2 (str): The name of the second fighter.
            fighter1_ml (int): The moneyline odds for the first fighter.
            fighter2_ml (int): The moneyline odds for the second fighter.
            fighter1_props (dict): Proposition bets for the first fighter.
            fighter2_props (dict): Proposition bets for the second fighter.
            rounds (float): The number of rounds scheduled for the fight.
            outcome (list): The initial outcome of the fight, structured as [winner, method, round].
                            If there is no winner, the first element should be None.

        Returns:
            None
        """
        self.name = name
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.fighter1_ml = fighter1_ml
        self.fighter2_ml = fighter2_ml
        self.fighter1_props = fighter1_props
        self.fighter2_props = fighter2_props
        self.rounds = rounds
        self.outcome = outcome
    
    def update_outcome(self, update: list) -> None:
        """
        Updates the outcome of the fight.

        Args:
            update (list): A list representing the updated outcome [winner, method, round].
                           The first element should be None if there is no winner.

        Raises:
            ValueError: If the update is not a list.

        Returns:
            None
        """
        if not isinstance(update, list):
            raise ValueError("Outcome update must be a list.")
        self.outcome = update


    

        
        