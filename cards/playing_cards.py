import card
import deck

# What is normally though of as a standard card in a deck
class PlayingCard(Card):
  suits = ['Heart', 'Diamond', 'Spade', 'Club']
  values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

  def __init__(self, suit, value):
    self.suit = suit
    self.value = value

  def suit():
    return self.suit

  def value():
    return self.value


playingcards = []
for suit in PlayingCard.suits:
  for value in PlayingCard.values:
    playing_cards = PlayingCard(suit, value)

new_deck = Deck(playing_cards)

