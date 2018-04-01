#######################
# Tree Implementation #
#######################

class Tree:
    def __init__(self, tag, branches):
        assert len(branches) >= 1
        for b in branches:
            assert isinstance(b, (Tree, Leaf))
        self.tag = tag
        self.branches = branches
        
class Leaf:
    def __init__(self, tag, word):
        self.tag = tag
        self.word = word

######################
# Printing Mechanism #
######################
Leaf.__str__ = lambda leaf: '({tag} {word})'.format(**leaf.__dict__)

def print_tree(t, indent=0, end='\n'):
    """Print Tree or Leaf t with indentation"""
    if isinstance(t, Leaf):
        print(t, end='')
    else:
        s = '(' + t.tag + ' '
        indent += len(s)
        print(s, end='')
        print_tree(t.branches[0], indent, '')
        for b in t.branches[1:]:
            print('\n' + ' '*indent, end='')
            print_tree(b, indent, '')
        print(')', end=end)
        
        
###########
# GRAMMAR #
###########
lexicon = {
        Leaf('N', 'cows'),
        Leaf('V', 'intimidate'),
        Leaf('J', 'Yankee'),
        Leaf('R', 'that')
        }
        
grammar = {
        'S': [['NP', 'VP']],
        'NP': [['N'], ['J', 'N'], ['NP', 'RP']],
        'VP': [['V', 'NP']],
        'RP': [['R', 'NP', 'V']],
        }

##########
# Parser #
##########
def parse(line):
    words = line.split()
        
    def expand(start, end, tag):
        """Yield all trees rooted by tag"""
        if end-start == 1:
            word = words[start]
            for leaf in lexicon:
                if leaf.tag == tag and leaf.word == word:
                    yield leaf
        if tag in grammar:
            for tags in grammar[tag]:
                for branches in expand_all(start, end, tags):
                    yield Tree(tag, branches)
                    
    def expand_all(start, end, tags):
        """Yield sequences of branches for a sequence of tags"""
        if len(tags) == 1:
            for branch in expand(start, end, tags[0]):
                yield [branch]
        else:
            first, rest = tags[0], tags[1:]
            for middle in range(start+1, end+1-len(rest)):                
                for first_branch in expand(start, middle, first):
                    for rest_branches in expand_all(middle, end, rest):
                        yield [first_branch] + rest_branches
                                
    for tree in expand(0, len(words), 'S'):
        print_tree(tree)
