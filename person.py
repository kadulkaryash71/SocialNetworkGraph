class Person:
    def __init__(self, name, age, year, institute, designation):
        self.name = name
        self.age = age
        self.year = year
        self.institute = institute
        self.designation = designation
        self._friends = set()

    def add_friend(self, Person, Network):
        self._friends.add(Person.name)
        Network.add_node(self.name, Person.name)
        return f"{Person.name} was added to your friend list!"
    
    def remove_friend(self, Person, Network):
        self._friends.remove(Person.name)
        Network.remove_node(self.name, Person.name)
        return f"Friend {Person.name} removed."
    
    def friend_check(self, Person):
        return f"{Person.name} is {self.name}'s friend" if Person.name in self._friends else f"{Person.name} not found."

    def get_friends(self):
        return self._friends
    
    def __str__(self):
        return f"""Your name is {self.name}
Your age is {self.age}
You are in {self.year}
You work as a {self.designation}
"""
