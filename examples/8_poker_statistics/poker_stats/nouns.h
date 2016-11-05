
#ifndef _NOUNS
#define _NOUNS

#include <iostream>

// constants
static const char *Suits[] = {"Hearts", "Diamonds", "Spades", "Clubs"};
static const int num_suits(4);
static const char *Values[] = {"2", "3", "4", "5", "6", "7", "8", "9", "10",
                               "Jack", "Queen", "King", "Ace"};
static const int num_values(13);
static const int cards_per_deck(num_suits * num_values);


class Card {
public:
    Card();
    Card(const int v, const int s);
    int get_value();
    int set_value(const int v);
    int get_suit();
    int set_suit(const int s);
    friend std::ostream& operator<<(std::ostream &os, const Card& card);
private:
    int value;
    int suit;
};


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


#endif
