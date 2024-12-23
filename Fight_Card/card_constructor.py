from Fight_Card.fight import Fight
import datetime

class Card:
    def __init__(self, fights: list[Fight],date:datetime.date) -> None:
        self.date = date
        self.fights = fights

    def update_outcomes(self, update: tuple) -> None:
        fight_name, new_outcome = update
        for fight in self.fights:
            if fight.name == fight_name:
                fight.update_outcome(new_outcome)
                break
        else:
            raise ValueError(f"Fight with name '{fight_name}' not found.")



    
    
            

        
