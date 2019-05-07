from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678, 21)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345, 223)
Tome_Rater.set_isbn(novel1, 9781536831139)
# ISBN is already taken
Tome_Rater.set_isbn(book1, 9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452, 123)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938, 65)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010, 73)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000, 36)
# ISBN is already taken
novel4 = Tome_Rater.create_novel(
    "There Will Come Soft Rains", "Ray Bradbury", 10001000, 98)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.bobo",
                    user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

# These are equal
Tome_Rater2 = TomeRater()
Tome_Rater3 = TomeRater()
Tome_Rater2.add_user("Marvin Minsky", "marvin@mit.edu",
                     user_books=[book1, novel1, nonfiction1])
Tome_Rater3.add_user("Marvin Minsky", "marvin@mit.edu",
                     user_books=[book1, novel1, nonfiction1])
print(Tome_Rater3 == Tome_Rater2)

# These are not equal
Tome_Rater2 = TomeRater()
Tome_Rater3 = TomeRater()
novel2_2 = Tome_Rater2.create_novel(
    "The Diamond Age", "Neal Stephenson", 10101010, 20)
novel2_3 = Tome_Rater3.create_novel(
    "The Diamond Age", "Neal Stephenson", 10101010, 20)
Tome_Rater2.add_user("Marvin Minsky", "marvin@mit.edu",
                     user_books=[book1, novel2_2, nonfiction1])
Tome_Rater3.add_user("Marvin Minsky", "marvin@mit.edu",
                     user_books=[book1, novel2_3, nonfiction1])
print(Tome_Rater3 == Tome_Rater2)

print(Tome_Rater.get_n_most_read_books(6))
print(Tome_Rater.get_n_most_prolific_readers(3))
print(Tome_Rater.get_n_most_expensive_books(5))
print(Tome_Rater.get_worth_of_user("marvin@mit.edu"))

#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())
