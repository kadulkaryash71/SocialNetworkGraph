import weakref

class Person:
    instances = []  # an array to save all the instances to memory
    
    def __init__(self, user_id, name, age, year, institute, designation):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.year = year
        self.institute = institute
        self.designation = designation
        self._friends = set()
        self.__class__.instances.append(weakref.proxy(self))

    # creating linkage of users in the given Network based on their User IDs
    def add_friend(self, Person, Network):
        self._friends.add(Person.user_id)
        Network.add_node(self.user_id, Person.user_id)
        return f"{Person.name} was added to your friend list!"
    
    # remove linkage between the requesting user and requested user in the Network
    def remove_friend(self, Person, Network):
        self._friends.remove(Person.user_id)
        Network.remove_node(self.user_id, Person.user_id)
        return f"Friend {Person.name} removed."
    
    # checks if the requesting user if friends with the requested user
    # the function can be useful when users are searching for people in their own friends list (friends list of others is supposedly private)
    def friend_check(self, Person):
        return f"{Person.name} is {self.name}'s friend" if Person.user_id in self._friends else f"{Person.name} not found."

    def get_friends(self):
        return self._friends
    
    # to view the requesting user's data
    def __str__(self):
        return f"""Your name is {self.name}
Your age is {self.age}
You are in {self.year}
You work as a {self.designation}
"""
