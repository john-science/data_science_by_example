
#include <algorithm>
#include <iostream>
#include <random>
#include <stdexcept>

using namespace std;

// forward declarations
bool in_array(const int arr[], const int value);
int* floyds_algorithm(const int n, const int m);
int randint(const int max_int);
int randint(const int min_int, const int max_int);
void print_int_array(const int arr[], const int length);

// constants
static const char *Suits[] = {"Hearts", "Diamonds", "Spades", "Clubs"};
static const int num_suits(4);
static const char *Values[] = {"2", "3", "4", "5", "6", "7", "8", "9", "10",
                               "Jack", "Queen", "King", "Ace"};
static const int num_values(13);
static const int cards_per_deck(num_suits * num_values);

// TODO: Build a Hands of cards (just an array of Cards)
// TODO: Determine the value of a hand
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

class Card {
public:
    Card();
    Card(const int v, const int s);
    int get_value() {return value;};
    int set_value(const int v) {if (v < 0 || v >= num_values) {throw out_of_range("blah");} else {value = v;}};
    int get_suit() {return suit;};
    int set_suit(const int s) {if (s < 0 || s >= num_suits) {throw out_of_range("blah");} else {suit = s;}};
    friend ostream& operator<<(ostream &os, const Card& card);
private:
    int value;
    int suit;
};

ostream& operator<< (ostream &os, const Card &card) {
    os << Values[card.value] << "-" << Suits[card.suit];
    return os;
}


Card::Card() {
    set_value(randint(num_values));
    set_suit(randint(num_suits));
}


Card::Card(const int v, const int s) {
    set_value(v);
    set_suit(s);
}


class Deck {
public:
    Deck();
    Deck(const int n);
    void shuffle();
    Card& operator[] (const int index);
    const Card& operator[] (const int index) const;
private:
    int num_cards;
    Card *cards;
};


Card& Deck::operator[] (const int index)
{
    return cards[index];
}


const Card& Deck::operator[] (const int index) const
{
    return cards[index];
}


Deck::Deck() {
    Deck(1);
}


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

/**
 * Print an arry of integers, nicely to the screen.
 */
void print_int_array(const int arr[], const int length) {
    for (int i = 0; i < length; ++i) {
        cout << arr[i] << ' ';
    }
}


/**
 * Test if value is in array of integers.
 */
template<typename T> bool in_array(const T arr[], const size_t len, const T value) {
    for (size_t i=0; i < len; ++i) {
        if (arr[i] == value) {
            return true;
        }
    }

    return false;
}


/**
 * Floyd's Algorithm
 * Randomly select M distinct value from [0 to N).
 */
int* floyds_algorithm(const int n, const int m) {
    int* result = new int[m];
    int i(0);
    int t(0);

    for (int j = n - m; j < n + 1; ++j) {
        t = randint(1, j + 1);

        if (in_array(result, m, t)) {
            result[i] = j;
        } else {
            result[i] = t;
        }

        i += 1;
    }

    return result;
}


/**
 *    Randomly select an integer below a max value.
 */
int randint(const int max_int) {
    float r = static_cast <float> (rand()) / static_cast <float> (RAND_MAX);
    return (int)(r * max_int);
}


/**
 *    Randomly select an integer in a range.
 */
int randint(const int min_int, const int max_int) {
    float r = static_cast <float> (rand()) / static_cast <float> (RAND_MAX);
    return (int)((r * (max_int - min_int)) + min_int);
}


/**
 *    Randomly select an element from an integer array.
 */
template<typename T> T choice(const T arr[], const int length) {
    float r = static_cast <float> (rand()) / static_cast <float> (RAND_MAX);
    return arr[(int)(length * r)];
}


int main() {
    srand(time(0));

    // poker defs
    int num_decks(1);
    int cards_per_hands(5);
    int num_hands(1);

    // draw!
    int* hand = floyds_algorithm(cards_per_deck * num_decks, cards_per_hands * num_hands);

    // print hand
    cout << endl;
    print_int_array(hand, cards_per_hands * num_hands);
    cout << endl << endl;

    // create a single deck of cards
    Deck deck = Deck(1);
    cout << deck[0] << "   " << deck[1] << "   " << deck[2] << endl;
}
