import sys
sys.path.append('/Users/kaihogan/Projects/Odds_Game_2')
from Fight_Card.fight import Fight

class Card:
    def __init__(self, fights: list[Fight]) -> None:
        self.fights = fights

    def update_outcomes(self, update: tuple) -> None:
        fight_name, new_outcome = update
        for fight in self.fights:
            if fight.name == fight_name:
                fight.update_outcome(new_outcome)
                break
        else:
            raise ValueError(f"Fight with name '{fight_name}' not found.")



    
    
            

        
