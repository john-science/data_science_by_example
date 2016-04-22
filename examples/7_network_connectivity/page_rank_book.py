
from glob import glob

NAMES_FILE = 'game_of_thrones_pseudonymns.txt'
BOOK_FILES = glob('data/book_1/txt/chapter*.txt')
DISTANCE = 15


def main():
    pr = PageRankBooks(NAMES_FILE, BOOK_FILES, DISTANCE)
    pr.find_connections()


class PageRankBooks(object):

    def __init__(self, names_file, book_files, max_distance):
        self.names_file = names_file
        self.book_files = book_files
        self.max_distance = max_distance
        self.characters = []
        self.pseudonymns = {}
        self._read_names()
        self.connections = {}
        self._init_connections()
        self.ranks = {}

    def _init_connections(self):
        ''' Initialize the characters connections with the present list
            of character names.
        '''
        for name in self.characters:
            self.connections[name] = defaultdict(int)

    def _read_names(self):
        ''' Define all of the character names in the books beforehand.
            Create a list of character names, along with a dictionary of
            pseudonymns.

            Input File Format:
            daenerys:mother of dragons,dany
            davos
            drogo:sun and stars
        '''
        f = open(self.names_file, 'r')
        for line in f.readlines():
            ln = line.rstrip().split(':')
            name = ln[0]
            self.characters.append(name)
            if len(ln) > 1:
                self.pseudonymns[name] = ln[1:]
        f.close()

    def find_connections(self):
        ''' find all the connections between characters
            in a book. Even if that book is broken into parts.
        '''
        self.characters = []
        self.pseudonymns = {}
        for file_path in self.book_files:
                self._find_connections_1_file(file_path)

    def _find_connections_1_file(self, file_path):
        ''' Parse a single input file, creating the basic network connections
            between the characters of a book.
            In particular, create a mapping from each name to each other name it is
            connected to, along with a count of connections.

            NOTE: First all instances of pseudonymns in the book are replaced.
            NOTE: Connections are defined as names appearing X words apart in the book.
        '''
        # read file
        text = open(file_path).read()

        # replace pseudonymns with ID name
        for name in self.pseudonymns:
            for pseudo in self.pseudonymns[name]:
                text.replace(pseudo, name)

        # break text into list of words
        words = text.split()

        # remove all words with length=1 (not important)
        words = list(filter(lambda w: len(w) > 1, words))

        # hunt through document, looking for names
        max_index = len(words) - 1
        for i in range(max_index):
            if words[i] not in self.characters:
                continue
            character = words[i]
            # find all connected names
            for word in [words[i]: words[i + self.max_distance]]:
                if word in self.charactes and word != name:
                    self.connections.[name][word] += 1

    def page_rank(self):
        ''' This will be an undamped PageRank, because I see no obvious
            basis on which to calculate a damping factor.
        '''
        # initialize ranks
        for name in self.characters:
            self.ranks[name] = 0.0

        num_nodes = len(self.characters)

        # loop through all the connections to build the page ranks
        for char1 in self.connections:
            num_links = float(sum(self.connections[char1].values()))
            for char2 in self.connections[char1]:
                self.ranks[char2] += (self.connections[char1][char2] / num_links) / num_nodes


if __name__ == '__main__':
    main()


"""
Testing the NetworkX plotting library:

import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_edge('Arya', 'Jon', color='r', weight=6)
G.add_edge('Jon', 'Catelyn', color='b', weight=4)
G.add_edge('Catelyn', 'Tyrion', color='g', weight=1)

pos = nx.circular_layout(G)

edges = G.edges()
colors = [G[u][v]['color'] for u,v in edges]
weights = [G[u][v]['weight'] for u,v in edges]
node_sizes = [480, 400, 320, 480]

nx.draw(G, pos, edges=edges, edge_color=colors, width=weights, with_labels=True,
        node_size=node_sizes)
plt.savefig("networkx_testing.png")
"""
