class bookshelf:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def __len__(self):
        return len(self.books)
    def __str__(self):
        return f"Bookshelf contains: {', '.join(self.books)}" 
    def __repr__(self):
        return f"Bookshelf( books={len(self.books)})"
    def __eq__(self, other):
        if isinstance(other, bookshelf):
            return self.books == other.books
        return False
    def __hash__(self):
        return hash(tuple(self.books))
    
shelf1 = BookShelf()
shelf1.add_book("Война и мир")
shelf1.add_book("Преступление и наказание")
shelf2 = BookShelf()
shelf2.add_book("Преступление и наказание")
shelf2.add_book("Война и мир")
print(len(shelf1))
print(str(shelf1))
print(shelf1 == shelf2)
    
import random

class Deck:
    def __init__(self):
        self.cards = []
    
   
    def __len__(self):
        print(len(self.cards))
        return len(self.cards)
    
    def __str__(self):
        return f"Deck contains: {', '.join(self.cards)}"
    
    def __repr__(self):
        return f"Deck(cards={len(self.cards)})"
    
    def __eq__(self, other):

        if isinstance(other, Deck):
            for i in range(len(self.cards)):
                if self.cards[i] not in other.cards:
                    return False
            print("True")
        return False

    def add_card(self, card):
        self.cards.append(card)
        print(f"{self.cards} is added")
        return self.cards
    
    def shuffle(self):
        random.shuffle(self.cards)
        print(f"Deck is shuffled: {', '.join(self.cards)}")
        return self.cards
    
    def draw(self):
        if self.cards:
            print(f"Drawing card: {self.cards[-1]}")
            return self.cards.pop()
        return None 
    
deck1 = Deck()
deck1.add_card("Туз пик")
deck1.add_card("Король червей")
deck2 = Deck()
deck2.add_card("Туз пик")
deck2.add_card("Король червей")
print(len(deck1))
print(deck1 == deck2)
deck2.shuffle()
print(deck1 == deck2)
    
class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
    
    def __str__(self):
        polinom = ""
        for i in self.coefficients:
            if i != 0:
                polinom += (f"{i}x^{self.coefficients.index(i)} + ")
        polinom = polinom[:-3]  
        return polinom

    def __repr__(self):
        return f"Polynomial(coefficients={self.coefficients})"
    
    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.coefficients == other.coefficients
        return False
    
    def __len__(self):
        return len(self.coefficients)
    
    def __hash__(self):
        return hash(tuple(self.coefficients))
    
p1 = Polynomial([3, 2, 1])
p2 = Polynomial([3, 2, 1])
p3 = Polynomial([1, 2, 3])
print(str(p1))
print(repr(p1))
print(p1 == p2)
print(p1 == p3)
print(len(p1))