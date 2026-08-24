class UserNotFoundError(Exception):
    pass
def fetch_user(user_id):
    user = None
    if user == None:
        raise UserNotFoundError(f'User {user_id} not in database')
    else:
        return user
users = [123, 456, 789]
for user_id in users:
    try:
        fetch_user(user_id)
    except UserNotFoundError as e:
        print("There was an error: ", e)
