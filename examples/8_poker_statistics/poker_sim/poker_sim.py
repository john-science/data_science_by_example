
import itertools
from random import shuffle

"""
Hand                 Score
high card             0604030201 -  1312111008
pair                 10000000000 - 11312111000
two pair             20000000000 - 21312110000
three of a kind      30000000000 - 31300000000
staight              40000000000 - 41300000000
flush                50000000000 - 51312111008
full house           60000000000 - 61312000000
four of a kind       70000000000 - 71300000000
straight flush       80000000000 - 81300000000
royal flush          81300000000

Notes:
High card matters, but suit doesn't.
You split the pot, if you have the exact same hand in different suits.
Ace can be low or high, for straights... but you can't wrap around.
If both players have 3-of-a-kind, the value of the 3, not the two, breaks the tie.
There are extra rules of you're playing Hold 'em, and there are cards on the table.

Tie Breakers:
http://www.pokerhands.com/poker_hand_tie_rules.html
"""

# CONSTANTS
VALUES = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
          "Jack", "Queen", "King", "Ace"]
NUM_VALUES = 13
SUITS = ["Hearts", "Diamonds", "Spades", "Clubs"]
NUM_SUITS = 4
DECK_SIZE = NUM_VALUES * NUM_SUITS
PERMS_7CARD = list(itertools.combinations(range(7), 5))


def main():
    play_5card_stud()


def play_5card_stud():
    ''' simulate a game of 5-card stud, with 4 players,
        going through the deck once.
    '''
    deck = Deck()
    for game in xrange(2):
        print('\n============GAME===============\n')
        hands = []
        scores = []
        for player in xrange(4):
            start = (game * 5 * 4) + (player * 5)
            hand = Hand(deck.cards[start: start + 5])
            hands.append(hand)
            scores.append(hand.score)

        max_score = max(scores)
        is_draw = scores.count(max_score) > 1
        win_val = "WON  " if not is_draw else "DRAW "
        for player in xrange(4):
            if scores[player] == max_score:
                print(win_val + str(scores[player]).rjust(11) + " " + str(hands[player]))
            else:
                print("LOST " + str(scores[player]).rjust(11) + " " + str(hands[player]))


def scoring_unit_test():
    ''' A by-eye spot check that the scoring system works.
    '''
    print('\nA test of each basic case:')
    test_hands = [('bubkis', [(1, 0), (2, 1), (4, 2), (5, 3), (6, 0)]),
                  ('pair', [(1, 0), (7, 2), (5, 2), (6, 3), (7, 0)]),
                  ('two pair', [(6, 0), (4, 2), (5, 2), (6, 3), (4, 0)]),
                  ('3-of-a-kind', [(3, 0), (4, 2), (7, 2), (7, 3), (7, 0)]),
                  ('straight', [(3, 0), (4, 2), (5, 2), (6, 3), (7, 0)]),
                  ('flush', [(1, 0), (4, 0), (5, 0), (11, 0), (7, 0)]),
                  ('full house', [(3, 0), (3, 2), (6, 2), (6, 3), (6, 0)]),
                  ('4-of-a-kind', [(3, 0), (3, 1), (3, 3), (3, 2), (9, 0)]),
                  ('royal flush', [(9, 2), (10, 2), (11, 2), (12, 2), (13, 2)])]
    for desc,test in test_hands:
        hand = Hand(test)
        print('\n' + desc)
        print(hand)
        print(hand.score)
    print('')

    print('\nA random deck of 5-card stud:\n')
    deck = Deck()
    for i in xrange(5, 46, 5):
        hand = Hand(deck.cards[i : i + 5])
        print(hand)
        print(hand.score)
        print('')


def card_to_string(card):
    ''' a card is a tuple: (int value, int suit) '''
    return VALUES[card[0]] + '-' + SUITS[card[1]]


