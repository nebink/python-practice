class BookStore:
    noOfBooks = 0
    
    def __init__(self, title, author, publisher, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price
        BookStore.noOfBooks += 1
    
    def BookInfo(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publisher: {self.publisher}")
        print(f"Price: {self.price}")
        
# Example usage
book1 = BookStore("The Alchemist", "Paulo Coelho", "HarperCollins", 10.99)
book2 = BookStore("To Kill a Mockingbird", "Harper Lee", "J. B. Lippincott & Co.", 8.99)

book1.BookInfo()
book2.BookInfo()

print(f"Total number of books: {BookStore.noOfBooks}")
