
#include <algorithm>
#include <iostream>
#include <random>
#include "random_seed.h"
#include "nouns.h"

using namespace std;


// TODO: Build a Hands of cards (just an array of Cards)
// TODO: Determine the score/rank of a hand
/**
 * Hands:
 * high card
 * pair
 * two pair
 * three of a kind
 * staight
 * flush
 * full house
 * four of a kind
 * straight flush
 * royal flush
 *
 * Notes:
 * High card matters, but suit doesn't.
 * You split the pot, if you have the exact same hand in different suits.
 * Ace can be low or high, for straights... but you can't wrap around.
 * If both players have 3-of-a-kind, the value of the 3, not the two, breaks the tie.
 * There are extra rules of you're playing Hold 'em, and there are cards on the table.
 */


int main() {
    srand(time(0));

    // poker defs
    int num_decks(1);
    int cards_per_hands(5);
    int num_hands(1);

    // create a single deck of cards
    Deck deck = Deck(1);
    cout << deck[0] << "   " << deck[1] << "   " << deck[2] << endl;

    // make a hand out of the first five cards in the deck
    Hand hand = Hand(&deck[0], 5);
    cout << hand[0] << "   " << hand[1] << "   " << hand[2] << "   " << hand[3] << "   " << hand[4] << "   " << hand[5] << "   " << hand[6] << endl;
    sort(&hand[0], &hand[0] + 5);
    cout << hand[0] << "   " << hand[1] << "   " << hand[2] << "   " << hand[3] << "   " << hand[4] << "   " << hand[5] << "   " << hand[6] << endl;
}
