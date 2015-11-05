Deck of cards will be implemented with Python3

Because the spec is asking for a generic framework for a deck of
cards, I will assume that the Card class should be a superclass, as to
allow those who implement the Card to decide the actual content and
behaviors of the Cards themselves via inheritance. The Deck class, however,
is far more specific as it requires specific functions that require certain
behaviors. This allows us to implement a generic Deck of Cards as
decks of cards, no matter what the game, they are just stacks of cards;
essentially a Deck of Cards will just be an array/list of cards
with some additional functionality.

All ambiguity is handled by making the framework general enough to take in
different types of cards, whether it's a standard deck of cards or a deck of
cards from a game like uno.

One could write testing code for the final implemented deck of cards by first
creating the specific card type and eventually calling the deck's methods
on that specific deck. For the standard 52 card deck, one can shuffle the cards
and make sure that the order of the unshuffled deck is not the same as the
order of the shuffled deck. We can also test shuffle's functionality by removing
a card from the deck and shuffling and comparing the size of the shuffled deck to
the size of an unshuffled deck.

In order to test the getNextCard() function, on can simply call getNextCard() on
the deck and iterate through the deck to see if that card still exists, and also
if that card is in the not_in_deck hand. We can run this 52 times and on the
53rd time, the assertion error should be raised and caught, testing what should
happen when the deck is empty.