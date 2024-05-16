from typing import List, Dict
from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str: [str]] = {}      # {"Steven King": ["Living torch", "Misery", "The long walk"]}
        self.rented_books: Dict[str: Dict[str: int]] = {}      # {"John": {"East of heaven": 15}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)                  # TAKE the book from library
            user.books.append(book_name)                                  # add book_name to his book list
            if user.username not in self.rented_books:          # if no such username: CREATE a dict inside of dict
                self.rented_books[user.username] = {book_name: days_to_return}
            else:        # else (if already user.username registered), just UPDATE the nested dict !!
                self.rented_books[user.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        return f'The book "{book_name}" is already rented and will be available in ' \
               f'{self.rented_books[user.username][book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            book_to_return = user.books.pop(user.books.index(book_name))
            del self.rented_books[user.username][book_name]
            self.books_available[author].append(book_to_return)
        return f"{user.username} doesn't have this book in his/her records!"