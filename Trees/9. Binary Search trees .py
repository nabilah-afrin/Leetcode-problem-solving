#Binary Search Trees 
class User: 
    def __init__(self, user_name, full_name , mail_id) -> None:
        self.username = user_name
        self.name = full_name
        self.email = mail_id
        print("Hello " + str(user_name) + " welcome to our service! ")
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    def __str__(self):
        return self.__repr__()
    def introduction(self, guest_name):
        print("hello {}, I'm {}, Contact me at {}" .format(guest_name, self.name, self.email))

class UserDatabase:
    def insert(self, user): pass
    def find(self, username):pass
    def update(self, user):pass
    def list_all(self):pass

class UserDatabase:
    def __init__(self) -> None: #constructor, that doesnt take anything except self
        self.total_users= []
    def insert(self, user):
        i = 0 #whre was no user
        while i < len(self.total_users):
            if self.total_users[i].username > user.username:
                break
            i += 1
        self.total_users.insert(i, user)
    def find(self, user_name):
        for user in self.total_users:
            if user.username == user_name: 
                return user
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email == user.name, user.email
    def user_list(self):
        return self.total_users

user_1 = User("bonito_flakes", "Nabilah Afrin", "afrinshwati@gmail.com")
database = UserDatabase()
database.insert(bonito_flakes)
database.update(User(username='bonito_flakes', name='Siddhant U', email='siddhantu@example.com'))
    