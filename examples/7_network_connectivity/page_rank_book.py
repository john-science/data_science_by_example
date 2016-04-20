
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
        self.ranks = {}
        self._init_ranks()

    def _init_ranks(self):
        ''' Initialize the ranks collection with the present list
            of character names.
        '''
        for name in self.characters:
            self.ranks[name] = defaultdict(int)

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

    def page_rank_one_file(self, file_path):
        ''' Parse a single input file, creating the basic network connections needed
            to page rank one book.
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
        max_index = len(words) - self.max_distance
        for i in range(max_index):
            if words[i] not in self.characters:
                continue
            character = words[i]
            for j in range(i, i + self.max_distance):
                if words[j] in self.characters:
                    self.ranks[name][words[j]] += 1


if __name__ == '__main__':
    main()
