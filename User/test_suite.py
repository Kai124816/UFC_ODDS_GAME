import unittest
from predictions import Picks, BetExceedsBudgetError, ContradictoryBetsError, InsufficientBetsError
from User.profile import Person
from Fight_Card.card_constructor import Card
from Fight_Card.fight import Fight


class TestPicks(unittest.TestCase):
    def setUp(self):
        # Create a sample fight card
        self.fights = [
            Fight(
                name="Fight 1",
                fighter1="Fighter A",
                fighter2="Fighter B",
                fighter1_ml=-150,
                fighter2_ml=130,
                fighter1_props={"KO": +200},
                fighter2_props={"KO": +250},
                rounds=3.0,
                outcome=["Fighter A", "KO"]
            ),
            Fight(
                name="Fight 2",
                fighter1="Fighter C",
                fighter2="Fighter D",
                fighter1_ml=-200,
                fighter2_ml=170,
                fighter1_props={"Decision": +100},
                fighter2_props={"Decision": +300},
                rounds=5.0,
                outcome=["NC"]
            ),
        ]
        self.card = Card(self.fights)
        self.picks = Picks(picks=[], card=self.card, remaining_budget=500, payout=0)

    def test_make_pick_success(self):
        self.picks.make_pick(fighter="Fighter A", method="KO", amount=100)
        self.assertEqual(len(self.picks.picks), 1)
        self.assertEqual(self.picks.remaining_budget, 400)

    def test_make_pick_exceeds_budget(self):
        with self.assertRaises(BetExceedsBudgetError):
            self.picks.make_pick(fighter="Fighter A", method="KO", amount=600)

    def test_make_pick_insufficient_bets(self):
        self.picks.make_pick(fighter="Fighter A", method="KO", amount=490)
        with self.assertRaises(InsufficientBetsError):
            self.picks.make_pick(fighter="Fighter C", method="Decision", amount=10)

    def test_make_pick_contradictory_bets(self):
        self.picks.make_pick(fighter="Fighter A", method="KO", amount=100)
        with self.assertRaises(ContradictoryBetsError):
            self.picks.make_pick(fighter="Fighter B", method="Decision", amount=50)

    def test_update_picks_outcomes(self):
        self.picks.make_pick(fighter="Fighter A", method="KO", amount=100)
        self.picks.update_picks(self.fights[0])
        self.assertEqual(self.picks.picks[0][2], "Hit")
        self.assertGreater(self.picks.payout, 0)

    def test_remove_pick(self):
        self.picks.make_pick(fighter="Fighter A", method="KO", amount=100)
        self.picks.remove_pick(self.picks.picks[0])
        self.assertEqual(len(self.picks.picks), 0)
        self.assertEqual(self.picks.remaining_budget, 400)


class TestPerson(unittest.TestCase):
    def setUp(self):
        # Create sample Picks object
        self.picks = Picks(picks=[], card=None, remaining_budget=500, payout=0)
        self.person = Person(
            username="test_user",
            password="secure_password",
            current_picks=self.picks,
            pick_history=[],
            total_payout=1000,
            total_profit=200
        )

    def test_password_hashing(self):
        # Ensure password is hashed
        self.assertNotEqual(self.person.password, "secure_password")
        self.assertTrue(self.person.verify_password("secure_password"))
        self.assertFalse(self.person.verify_password("wrong_password"))

    def test_change_password(self):
        self.person.change_password("new_password")
        self.assertTrue(self.person.verify_password("new_password"))
        self.assertFalse(self.person.verify_password("secure_password"))

    def test_profile_attributes(self):
        self.assertEqual(self.person.username, "test_user")
        self.assertEqual(self.person.total_payout, 1000)
        self.assertEqual(self.person.total_profit, 200)

    def test_pick_history(self):
        self.person.pick_history.append(self.picks)
        self.assertEqual(len(self.person.pick_history), 1)
        self.assertIs(self.person.pick_history[0], self.picks)


if __name__ == "__main__":
    unittest.main()
