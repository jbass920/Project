import random


class Card:
    """Represents a standard playing card"""

    def __init__(self, suit: str, rank: str) -> None:
        """Creates a new instance of a Card"""
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        """Returns a string representation of the Card"""
        return f"{self.rank} of {self.suit}"


class Deck:
    """Represents a deck of standard playing cards"""

    def __init__(self) -> None:
        """Creates a new instance of a Deck"""
        self.cards = []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for rank in range(2, 11):
                self.cards.append(Card(suit, str(rank)))
            for rank in ["Jack", "Queen", "King", "Ace"]:
                self.cards.append(Card(suit, rank))

    def shuffle(self) -> None:
        """Shuffles the deck of cards"""
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        """Removes and returns a card from the deck"""
        return self.cards.pop()


class Hand:
    """Represents a hand of cards"""

    def __init__(self) -> None:
        """Creates a new instance of a Hand"""
        self.cards = []
        self.total = 0
        self.aces = 0

    def add_card(self, card: Card) -> None:
        """Adds a card to the hand"""
        self.cards.append(card)
        if card.rank == "Ace":
            self.aces += 1
        self.total += self.card_value(card)

    def card_value(self, card: Card) -> int:
        """Returns the value of a card"""
        if card.rank in ["Jack", "Queen", "King"]:
            return 10
        elif card.rank == "Ace":
            return 11
        else:
            return int(card.rank)

    def adjust_for_ace(self) -> None:
        """Adjusts the value of a hand if it contains an ace"""
        while self.total > 21 and self.aces:
            self.total -= 10
            self.aces -= 1


class Player:
    """Represents a player"""

    def __init__(self) -> None:
        """Creates a new instance of a Player"""
        self.hand = Hand()

    def hit(self, deck: Deck) -> None:
        """Adds a card to the player's hand"""
        self.hand.add_card(deck.deal_card())
        self.hand.adjust_for_ace()

    def show_hand(self) -> None:
        """Prints the player's hand to the console"""
        for card in self.hand.cards:
            print(card)

    def get_hand_total(self) -> int:
        """Returns the total value of the player's hand"""
        return self.hand.total


class Dealer:
    """Represents the dealer"""

    def __init__(self) -> None:
        """Creates a new instance of a Dealer"""
        self.hand = Hand()

    def hit(self, deck: Deck) -> None:
        """Adds a card to the dealer's hand"""
        self.hand.add_card(deck.deal_card())
        self.hand.adjust_for_ace()

    def show_hand(self) -> None:
        """Prints the dealer's hand to the console"""
        print("Dealer's Hand:")
        print("HIDDEN CARD")
        for card in self.hand.cards[1:]:
            print(card)

# Define a function to get the total value of a hand
def get_hand_total(hand):
    total = 0
    aces = 0
    for card in hand:
        if card in ["J", "Q", "K"]:
            total += 10
        elif card == "A":
            aces += 1
            total += 11
        else:
            total += int(card)
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

# Define a function to play a round of blackjack
def play_blackjack():
    # Set up the deck of cards
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * 4
    random.shuffle(deck)
    
    # Deal the initial cards
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Let the player take their turn
    while True:
        print("Your hand:", player_hand)
        print("Dealer's hand:", [dealer_hand[0], "*"])
        if get_hand_total(player_hand) > 21:
            print("Bust! You lose.")
            return
        elif get_hand_total(player_hand) == 21:
            print("Blackjack! You win!")
            return
        else:
            action = input("Do you want to hit or stand? ")
            if action == "hit":
                player_hand.append(deck.pop())
            elif action == "stand":
                break

    # Let the dealer take their turn
    while get_hand_total(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    # Determine the winner
    print("Your hand:", player_hand)
    print("Dealer's hand:", dealer_hand)
    player_total = get_hand_total(player_hand)
    dealer_total = get_hand_total(dealer_hand)
    if dealer_total > 21:
        print("Dealer busts! You win!")
    elif dealer_total == 21:
        print("Dealer has blackjack! You lose.")
    elif dealer_total < player_total:
        print("You win!")
    elif dealer_total > player_total:
        print("You lose.")
    else:
        print("It's a tie!")

# Play the game
while True:
    play_blackjack()
    again = input("Do you want to play again? ")
    if again.lower() != "yes":
        break

