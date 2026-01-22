class Author: # define the class as author
    def __init__(self,name):
        self.name =name # store the names of th Authors
        self.books=[] # create empty list for books published
    def publish(self,title):
        if title in self.books:
            print(f"Error: '{title}' has already been added to  {self.name} List of published books.")
        else:
            self.books.append(title)
            print(f"{self.name} published '{title}'.")



    def __str__(self):
        return f'Name: {self.name}  Books: {self.books}'




Orwell = Author ('George Orwell')
Orwell.publish('1984')
Orwell.publish('Animal Farm')

print(Orwell)
Dostoevsky = Author ('Fyodor Dostoevsky')
Dostoevsky.publish('White Nights')
Dostoevsky.publish('The Idiot')
Dostoevsky.publish('Demons')
Dostoevsky.publish('Demons')
print(Dostoevsky)

