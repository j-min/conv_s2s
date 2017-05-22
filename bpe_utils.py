import re
import collections
from pprint import pprint


def get_stats(vocab):
    """
    word frequencies => bigram frequencies
    
    Arg:
        Dict
            Keys: word
            values: frequencies
    
    Return:
        collections.defaultdict
            keys: bigram
            values: frequencies
    """
    pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[(symbols[i], symbols[i+1])] += freq
    return pairs

def merge_vocab(pair, v_in):
    """
    Apply single step of BPE to vocabulary
    """
    v_out = {}
    bigram = re.escape(' '.join(pair)) # esacpe non-ascii characters
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
        w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]
    return v_out

