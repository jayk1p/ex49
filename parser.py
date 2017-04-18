
class ParserError(Exception):
    pass


class Sentence(object):

    def __init__(self, subject, verb, obj):
        # remember we take ('noun','princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]


def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

    # list.pop REMOVES the item at the given position in the list,
    # and return it.

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)


def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")



def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")


## I am not sure why it is going to "else" than "elif", b/c
## I do have 'verb' == 'verb'

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    # print Sentence(subj, verb, obj)
    return Sentence(subj, verb, obj)

# The thing about this is that we have to have a list of two tuples or more
# or else this program is not going to work




def scan(stuff):

    word_list = []
    # stuff = raw_input('> ')
    # You don't need this for nosetests
    words = stuff.split()

    for i in words:
        if "north" == i:
            word_list.append(('direction', 'north'))

        if "south" == i:
            word_list.append(('direction', 'south'))

        if "east" == i:
            word_list.append(('direction', 'east'))


        if "go" == i:
            word_list.append(('verb', 'go'))

        if "kill" == i:
            word_list.append(('verb', 'kill'))

        if "eat" == i:
            word_list.append(('verb', 'eat'))


        if "the" == i:
            word_list.append(('stop', 'the'))

        if "in" == i:
            word_list.append(('stop', 'in'))

        if "of" == i:
            word_list.append(('stop', 'of'))


        if "bear" == i:
            word_list.append(('noun', 'bear'))

        if "princess" == i:
            word_list.append(('noun', 'princess'))


        if "1234" == i:
            word_list.append(('number', 1234))

        if "3" == i:
            word_list.append(('number', 3))

        if "91234" == i:
            word_list.append(('number', 91234))


        if "ASDFADFASDF" == i:
            word_list.append(('error', 'ASDFADFASDF'))

        if "IAS" == i:
            word_list.append(('error', 'IAS'))


    return parse_sentence(word_list)


# scan("eat bear")

# x = parse_sentence(word_list)

x = scan("eat bear")

# print x.subject
# print x.verb
# print x.object


# word_list = [('verb','eat'),('noun', 'food')]
# This list is supposed to have at least two tuples
# If not, peek will spit out only one character, instead of
# a word
