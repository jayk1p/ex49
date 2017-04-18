from nose.tools import *
from ex49.parser import Sentence
from ex49 import parser


def test_Sentence():
    sentence_one = Sentence(("noun", "player"),("verb", "eat"), ("noun", "bear"))
    assert_equal(sentence_one.subject, "player")
    assert_equal(sentence_one.verb, "eat")
    assert_equal(sentence_one.object, "bear")


def test_peek():
    peek_one = [("noun", "player"),("verb", "eat"), ("noun", "bear")]
    result = parser.peek(peek_one)

    ## **Remember, you need the "parser" before the ".peek" b/c
    ## you are importing this from another module!!!

    assert_equal(result, "noun")



def test_match():
    match_one = [("stop", "player"),("verb", "eat"), ("noun", "bear")]
    result = parser.match(match_one, "stop")


    assert_equal(result, "stop")


# match_one = [("Stop", "drop"), ('Stop', 'drop'), ("woohooo", 'wip pee')]
# word = match_one.pop(0)
#
# print word[0]
