import random

suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
rank_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, '10': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}


class Card:
    def __init__(self, suit=None, rank=None):
        # assert suit in suits
        self.suit = suit
        # assert rank in ranks
        self.rank = rank

    def __str__(self):
        """
        Dunder method to return a human-readable string, e.g. in the print function
        @return: str
        """
        return f'{self.rank} of {self.suit}'


class CardDeck:
    def __init__(self):
        # Stored cards
        self.deck_stored = []
        # Drawn cards
        self.deck_drawn = []
        # Deck (list of all cards) is initialized when the class the instance is created
        self.create_deck()

    def create_deck(self):
        """
        Creates a regular 52 card deck when CardDeck is initialized
        stores it in self.deck_stored
        @return: None
        """
        for s in suits:
            for r in ranks:
                self.deck_stored.append(Card(suit=s, rank=r))
        return

    def shuffle(self):
        """
        Shuffles the card in self.deck_stored
        @return: None
        """
        random.shuffle(self.deck_stored)
        return

    def get_number_of_cards_remaining(self):
        """
        Retrieves the number of cards remaining in the deck
        @return: int, length of self.deck_stored
        """
        return len(self.deck_stored)

    def get_value_of_cards_remaining(self):
        """
        Retrieves the total value of all cards remaining in the deck
        @return: int, total value of all cards
        """
        return sum([rank_value[card.rank] for card in self.deck_stored])

    def get_cards_drawn(self):
        """
        Retrieves the drawn cards
        @return: list, list of drawn cards
        """
        return [card for card in self.deck_drawn]

    def draw(self):
        """
        Draws the topmost card from the deck
        Prints its suit and rank
        @return: None
        """
        # The topmost card is the last one in the stored cards
        card = self.deck_stored.pop()
        self.deck_drawn.append(card)
        return card

    def peek(self):
        """
        Lets to peek at the next three cards that will be drawn from the deck
        @return: list, list of next three cards
        """
        return [card for card in self.deck_stored[:-4:-1]]


random.seed(42)
# Creates an instance of the card deck
deck = CardDeck()
# Prints the amount of cards available
print('Number of cards in the deck:', deck.get_number_of_cards_remaining())
# Check if the bookkeeping of the drawn cards is done properly
print('Combined value of the cards', deck.get_value_of_cards_remaining())
# Draws three cards and prints them
deck.shuffle()
for i in range(3):
    card = deck.draw()
    print(card)
# Check if we're missing any cards
print('Number of cards in the deck after three were drawn:', deck.get_number_of_cards_remaining())
print('Combined value of remaining cards', deck.get_value_of_cards_remaining())

# Peeks at the next three cards
next_3_cards = deck.peek()
print(10 * '#' + ' These cards are the next to be drawn: ' + 10 * '#')
for card in next_3_cards:
    print(card)
# Checks if that's true
print(10 * '#' + ' These cards were drawn ' + 10 * '#')
# Draws next three cards and prints them
for i in range(3):
    card = deck.draw()
    print(card)
print('Number of cards in the deck after six were drawn:', deck.get_number_of_cards_remaining())
# Checks the drawn cards
drawncards = deck.get_cards_drawn()
for card in drawncards:
    print(card)
# Check if the bookkeeping of the drawn cards is done properly
print('Combined value of remaining cards', deck.get_value_of_cards_remaining())
