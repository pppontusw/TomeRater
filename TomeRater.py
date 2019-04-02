class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = []

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Email address of {name} has been changed to {address}".format(name=self.name, address=address))

    def __repr__(self):
        return "User {name}, email: {email}, books read: {num_read_books}".format(name=self.name, email=self.email, num_read_books=len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating=None):
        self.rating = rating
        self.books.append({book:rating})

    def get_average_rating(self):
        return (sum([i for j in self.books for i in j.values() if i is not None])) / len(self.books)

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new):
        self.isbn = new
        print("The ISBN of {name} has changed to {new_isbn}".format(name=self.title, new_isbn=new))

    def add_rating(self, rating):
        if rating is not None and rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        return (sum(self.ratings)) / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    
    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title,isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            user = self.users.get(email)
            user.read_book(book, rating)
            book.add_rating(rating)
            book_in_books_dict = self.books.get(book, False)
            if book_in_books_dict:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {email}!".format(email=email))

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
            for i in user_books:
                self.add_book_to_user(i, email)

    def print_catalog(self):
        for i in self.books.keys():
            print(i)

    def print_users(self):
        for i in self.users.values():
            print(i)

    def most_read_book(self):
        amount_of_reads = float("-inf")
        for k,v in self.books.items():
            if v > amount_of_reads:
                most_read_book = k
                amount_of_reads = v
        return most_read_book

    def highest_rated_book(self):
        highest_rating = float("-inf")
        for book in self.books.keys():
            j = book.get_average_rating()
            if j > highest_rating:
                highest_rating = j
                highest_rated_book = book
        return highest_rated_book

    def most_positive_user(self):
        highest_avg_rating = float("-inf")
        for user in self.users.values():
            avg_rating = user.get_average_rating()
            if avg_rating > highest_avg_rating:
                highest_avg_rating = avg_rating
                highest_avg_rating_user = user
        return highest_avg_rating_user
