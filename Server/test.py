import DataEngine.AuthenticationDBHandler


db = DataEngine.AuthenticationDBHandler.AuthenticationSQLDBHandler(db_path="DataBases/users.db")
db.nuke_and_recreate_db()
db.create_api_user(
    username="username",
    password_blob="blob"
)

db.add_api_role(
    username="username",
    roles=["iam_admin"]
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
