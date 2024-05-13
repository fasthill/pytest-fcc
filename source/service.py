import requests

database = {
    1: "Alice",
    2: "Bob",
    3: "Charlie",
}

def get_user_from_db(user_id):
    print("database:", database.get(user_id))
    return database.get(user_id)

# 1시간 4분 이후 교육, https://www.youtube.com/watch?v=cHYq1MRoyI0