import csv
from friend import Friend

class FriendRepository:
    def __init__(self, filename):
        self.filename = filename

    def get_all_friends(self):
        friends = []
        with open(self.filename, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                friends.append(Friend(row['last_name'], row['first_name'], row['date_of_birth'], row['email']))
        return friends
