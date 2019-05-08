class User():
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.books = []

  def get_email(self):
    return self.email

  def change_email(self, address):
    self.email = address
    print("Email address of {name} has been changed to {address}".format(
        name=self.name, address=address))

  def __repr__(self):
    return "User {name}, email: {email}, books read: {num_read_books}".format(
        name=self.name, email=self.email, num_read_books=len(self.books))

  def __eq__(self, other_user):
    return self.name == other_user.name and self.email == other_user.email

  def read_book(self, book, rating=None):
    self.books.append({book:rating})

  def get_average_rating(self):
    return (sum([i for j in self.books for i in j.values() if i is not None])) / len(self.books)

class Book():
  def __init__(self, title, isbn, price):
    self.title = title
    self.isbn = isbn
    self.ratings = []
    self.price = price

  def get_title(self):
    return self.title

  def get_isbn(self):
    return self.isbn

  def add_rating(self, rating):
    if rating is None:
      print("No rating given for book {}".format(self.title))
    elif rating >= 0 and rating <= 4:
      self.ratings.append(rating)
    else:
      print("Invalid Rating {} for book {}".format(rating, self.title))

  def get_average_rating(self):
    return (sum(self.ratings)) / len(self.ratings)

  def __hash__(self):
    return hash((self.title, self.isbn))

  def __repr__(self):
    return "Book titled {title}".format(title=self.title)

class Fiction(Book):
  def __init__(self, title, author, isbn, price):
    super().__init__(title, isbn, price)
    self.author = author

  def get_author(self):
    return self.author

  def __repr__(self):
    return "{title} by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):
  def __init__(self, title, subject, level, isbn, price):
    super().__init__(title, isbn, price)
    self.subject = subject
    self.level = level

  def get_subject(self):
    return self.subject

  def get_level(self):
    return self.level

  def __repr__(self):
    return "{title}, a {level} manual on {subject}".format(
        title=self.title, level=self.level, subject=self.subject)

class TomeRater():
  def __init__(self):
    self.users = {}
    self.books = {}

  def __repr__(self):
    return """
    <TomeRater Object containing
    {users}
    {books}
    >""".format(users=self.users, books=self.books)

  def __eq__(self, other):
    return (
        self.users == other.users and
        self.books == other.books
        )

  def create_book(self, title, isbn, price):
    if not isbn in [i.isbn for i in self.books.keys()]:
      book = Book(title, isbn, price)
      self.books[book] = 0
      return book
    else:
      print("ISBN is already taken!")
      return None

  def create_novel(self, title, author, isbn, price):
    if not isbn in [i.isbn for i in self.books.keys()]:
      book = Fiction(title, author, isbn, price)
      self.books[book] = 0
      return book
    else:
      print("ISBN is already taken!")
      return None

  def create_non_fiction(self, title, subject, level, isbn, price):
    if not isbn in [i.isbn for i in self.books.keys()]:
      book = Non_Fiction(title, subject, level, isbn, price)
      self.books[book] = 0
      return book
    else:
      print("ISBN is already taken!")
      return None

  def set_isbn(self, book, new_isbn):
    if new_isbn not in [i.isbn for i in self.books.keys()]:
      book.isbn = new_isbn
      print("The ISBN of {name} has changed to {new_isbn}".format(
          name=book.title, new_isbn=new_isbn))
    else:
      print("ISBN is already taken!")

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
    if email in self.users.keys():
      print('Email already exists!')
      return None
    if '@' in email and ('.com' in email or '.edu' in email or '.org' in email):
      new_user = User(name, email)
      self.users[email] = new_user
      if user_books:
        for i in user_books:
          self.add_book_to_user(i, email)
      return None
    else:
      print("Invalid email address!")
      return None

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

  def get_n_most_read_books(self, n):
    if len(self.books) >= n:
      sorted_list = sorted(self.books.keys(), key=self.books.get)
      sorted_list.reverse()
      return sorted_list[:n]
    print("There is only {} books in TomeRater!".format(len(self.books)))
    return None

  def get_n_most_prolific_readers(self, n):
    if len(self.users) >= n:
      new_dict = {i.email:len(i.books) for i in self.users.values()}
      sorted_list = sorted(new_dict.keys(), key=new_dict.get)
      sorted_list.reverse()
      return sorted_list[:n]
    print("There is only {} users in TomeRater!".format(len(self.users)))
    return None

  def get_n_most_expensive_books(self, n):
    if len(self.books) >= n:
      new_dict = {i.title:i.price for i in self.books.keys()}
      sorted_list = sorted(new_dict, key=new_dict.get)
      sorted_list.reverse()
      return sorted_list[:n]
    print("There is only {} books in TomeRater!".format(len(self.books)))
    return None

  def get_worth_of_user(self, user_email):
    if user_email in self.users.keys():
      user = self.users[user_email]
      books_cost = [i.price for j in user.books for i in j]
      return sum(books_cost)
    print("There is no such user!")
    return None
