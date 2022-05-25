
class Book:
    """A book in a collection."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def getBook(self):
        return f'{self.title}, by {self.author}'

class Library:
    """A collection of books"""
    def __init__(self):
        self.Will = Book('Will', 'Will Smith')
        self.TBC = Book('The Bone Collector', 'Jeffery Deaver')
    
    def getCollection(self):
        will = self.Will.getBook()
        tbc = self.TBC.getBook()
        return will, tbc


def main():
    library = Library()
    List_of_Books = library.getCollection()
    print(List_of_Books)


if __name__ == "__main__":
    main()
