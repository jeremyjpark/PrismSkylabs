import random

# This is a general Deck of cards that has some number of Card Objects.
class Deck(Object):

  # Constructor, which takes in a list of cards in the Deck.
  def __init__(self, cards):
    self.size = len(cards) # not used, but might be helpful
    self.deck = cards
    self.not_in_deck = []

  # Shuffle() that shuffles this deck randomly. When called, all cards are put
  # back in the Deck.
  def shuffle():
    self.deck += self.not_in_deck
    self.not_in_deck = []
    random.shuffle(self.deck)

  # GetNextCard() that returns the next card from the deck. If the deck is
  # empty (there are no cards left in the deck), an error will signal that
  # There are no cards left in the Deck.
  def getNextCard():
    try:
      assert(self.deck == 0) # Check that the deck isn't empty
      card = self.deck.pop()
      self.not_in_deck.push(card)
      return card
    except:
      print("No cards left in Deck")