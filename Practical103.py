class Library:
    def __init__(self, acc_number, title, author):
        self.acc_number = acc_number
        self.title = title
        self.author = author

    def read(self):
        print("Book Details:")
        print("Accession Number:", self.acc_number)
        print("Title:", self.title)
        print("Author:", self.author)

    def compute_fine(self, days_late):
        fine = days_late * 15
        print("Fine Charged:", fine)

# Example usage:
book = Library(1234, "Python Programming", "John Doe")
book.read()
book.compute_fine(5)
