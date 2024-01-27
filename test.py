from person import Person
from network import Network

reddit = Network("Reddit")

# TEST: NETWORK SERIALIZATION
jack = Person("jb500", "Jack Bauer", 22, "Grade 12", "Dublin City University", "Research Assistant")
skylar = Person("skylarg_10", "Skylar Gray", 25, "Second Year", "Trinity College Dublin", "Professor")
leslie = Person("lesliewhite_", "Leslie White", 24, "First Year", "Massachusettes Institute of Technology", "Student")
minge = Person("mab__007", "Minge Abrahams", 23, "Third Year", "Dublin City University", "Student")

jack.add_friend(minge, reddit)
skylar.add_friend(minge, reddit)
skylar.add_friend(leslie, reddit)
leslie.add_friend(jack, reddit)

reddit.show_network()