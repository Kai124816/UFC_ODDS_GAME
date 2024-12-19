from User.predictions import Picks
import bcrypt

class Person:
    """
    A class to manage user profiles for the betting application.

    Attributes:
    username (str): The user's unique username.
    password (str): The hashed password for user authentication.
    picks (Picks): The user's current betting activity.
    pick_history (list[Picks]): A history of all past betting activities.
    total_payout (int): The total amount of payouts received.
    total_profit (int): The total profit earned from bets.
    """

    def __init__(self, username: str, password: str, current_picks: Picks = None, pick_history: list[Picks] = None,
                 total_revenue: int = 0, total_profit: int = 0) -> None:
        """
        Initialize a Person instance.

        Args:
        username (str): The user's unique username.
        password (str): The plain-text password (will be hashed).
        current_picks (Picks): The user's current picks.
        pick_history (list[Picks], optional): A list of previous Picks objects. Defaults to None.
        total_payout (int, optional): The total payout amount. Defaults to 0.
        total_profit (int, optional): The total profit amount. Defaults to 0.
        """
        self.username = username
        self.password = self._hash_password(password)
        self.picks = current_picks
        self.pick_history = pick_history if pick_history else []
        self.total_revenue = total_revenue
        self.total_profit = total_profit

    @staticmethod
    def _hash_password(password: str) -> str:
        """
        Hash a plain-text password.

        Args:
        password (str): The plain-text password.

        Returns:
        str: The hashed password.
        """
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def change_password(self, new_password: str) -> None:
        """
        Change the user's password.

        Args:
        new_password (str): The new plain-text password.
        """
        self.password = self._hash_password(new_password)

    def verify_password(self, password: str) -> bool:
        """
        Verify a given password against the stored hashed password.

        Args:
        password (str): The plain-text password to verify.

        Returns:
        bool: True if the password is correct, False otherwise.
        """
        return bcrypt.checkpw(password.encode(), self.password.encode())

        