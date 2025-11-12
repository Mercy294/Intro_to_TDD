from borrow_book import borrow_book


def test_borrow_book_available():
    available_books = ["The Maze Runner", "The Hunger Games", "Percy Jackson"]
    result = borrow_book("The Maze Runner", available_books)
    assert result == "You have borrowed 'The Maze Runner'."
    assert "The Maze Runner" not in available_books


def test_borrow_book_unavailable():
    available_books = ["The Maze Runner", "The Hunger Games", "Percy Jackson"]
    result = borrow_book("Twilight", available_books)
    assert result == "Sorry, 'Twilight' is not available."
    assert "Twilight" not in available_books


def test_borrow_book_updates_list():
    available_books = ["The Maze Runner", "The Hunger Games", "Percy Jackson"]
    result = borrow_book("Percy Jackson", available_books)
    assert result == "You have borrowed 'Percy Jackson'."
    assert "Percy Jackson" not in available_books
    

def test_borrow_book_empty_list():
    available_books = []
    result = borrow_book("The Maze Runner", available_books)
    assert result == "Sorry, 'The Maze Runner' is not available."
    assert "The Maze Runner" not in available_books
