import sys
import heapq

def file_character_frequencies(file_name):
 
    file = open(file_name, 'r')
    freq = dict()
     
    while 1:
         
        # read by character
        char = file.read(1)
        if freq.get(char) == None:
            freq[char] = 1
        else:
            freq[char] += 1
        if not char:
            break
     
    file.close()

    return freq


class PriorityTuple(tuple):
    """A specialization of tuple that compares only its first item when sorting.
    Create one using double parens e.g. PriorityTuple((x, (y, z))) """
    def __lt__(self, other):
        return self[0] < other[0]

    def __le__(self, other):
        return self[0] <= other[0]

    def __gt__(self, other):
        return self[0] > other[0]

    def __ge__(self, other):
        return self[0] >= other[0]

    def __eq__(self, other):
        return self[0] == other[0]

    def __ne__(self, other):
        x = self.__eq__(other)
        return not x

class Node:
    def __init__(self, prob, symbol, left=None, right=None):

        self.prob = prob

        self.symbol = symbol

        self.left = left

        self.right = right

        self.code = ''

def huffman_codes_from_frequencies(frequencies):
    
    symbols = frequencies.keys()
    probabilities = frequencies.values()

    nodes = []

    for symbol in symbols:
        nodes.append(Node(frequencies.get(symbol), symbol))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.prob)

        right = nodes[0]
        left = nodes[1]

        left.code = 0
        right.code = 1

        newNode = Node(left.prob+right.prob, left.symbol+right.symbol, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffman_encoding = caluclate_codes(nodes[0])
    return huffman_encoding


codes = dict()

def caluclate_codes(node, val=''):
    newVal = val + str(node.code)

    if(node.left):
        caluclate_codes(node.left, newVal)
    if(node.right):
        caluclate_codes(node.right, newVal)

    if(not node.left and not node.right):
        codes[node.symbol] = newVal

    return codes

def huffman_letter_codes_from_file_contents(file_name):
    """WE WILL GRADE BASED ON THIS FUNCTION."""

    freqs = file_character_frequencies(file_name)
    return huffman_codes_from_frequencies(freqs)


def encode_file_using_codes(file_name, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name) as f:
        contents = f.read()
    file_name_encoded = file_name + "_encoded"
    with open(file_name_encoded, 'w') as fout:
        for c in contents:
            fout.write(letter_codes[c])
    print("Wrote encoded text to {}".format(file_name_encoded))


def decode_file_using_codes(file_name_encoded, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name_encoded) as f:
        contents = f.read()
    file_name_encoded_decoded = file_name_encoded + "_decoded"
    codes_to_letters = {v: k for k, v in letter_codes.items()}
    with open(file_name_encoded_decoded, 'w') as fout:
        num_decoded_chars = 0
        partial_code = ""
        while num_decoded_chars < len(contents):
            partial_code += contents[num_decoded_chars]
            num_decoded_chars += 1
            letter = codes_to_letters.get(partial_code)
            if letter:
                fout.write(letter)
                partial_code = ""
    print("Wrote decoded text to {}".format(file_name_encoded_decoded))


def main():
    """Provided to help you play with your code."""
 
    codes = huffman_letter_codes_from_file_contents(sys.argv[1])
    print(codes)


if __name__ == '__main__':
    """We are NOT grading you based on main, this is for you to play with."""
    main()