class Hand(object):

    def __init__(self, cards):
        self.cards = cards
        self.size = len(cards)
        self.score = self.get_score()

    @staticmethod
    def high_card(cards):
        ''' get the value, but not the suit of the high card in this hand '''
        return max(cards)[0]

    def get_score(self):
        ''' get the 5-card draw poker score,
            trying all permutations '''
        if self.size == 5:
            return Hand._5card_score(self.cards)
        elif self.size == 7:
            score = 0
            for ind in PERMS_7CARD:
                new_hand = []
                for i in ind:
                    new_hand.append(self.cards[i])
                new_score = Hand._5card_score(new_hand)
                if new_score > score:
                    score = new_score
            return score
        else:
            raise ValueError('Currently only hands of 5 and 7 cards are supported.')

    @staticmethod
    def _5card_score(cards):
        ''' get the 5-card draw poker score
            assuming only one deck is present
        '''
        high_card = Hand.high_card(cards)
        score = 0

        # check for pair(s), and 3/4-of-a-kind
        has_one_pair = False
        has_two_pair = False
        has_3ofakind = False
        has_4ofakind = False
        has_full_house = False
        high_set = -999

        values = {}
        for v,s in cards:
            if v not in values:
                values[v] = 0
            values[v] += 1
        num_unique = len(values)

        if num_unique < 5:
            if num_unique == 4:
                # one pair
                has_one_pair = True
                for v,cnt in values.iteritems():
                    if cnt > 1:
                        high_set = v
                        break
            elif num_unique == 3:
                # 2 pair, or 3-of-a-kind
                for v,cnt in values.iteritems():
                    if cnt == 3:
                        high_set = v
                        has_3ofakind = True
                        break
                    elif cnt == 2:
                        has_two_pair = True
                        if v > high_set:
                            high_set = v
            else:
                # 4-of-a-kind or full house
                for v,cnt in values.iteritems():
                    if cnt == 4:
                        high_set = v
                        has_4ofakind = True
                        break
                    elif cnt == 3:
                        high_set = v
                        has_full_house = True
                        break

            # return early, if you can
            if has_one_pair:
                vals = sorted(values.keys(), reverse=True)
                vals.remove(high_set)
                vals[0] *= 1e6
                vals[1] *= 1e4
                vals[2] *= 1e2
                score = int(1e10 + (high_set * 1e8) + sum(vals))
                return score
            elif has_two_pair:
                low_set = high_set
                spare = 0
                for v,cnt in values.iteritems():
                    if cnt == 2:
                        if v < low_set:
                            low_set = v
                    elif cnt == 1:
                        spare = v
                score = int(2e10 + (high_set * 1e8) + (low_set * 1e6) + (spare * 1e4))
                return score
            elif has_3ofakind:
                score = int(3e10 + (high_set * 1e8))
                return score
            elif has_full_house:
                score = int(6e10 + (high_set * 1e8))
                return score
            elif has_4ofakind:
                score = int(7e10 + (high_set * 1e8))
                return score

        # check for straight
        has_straight = False
        if len(values) == 5:
            vals = sorted(values.keys())
            if vals[0] + 4 == vals[-1]:
                has_straight = True
            elif vals[0] + 3 == vals[-2] and vals[-1] == 13:
                # ace-low straight
                high_card = vals[-2]
                has_straight = True

        # check for flush
        has_flush = False
        suits = set([c[1] for c in cards])
        if len(suits) == 1:
            has_flush = True

        # build final score for less likely hands
        if has_flush and has_straight:
            score = int((800 + high_card) * 1e8)
        elif has_straight:
            score = int((400 + high_card) * 1e8)
        elif has_flush:
            vals = sorted(values.keys(), reverse=True)
            vals[0] *= 1e8
            vals[1] *= 1e6
            vals[2] *= 1e4
            vals[3] *= 1e2
            score = int(5e10 + sum(vals))
        else:
            # high card
            vals = sorted(values.keys(), reverse=True)
            vals[0] *= 1e8
            vals[1] *= 1e6
            vals[2] *= 1e4
            vals[3] *= 1e2
            vals[4] *= 1e2
            score = int(sum(vals))

        return score

    def __str__(self):
        return ' '.join(card_to_string(card) for card in sorted(self.cards))


class Deck(object):

    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.num_cards = self.num_decks * DECK_SIZE
        self.cards = [((i % NUM_VALUES) + 1, (i // NUM_SUITS) % NUM_SUITS) for i in range(self.num_cards)]
        shuffle(self.cards)


if __name__ == '__main__':
    main()
