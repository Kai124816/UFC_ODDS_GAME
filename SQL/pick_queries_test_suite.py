from User.profile import Person
from User.predictions import Picks
from Fight_Card.card_constructor import Card
from Fight_Card.fight import Fight
from SQL.pick_queries import table_exists, create_table, store_picks, delete_user, SQL_to_Picks
import datetime

# Example instance of the Fight class
fight1 = Fight(
    name="Main Event",
    fighter1="Peter Howton",
    fighter2="Shamil Gaziev",
    fighter1_ml=-150,  # Money Line for Fighter 1
    fighter2_ml=130,   # Money Line for Fighter 2
    fighter1_props={"KO": 250, "Submission": 300},  # Props for Fighter 1
    fighter2_props={"KO": 200, "Submission": 350},  # Props for Fighter 2
    rounds=2.5,  # Over/Under on Rounds
    outcome=["Shamil Gaziev", "KO", 2]  # Winner is Shamil Gaziev, by KO in Round 2
)

fight2 = Fight(
    name="Co-Main Event",
    fighter1="Edison Castle",
    fighter2="Tracy Cortez",
    fighter1_ml=-120,
    fighter2_ml=110,
    fighter1_props={"KO": 220, "Submission": 330},
    fighter2_props={"KO": 240, "Submission": 320},
    rounds=3.5,
    outcome=["Edison Castle", "Submission", 3]
)

fight3 = Fight(
    name="Opening Fight",
    fighter1="Aiden Sands",
    fighter2="Hinge Demon",
    fighter1_ml=100,
    fighter2_ml=-110,
    fighter1_props={"KO": 280, "Submission": 400},
    fighter2_props={"KO": 260, "Submission": 310},
    rounds=1.5,
    outcome=["Aiden Sands", "Decision", 3]  
)

pick_1 = ["John Doe","ML","Hit",14]
pick_2 = ["Peter Howton","Decision","Miss",9]
pick_3 = ["Edison Castle","Submission","Hit",12]
pick_4 = ["Aiden Sands","TKO","Miss",8]

Test_Card = card = Card(
    fights=[fight1, fight2, fight3],  # List of Fight instances
    date=datetime.date(2024, 12, 25)  # Example date
)
test_picks = Picks([pick_1,pick_2,pick_3,pick_4],Test_Card,7,35)
Test_User1 = Person("Kai","1234",test_picks,[],79,14)

print(table_exists("Kai_picks"))
create_table(Test_User1)
print(table_exists("Kai_picks"))
store_picks(Test_User1)
SQL_to_Picks(Test_User1,datetime.date(2024, 12, 25))
print(Test_User1.picks.picks)
delete_user(Test_User1)










