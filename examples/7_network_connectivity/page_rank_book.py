
from glob import glob

NAMES_FILE = 'game_of_thrones_pseudonymns.txt'
BOOK_FILES = glob('data/book_1/txt/chapter*.txt')
DISTANCE = 15


def main():
    pr = PageRankBooks(NAMES_FILE, BOOK_FILES, DISTANCE)


class PageRankBooks(object):

    def __init__(self, names_file, book_files, max_distance):
        self.names_file = names_file
        self.book_files = book_files
        self.max_distance = max_distance
        self.charachters = []
        self.pseudonymns = {}
        self._read_names()
        self.connections = {}
        self._init_connections()

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

    def find_all_connections(self, file_paths):
        ''' Just a helper method to find all the connections between characters
            in a book. Even if that book is broken into parts.
        '''
        self.charachters = []
        self.pseudonymns = {}
        for file_path in file_paths:
                self._find_connections(file_path)

    def _find_connections(self, file_path):
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
                if word in self.characters:
                    self.connections.[name][word] += 1

    def page_rank(self):
        ''' TODO '''
        pass


if __name__ == '__main__':
    main()
