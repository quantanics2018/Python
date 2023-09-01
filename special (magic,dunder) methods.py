class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        total_pages = self.pages + other.pages
        return Book(f"{self.title} + {other.title}", self.author, total_pages)

# Creating book objects
book1 = Book("Python Crash Course", "Eric Matthes", 560)
book2 = Book("Deep Learning", "Ian Goodfellow", 800)

# Using special methods
print(book1)         # Output: Python Crash Course by Eric Matthes
print(len(book1))    # Output: 560

combined_book = book1 + book2
print(combined_book)  # Output: Python Crash Course + Deep Learning by Eric Matthes
print(len(combined_book))  # Output: 1360
