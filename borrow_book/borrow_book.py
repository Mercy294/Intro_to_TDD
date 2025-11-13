def borrow_book(book_title, available_books):
    if book_title in available_books:
        available_books.remove(book_title)
        return f"You have borrowed '{book_title}'."
    else:
        return f"Sorry, this '{book_title}' is not available."


