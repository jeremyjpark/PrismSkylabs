Deck of cards will be implemented with Python3

Because the spec is asking for a generic framework for a deck of 
cards, I will assume that the Card class should be a superclass, as to 
allow those who implement the Card to decide the actual content and 
behaviors of the Cards themselves via inheritance. The Deck class, however, 
is far more specific as it requires specific functions that require certain 
behaviors. This allows us to implement a generic Deck of Cards as 
decks of cards, no matter what the game, are just stacks of cards; 
essentially a Deck of Cards will just be an array/list of cards 
with some additional functionality.