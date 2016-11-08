
#include <iostream>
#include <random>
#include "random_seed.h"
#include "nouns.h"

using namespace std;


/**
 * Hand                 Score
 * high card            0-12
 * pair                 1000-1012
 * two pair             2000-2012  # TODO: Not just high card
 * three of a kind      3000-3012
 * staight              4003-4012
 * flush                5004-5012
 * full house           6000-6012  # TODO: Not accounting for tie breakers
 * four of a kind       7000-7012
 * straight flush       8003-8012
 * royal flush          8012
 *
 * Notes:
 * High card matters, but suit doesn't.
 * You split the pot, if you have the exact same hand in different suits.
 * Ace can be low or high, for straights... but you can't wrap around.
 * If both players have 3-of-a-kind, the value of the 3, not the two, breaks the tie.
 * There are extra rules of you're playing Hold 'em, and there are cards on the table.
 */
int score_5card_draw(Hand hand) {
    // find high card
    int high_card(hand[4].get_value());

    // set minimum score
    int score(high_card);

    // check for pair(s), and 3/4-of-a-kind
    bool has_one_pair(false);
    bool has_two_pair(false);
    bool has_3ofakind(false);
    bool has_4ofakind(false);
    int high_pair(-999);

    int val(-999);
    int count(0);
    for (int i=0; i < 6; ++i) {
        if (i < 5 || hand[i].get_value() == val) {
            count += 1;
        } else {
            if (count < 2) {
                if (i < 5) {
                    val = hand[i].get_value();
                }
            } else if (count == 2) {
                if (!has_one_pair) {
                    has_one_pair = true;            // TODO: Complete failure for one pair!
                    high_pair = val;
                } else {
                    has_one_pair = false;
                    has_two_pair = true;
                    if (val > high_pair) {
                        high_pair = val;
                    }
                }
            } else if (count == 3) {
                has_3ofakind = true;
                high_card = val;
            } else if (count == 4) {
                has_4ofakind = true;
                high_card = val;
            }
            count = 1;
        }
    }

    // save the compute time: if any of these are true, there are no straights or flushes
    if (has_one_pair || has_two_pair || has_3ofakind || has_4ofakind) {
        if (has_one_pair && has_3ofakind) {
            // check for full house
            score = 6000 + high_card;
        } else if (has_one_pair) {
            score = 1000 + high_pair;
        } else if (has_two_pair) {
            score = 2000 + high_pair;
        } else if (has_3ofakind) {
            score = 3000 + high_card;
        } else if (has_4ofakind) {
            score = 7000 + high_card;
        }

        return score;
    }

    // check for straight
    bool is_straight(false);
    val = hand[0].get_value();
    if (hand[1].get_value() == val + 1 && hand[2].get_value() == val + 2 && hand[3].get_value() == val + 3) {
        if (hand[4].get_value() == val + 4) {
            // typical straight
            is_straight = true;
        } else if (val == 2 && hand[4].get_value() == 12) {
            // the Ace-low straight
            is_straight = true;
        }
    }

    // check for flush
    bool is_flush(true);
    int suit(hand[0].get_suit());
    for (int j=1; j < 5; ++j) {
        if (hand[j].get_suit() != suit) {
            is_flush = false;
            break;
        }
    }

    if (is_flush) {
        if (is_straight) {
            // straight flush
            score = 8000 + high_card;
        } else {
            // normal straight
            score = 5000 + high_card;
        }
    }

    return score;
}


int main() {
    srand(time(0));

    // poker defs
    int num_decks(1);
    int cards_per_hands(5);
    int num_hands(1);

    // create a single deck of cards
    Deck deck = Deck(1);

    // make a hand out of the first five cards in the deck
    for (int i=0; i < 25; i += 5) {
        Hand hand = Hand(&deck[i], 5);
        cout << hand[0] << "   " << hand[1] << "   " << hand[2] << "   " << hand[3] << "   " << hand[4] << endl;
        cout << score_5card_draw(hand) << endl << endl;
    }
}
