from user_queries import user_to_SQL,update_revenue_and_profit,update_password,update_username,SQL_to_user,delete_user
from User.profile import Person

password = "my_secure_password"

test_user = Person("kai",password,None,None,0,0)
user_to_SQL(test_user)

test_user.total_profit = 50
test_user.total_revenue = 83
update_revenue_and_profit(test_user)

new_password = "my_new_password"
update_password(test_user,new_password)

test_user.username = "peter"
update_username(test_user)

test_user2 = Person
SQL_to_user(test_user2,"peter")

delete_user("peter")



