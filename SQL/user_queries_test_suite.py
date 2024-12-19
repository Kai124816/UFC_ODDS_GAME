import sys
from user_queries import user_to_SQL,update_revenue_and_profit,update_password,update_username,SQL_to_user
sys.path.append("../")
from User.profile import Person
import bcrypt

password = "my_secure_password"
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

test_user = Person("kai",hashed_password,None,None,0,0)
user_to_SQL(test_user)

test_user.total_profit = 50
test_user.total_revenue = 83
update_revenue_and_profit(test_user)

new_password = "my_new_password"
salt = bcrypt.gensalt()
new_hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
update_password(test_user,new_hashed_password)

test_user.username = "peter"
update_username(test_user)




