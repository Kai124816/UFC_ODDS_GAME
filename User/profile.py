from predictions import picks

class person():
    def __init__(self,username:str,password:str,history:list[picks],current_picks:picks,total_payout:int,total_profit:int) -> None:
        self.username = username
        self.password = password
        self.history = history
        self.current_picks = current_picks
        self.total_payout = total_payout
        self.total_profit = total_profit

    def commit_to_history(self) -> None:
        self.history.append(self.current_picks)
        self.total_payout += self.current_picks.payout
        self.total_profit += self.current_picks.payout
        self.total_profit -= 50
        new_picks = picks([],50,0)
        self.current_picks = new_picks
    
    def change_password(self,new_password:str) -> None:
        self.password = new_password
        