
#include <algorithm>
#include <iostream>
#include <stdexcept>
#include "random_seed.h"
#include "nouns.h"

using namespace std;


/**
 *  Generate a totally random Card.
 *  (This is called when initializing an array of Cards.)
 */
Card::Card() {
    set_value(randint(num_values));
    set_suit(randint(num_suits));
}


/**
 *  Define a specific Card.
 */
Card::Card(const int v, const int s) {
    set_value(v);
    set_suit(s);
}


/**
 * Overriding cout operator to print a Card
 */
ostream& operator<< (ostream &os, const Card &card) {
    os << Values[card.value] << "-" << Suits[card.suit];
    return os;
}

/**
 * Getter for face-value or number of a Card.
 */
int Card::get_value() {
    return value;
}


/**
 * Set the face-value or number of a Card.
 */
int Card::set_value(const int v) {
    if (v < 0 || v >= num_values) {
        throw out_of_range("blah");
    } else {
        value = v;
    }
}


/**
 *  Get the suit of the Card.
 */
int Card::get_suit() {
    return suit;
};


/**
 *  Set the suit of the Card.
 */
int Card::set_suit(const int s) {
    if (s < 0 || s >= num_suits) {
        throw out_of_range("blah");
    } else {
        suit = s;
    }
}


/**
 *  Get a specific card using the index operator.
 */
Card& Deck::operator[] (const int index)
{
    return cards[index];
}


/**
 *  constant versino of the index operator
 */
const Card& Deck::operator[] (const int index) const
{
    return cards[index];
}


/**
 *  Default constructor.
 */
Deck::Deck() {
    Deck(1);
}


/**
 *  The usual constructor: casinos frequently use more
 *  one deck of cards at a time.
 */
Deck::Deck(const int num_decks) {
    num_cards = num_decks * cards_per_deck;
    cards = new Card[num_cards];

    // fill (possibly multiple) deck with cards
    int i(0);
    for (int d=0; d < num_decks; ++d) {
        for (int s=0; s < num_suits; ++s) {
            for (int v=0; v < num_values; ++v) {
                cards[i] = Card(v, s);
                ++i;
            }
        }
    }

    // shuffle the deck
    random_shuffle(&cards[0], &cards[num_cards]);
}
