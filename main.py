from network import Network
from person import Person
import pickle

facebook = Network("Facebook")

jack = Person("jb500", "Jack Bauer", 22, "Grade 12", "Dublin City University", "Research Assistant")
skylar = Person("skylarg_10", "Skylar Gray", 25, "Second Year", "Trinity College Dublin", "Professor")
leslie = Person("lesliewhite_", "Leslie White", 24, "First Year", "Massachusettes Institute of Technology", "Student")
brock = Person("bmonaghan", "Brock Monaghan", 28, "Graduate", "Dublin City University", "Alumni")

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

# TEST: SERIALIZATION
with open(f'serialized/obj_1.pkl', 'wb') as f:
    pickle.dump(facebook, f)
    f.close()
