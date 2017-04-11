from nose.tools import *
from ex49 import parser




def test_verbs():
    result = parser.scan("eat bear")
    assert_equal(result, [('noun', 'player'),
                          ('verb', 'eat'),
                          ('noun', 'bear')])

    ## The "eat" is made into the (verb,eat) tuple, but
    ## the program isn't matching the "verb" with line 72
    ## I don't know why




# this is a case when you put in just "one word"
# This case porbably doesn't work b/c of line 78 which
# needs to equalize the "word" and the 'noun', which can't happen
# b/c the word is just a word, not a sub, verb, noun, etc
# IN other words, this info is not given. We need to have it ourselves
# The only way I can think of this is to have a tuple like I did
# in ex48


# def test_object():
#     assert_equal
#
#
# def test_subject():
#     assert_equal(parse_sentence("go"), [('verb', 'go')])
#     result = lexicon.scan("go kill eat")
#     assert_equal(result, [('verb', 'go'),
#                           ('verb', 'kill'),
#                           ('verb', 'eat')])
