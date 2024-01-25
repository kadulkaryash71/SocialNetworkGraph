from network import Network
from person import Person

facebook = Network("Facebook")

jack = Person("Jack Bauer", 22, "Grade 12", "Dublin City University", "Research Assistant")
skylar = Person("Skylar Gray", 25, "Second Year", "Trinity College Dublin", "Professor")
leslie = Person("Leslie White", 24, "First Year", "Massachusettes Institute of Technology", "Student")
brock = Person("Brock Monagha", 28, "Graduate", "Dublin City University", "Alumni")

print(jack)
print(facebook)

### TEST: ADD FRIEND

jack.add_friend(skylar, facebook)
jack.add_friend(leslie, facebook)
print(jack.get_friends())
print(facebook)

brock.add_friend(jack, facebook)
print(facebook)

leslie.add_friend(brock, facebook)
print(facebook)

skylar.add_friend(leslie, facebook)
print(facebook)


### TEST: REMOVE FRIEND

jack.remove_friend(skylar, facebook)
print(jack.get_friends())
print(facebook)


# TEST: FRIEND CHECK
print(jack.friend_check(skylar))


# TEST: SHOW NETWORK
facebook.show_network()
