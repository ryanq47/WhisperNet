import DataEngine.AuthenticationDBHandler
import SecurityEngine.AuthenticationHandler

'''
db.create_api_user(
    username="username",
    password_blob="blob"
)

db.add_api_role(
    username="username",
    roles=["iam_admin","iam_user"]
)

roles = db.get_all_api_user_roles(
    username="username"
)


print("Rolls of user")

print(roles)

users_with_roll = db.get_api_users_with_role(
    role_name="iam_admin"
)

print("Users with roll")
print(users_with_roll)
'''
#db = DataEngine.AuthenticationDBHandler.AuthenticationSQLDBHandler(db_path="DataBases/users.db")
#db.nuke_and_recreate_db()


print("create user")
SecurityEngine.AuthenticationHandler.UserManagement.create_user(
    path_struct="a",
    username = "username",
    password="1234",
    roles=["iam_admin"]
)


print("get roles:")
roles2 = SecurityEngine.AuthenticationHandler.Authentication.api_get_user_role(
    username = "username",

)

print(roles2)


'''
## need to fix these ones, select each item's 2nd attribute

Prolly should do in the AuthDBHandler and just have it return a list
of roles

Rolls of user
[('username', 'iam_admin'), ('username', 'iam_user')]
Users with roll
[('username', 'iam_admin')]

'''