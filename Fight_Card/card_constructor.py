from Fight_Card.fight import Fight
import datetime

class Card:
    """
    Represents a card containing a list of fights and a scheduled date.

    Attributes:
        date (datetime.date): The date of the card.
        fights (list[Fight]): A list of Fight objects scheduled on the card.
    """

    def __init__(self, fights: list[Fight], date: datetime.date) -> None:
        """
        Initializes a Card object with a list of fights and a date.

        Args:
            fights (list[Fight]): A list of Fight objects scheduled for the card.
            date (datetime.date): The date of the card.

        Returns:
            None
        """
        self.date = date
        self.fights = fights

    def update_outcomes(self, update: tuple) -> None:
        """
        Updates the outcome of a specific fight on the card.

        Args:
            update (tuple): A tuple containing the fight name (str) and the new outcome.

        Raises:
            ValueError: If no fight with the given name is found on the card.

        Returns:
            None
        """
        fight_name, new_outcome = update
        for fight in self.fights:
            if fight.name == fight_name:
                fight.update_outcome(new_outcome)
                break
        else:
            raise ValueError(f"Fight with name '{fight_name}' not found.")



    
    
            

        
