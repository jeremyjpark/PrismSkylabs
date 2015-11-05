Deck of Cards
-------------
Create a framework that models a generic deck of cards, with the following
behaviors:
  * Should contain an operation named Shuffle() that shuffles this deck
    randomly.
  * Should contain an operation called GetNextCard() that returns the next
    card from the deck
  * GetNextCard() should signal an error when the entire deck has been dealt
    out
  * A call to Shuffle() should cause all cards to be put back in the deck

Using this framework, create a class to model a standard deck of 52 playing
cards that contain 4 suits of 13 cards each.

Include a README as part of your solution and explain:
  * your design decisions
  * how you resolved any ambiguity in the instructions
  * how you would determine that your framework is working correctly for the
    deck of playing cards

Additionally, if you’ve been asked to solve this assignment in a compiled
language, please include Makefile or something suitable that can be used
to compile your code, with instructions in the README.


The Vacationing Salesman
------------------------
The goal of this question is to write a script, which given
a vacation itinerary determines the real-world distance traveled over
the itinerary.

Points on the itinerary will be referenced in form "City, Country".
For example:
    "Paris, France"
    "New York City, USA"
    "Nuuk, Greenland"
are all possible points on the itinerary.

Basic Implementation:
  * a function that accepts an ordered list of strings,
    each string of the form above designating a "City, Country"
  * that function returns a list with the distance, in either km or miles,
    between each successive pair of cities. So, if the input list is
    like the example list of cites above, the output of the function
    could be: [3631.16, 1852.78], where output has been chosen to be
    in miles.
  * wrap the basic function in a script, so that it accepts cites
    via stdin, one city per line. Output is written to stdout.
    Interaction would go something like this:

    $ vacationing-salesman < cities.txt
    Success! Your vacation itinerary is:
        Paris, France -> New York City, USA: 3,631.16 miles
        New York City, USA -> Nuuk, Greenland: 1,852.78 miles
    Total distance covered in your trip: 5,483.94 miles

Bonus Points:
  * add an option to the script which controls output in miles or kilometers
  * add an option to your script for mode of travel. The default is
    'as a crow files' - that is, the straight-line distance between
    the given cities. Other options could be: 'car', 'transit', 'foot'
    or 'kayak'.  Some options may not be feasible between all pairs
    of cities - handle this as you like.
 * add an option to your script to optimize the itinerary to minimize
   total distance travelled. Interaction could go something like this:
   $ vacationing-salesman --optimize < cities.txt
   Success! An *optimized* version of your vacation itinerary is:
        New York City, USA -> Nuuk, Greenland: 1,852.78 miles
        Nuuk, Greenland -> Paris, France: 2,229.06 miles
    Total distance covered in your trip: 4,081.84 miles

Most important of all, please include a README in your submission that
details:
  * how to run your script or function
  * why you choose the langauge you did
  * what the primary design decisions were in implementing your solution
    and why you made the choices you did
  * if you ran out of time, what you were hoping to do next
