import unittest
from fight import Fight
from card_constructor import Card

class TestFight(unittest.TestCase):
    def setUp(self):
        # Setup a Fight instance
        self.fight = Fight(
            name="Main Event",
            fighter1="Fighter A",
            fighter2="Fighter B",
            fighter1_ml=-150,
            fighter2_ml=130,
            fighter1_props={"reach": 70, "height": 180},
            fighter2_props={"reach": 68, "height": 175},
            rounds=5.0,
            outcome=[]
        )

    def test_initialization(self):
        # Test initial attributes
        self.assertEqual(self.fight.name, "Main Event")
        self.assertEqual(self.fight.fighter1, "Fighter A")
        self.assertEqual(self.fight.fighter2, "Fighter B")
        self.assertEqual(self.fight.fighter1_ml, -150)
        self.assertEqual(self.fight.fighter2_ml, 130)
        self.assertEqual(self.fight.fighter1_props["reach"], 70)
        self.assertEqual(self.fight.fighter2_props["height"], 175)
        self.assertEqual(self.fight.rounds, 5.0)
        self.assertEqual(self.fight.outcome, [])

    def test_update_outcome(self):
        # Test updating the outcome
        new_outcome = ["KO", "Round 3"]
        self.fight.update_outcome(new_outcome)
        self.assertEqual(self.fight.outcome, new_outcome)

    def test_update_outcome_invalid(self):
        # Test invalid outcome update
        with self.assertRaises(ValueError):
            self.fight.update_outcome("Invalid Outcome")


class TestCard(unittest.TestCase):
    def setUp(self):
        # Setup Card with multiple fights
        self.fight1 = Fight(
            name="Main Event",
            fighter1="Fighter A",
            fighter2="Fighter B",
            fighter1_ml=-150,
            fighter2_ml=130,
            fighter1_props={"reach": 70, "height": 180},
            fighter2_props={"reach": 68, "height": 175},
            rounds=5.0,
            outcome=[]
        )
        self.fight2 = Fight(
            name="Co-Main Event",
            fighter1="Fighter C",
            fighter2="Fighter D",
            fighter1_ml=-110,
            fighter2_ml=100,
            fighter1_props={"reach": 72, "height": 185},
            fighter2_props={"reach": 71, "height": 182},
            rounds=3.0,
            outcome=[]
        )
        self.card = Card(fights=[self.fight1, self.fight2])

    def test_initialization(self):
        # Test Card initialization
        self.assertEqual(len(self.card.fights), 2)
        self.assertEqual(self.card.fights[0].name, "Main Event")
        self.assertEqual(self.card.fights[1].name, "Co-Main Event")

    def test_update_outcomes(self):
        # Test updating outcomes
        new_outcome = ("Main Event", ["KO", "Round 3"])
        self.card.update_outcomes(new_outcome)
        self.assertEqual(self.card.fights[0].outcome, ["KO", "Round 3"])

    def test_update_outcomes_invalid_fight(self):
        # Test updating outcome for a non-existent fight
        with self.assertRaises(ValueError):
            self.card.update_outcomes(("Non-existent Fight", ["Decision", "Round 5"]))

if __name__ == "__main__":
    unittest.main()
