#Definindo uma classe simples

##age default = 0 
class User:
    #class attribute that is defined only once.
    active_users = 0

    #Class Methods --> not an instance --> the actual class user
    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."
        
    def __init__(self,first,last,age = 0):
        self.first = first
        self.last = last
        self.age = age
        User.active_users+=1

    def logout(self):
        User.active_users -=1
        return f"{self.first} has logged out."
    
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self,thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >=65 #boolean expression true or false.

    def birthday(self):
        self.age +=1
        return f"Happy {self.age}th, {self.first}"


#user1 eh objeto da classe User
#instanciando a classe abaixo ->

user1 = User("Joe","Smith",68)
user2 = User("Blanca","Lopez",41)
# print(user1.is_senior())
# print(user1.birthday())
# print(user1.likes("Ice Cream"))
# print(user2.initials())
# print(user2.full_name())

#print("Currently we have {} active users".format(User.active_users))
#print(user2.logout())
#print("Currently we have {} active users" .format(User.active_users))

print(User.display_active_users())
