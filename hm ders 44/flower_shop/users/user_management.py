class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        
    def __str__(self):
        return f"{self.user_id} - {self.name}"

class UserManager:
    def __init__(self):
        self.users = []
        
    def add_user(self, user_id, name):
        new_user = User(user_id, name)
        self.users.append(new_user)
        return new_user
    
    def fin_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None