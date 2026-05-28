#Exercise 1: Quizz

#"What is a class?
#A blueprint used to create objects.

#What is an instance?
#An individual object created from a class.

#What is encapsulation?
#Hiding internal data and restricting direct access.

#What is abstraction?
#Hiding complex details and showing only essentials.

#What is inheritance?
#A subclass deriving properties from a parent class.

#What is multiple inheritance?
#A subclass inheriting from more than one parent class.

#What is polymorphism?
#Different classes using the same method name with different behaviors.

#What is method resolution order or MRO?
#The order Python uses to search for methods in inheritance.


#Exercise 2: Create a deck of cards class

import random

class Card :
    def __init__(self, suit, value) :
        self.suit = suit
        self.value = value

    def __repr__(self) :
        return f"{self.value} of {self.suit}"


class Deck :
    def __init__(self) :
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = []
        self.reset_deck()

    def reset_deck(self) :
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]

    def shuffle(self) :
        if len(self.cards) != 52 :
            self.reset_deck()
        random.shuffle(self.cards)

    def deal(self) :
        if len(self.cards) == 0 :
            print("Error : No cards left in the deck.")
            return None
        return self.cards.pop()
    


if __name__ == "__main__" :

    my_deck = Deck()
    print(f"Initial deck size : {len(my_deck.cards)}")

    my_deck.shuffle()
    print("Deck shuffled successfully.")

    print("\nDealing 5 Cards")
    for i in range(1, 6) :
        card = my_deck.deal()
        print(f"Card {i} dealt : {card}")
    print(f"\nRemaining deck size : {len(my_deck.cards)}")

    print("\n--- Dealing remaining cards until empty ---")
    while len(my_deck.cards) > 0 :
        my_deck.deal()
    my_deck.deal()

