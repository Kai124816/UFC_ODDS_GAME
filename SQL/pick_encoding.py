from User.profile import Person
from User.predictions import Picks
from Fight_Card.card_constructor import Card
from Fight_Card.fight import Fight
import json

def pick_to_int(pick:list,card:Card):
    """
    Description of pick list:
        Pick[0] = Fighter name
        Pick[1] = Method, either "ML", "TKO", "Submission", or "Rounds"
        Pick[2] = Outcome, either "Hit" "Miss" or "TBD"
        Pick[3] = Amount, amount placed on bet
    """
    for i in range(len(card.fights)):
        if pick[0] == card.fights[i].fighter1:
            placement = i + 1
            fighter = 0
        elif pick[0] == card.fights[i].fighter2:
            placement = i + 1
            fighter = 1

    if pick[1] == "ML":
        method = 0
    elif pick[1] == "TKO":
        method = 1
    elif pick[1] == "Submission":
        method = 2
    else:
        method = 3
    
    if pick[2] == "TBD":
        outcome = 1
    elif pick[2] == "Miss":
        outcome = 2
    else:
        outcome == 3
    
    amount = pick[3]

    pick_num = bin(placement) & (bin(fighter) << 4)
    pick_num = pick_num & (bin(method) << 5)
    pick_num = pick_num & (bin(outcome) << 7)
    pick_num = pick_num & (bin(amount) << 9)
    return int(pick_num)

def picks_to_json(predictions:Picks):
    picks_list = []
    card = predictions.card
    for pick in predictions.picks:
        int1 = pick_to_int(pick,card)
        picks_list.append(int1)
    json_list = json.dumps(picks_list)
    return json_list

def decode_pick(pick_num:int,card:Card):
    pick = []
    placement = int(bin(pick_num) & bin(15))
    fighter = int(bin(pick_num) & (bin(1) << 4))
    method = int(bin(pick_num) & (bin(3) << 5))
    outcome = int(bin(pick_num) & (bin(3) << 7))
    amount = int(bin(pick_num) & (bin(63) << 9))

    if fighter == 0:
        pick[0] = card.fights[placement+1].fighter1
    if fighter == 1:
        pick[0] = card.fights[placement+1].fighter2
    
    if method == 0:
        pick[1] = "ML"
    elif method == 1:
        pick[1] = "TKO"
    elif method == 2:
        pick[1] = "Submission"
    else:
        pick[1] = "Rounds"

    if outcome == 1:
        pick[2] = "TBD"
        outcome = 1
    elif outcome == 2:
        pick[2] = "Miss"
    else:
        pick[2] = "Hit"

    pick[3] = amount

    




    




def json_to_picks(card:Card,json_picks:json):
    python_list = json.loads(json_picks)


    




    






