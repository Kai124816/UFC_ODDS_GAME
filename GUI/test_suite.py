from gameplay_interface import interface
from User.profile import Person
from User.predictions import Picks
from Fight_Card.card_constructor import Card
from Fight_Card.fight import Fight
import datetime

fight1 = Fight(
    name="Mackenzie Dern vs Amanda Ribas",
    fighter1="Mackenzie Dern",
    fighter2="Amanda Ribas",
    fighter1_ml=-218,  # Money Line for Fighter 1
    fighter2_ml=180,   # Money Line for Fighter 2
    fighter1_props={"Decision": 150, "TKO": 250, "Submission": 300},  # Example Props for Fighter 1
    fighter2_props={"Decision": 150, "TKO": 200, "Submission": 350},  # Example Props for Fighter 2
    rounds=3.0,  # Over/Under on Rounds
    outcome=["TBD"]  # Fight hasn't happened yet
)

fight2 = Fight(
    name="Santiago Ponzinibbio vs Carlston Harris",
    fighter1="Santiago Ponzinibbio",
    fighter2="Carlston Harris",
    fighter1_ml=-108,
    fighter2_ml=-112,
    fighter1_props={"Decision": 140, "TKO": 220, "Submission": 310},
    fighter2_props={"Decision": 160, "TKO": 210, "Submission": 330},
    rounds=3.0,
    outcome=["TBD"]
)

fight3 = Fight(
    name="Cesar Almeida vs Abdul Razak Alhassan",
    fighter1="Cesar Almeida",
    fighter2="Abdul Razak Alhassan",
    fighter1_ml=-110,
    fighter2_ml=-110,
    fighter1_props={"Decision": 130, "TKO": 240, "Submission": 320},
    fighter2_props={"Decision": 150, "TKO": 230, "Submission": 340},
    rounds=3.0,
    outcome=["TBD"]
)

fight4 = Fight(
    name="Chris Curtis vs Roman Kopylov",
    fighter1="Chris Curtis",
    fighter2="Roman Kopylov",
    fighter1_ml=210,
    fighter2_ml=-258,
    fighter1_props={"Decision": 170, "TKO": 260, "Submission": 350},
    fighter2_props={"Decision": 140, "TKO": 220, "Submission": 310},
    rounds=3.0,
    outcome=["TBD"]
)

fight5 = Fight(
    name="Christian Rodriguez vs Austin Bashi",
    fighter1="Christian Rodriguez",
    fighter2="Austin Bashi",
    fighter1_ml=-120,
    fighter2_ml=100,
    fighter1_props={"Decision": 150, "TKO": 250, "Submission": 300},
    fighter2_props={"Decision": 160, "TKO": 240, "Submission": 320},
    rounds=3.0,
    outcome=["TBD"]
)

fight6 = Fight(
    name="Punahele Soriano vs Uroš Medić",
    fighter1="Punahele Soriano",
    fighter2="Uroš Medić",
    fighter1_ml=164,
    fighter2_ml=-198,
    fighter1_props={"Decision": 180, "TKO": 270, "Submission": 350},
    fighter2_props={"Decision": 150, "TKO": 230, "Submission": 320},
    rounds=3.0,
    outcome=["TBD"]
)

fight7 = Fight(
    name="Jose Johnson vs Felipe Bunes",
    fighter1="Jose Johnson",
    fighter2="Felipe Bunes",
    fighter1_ml=-198,
    fighter2_ml=164,
    fighter1_props={"Decision": 140, "TKO": 220, "Submission": 310},
    fighter2_props={"Decision": 160, "TKO": 210, "Submission": 330},
    rounds=3.0,
    outcome=["TBD"]
)

fight8 = Fight(
    name="Marco Tulio vs Ihor Potieria",
    fighter1="Marco Tulio",
    fighter2="Ihor Potieria",
    fighter1_ml=-110,
    fighter2_ml=-110,
    fighter1_props={"Decision": 130, "TKO": 240, "Submission": 320},
    fighter2_props={"Decision": 150, "TKO": 230, "Submission": 340},
    rounds=3.0,
    outcome=["TBD"]
)

fight9 = Fight(
    name="Thiago Moisés vs Trey Ogden",
    fighter1="Thiago Moisés",
    fighter2="Trey Ogden",
    fighter1_ml=-192,
    fighter2_ml=160,
    fighter1_props={"Decision": 140, "TKO": 220, "Submission": 310},
    fighter2_props={"Decision": 160, "TKO": 210, "Submission": 330},
    rounds=3.0,
    outcome=["TBD"]
)

fight10 = Fight(
    name="Preston Parsons vs Andreas Gustafsson",
    fighter1="Preston Parsons",
    fighter2="Andreas Gustafsson",
    fighter1_ml=-110,
    fighter2_ml=-110,
    fighter1_props={"Decision": 130, "TKO": 240, "Submission": 320},
    fighter2_props={"Decision": 150, "TKO": 230, "Submission": 340},
    rounds=3.0,
    outcome=["TBD"]
)

fight11 = Fight(
    name="Ernesta Kareckaitė vs Nicolle Caliari",
    fighter1="Ernesta Kareckaitė",
    fighter2="Nicolle Caliari",
    fighter1_ml=-110,
    fighter2_ml=-110,
    fighter1_props={"Decision": 130, "TKO": 240, "Submission": 320},
    fighter2_props={"Decision": 150, "TKO": 230, "Submission": 340},
    rounds=3.0,
    outcome=["TBD"]
)

Test_Card = card = Card(
    fights=[fight1, fight2, fight3, fight4, fight5, fight6, fight7, fight8, fight9, fight10, fight11],  # List of Fight instances
    date=datetime.date(2024, 12, 25)  # Example date
)
test_picks = Picks([],Test_Card,50,0)
Test_User1 = Person("Kai","1234",test_picks,[],79,14)

interface(Test_User1,Test_Card)
