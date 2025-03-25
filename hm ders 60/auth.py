class Authentiactor:
    def __init__(self):
        self.users = {"metehan": "gamerboy", "semanur": "gamergirl"}

    def login(self, username, password):
        if username not in self.users:
            return False
        return self.users[username] == password