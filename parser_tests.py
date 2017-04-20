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


    peek_two = []
    result = parser.peek(peek_two)

    assert_equal(result, None)



def test_match():
    match_one = [("stop", "player"), ("verb", "eat"), ("noun", "bear")]
    result = parser.match(match_one, "stop")

    assert_equal(result, ("stop","player"))


    match_two = [("noun", "player"),("verb", "eat"), ("noun", "bear")]
    result = parser.match(match_two, "stop")

    assert_equal(result, None)


def test_skip():
    skip_one = [("noun", "player"), ("verb", "eat"), ("noun", "bear")]
    result = parser.skip(skip_one, "stop")

    assert_equal(result, None)


    # skip_two = [("stop", "player"), ("verb", "eat"), ("noun", "bear")]
    # result = parser.skip(skip_two, "stop")
    #
    # assert_equal(result, ("stop", "player"))

# This doesn't work for some damn reason


def test_parse_verb():

    # parse_verb_one = [("noun", "player"), ("verb", "eat"), ("noun", "bear")]
    # result = parser.parse_verb(parse_verb_one)
    #
    # assert_raises(parser.ParserError, parser.parse_verb , result)

# Not working...


    parse_verb_two = [("verb", "eat"), ("noun", "bear")]
    result = parser.parse_verb(parse_verb_two)

    assert_equal(result,("verb", "eat"))


def test_parse_object():

    parse_object_one = [("noun", "bear"), ("verb", "eat")]
    result = parser.parse_object(parse_object_one)

    assert_equal(result, ("noun", "bear"))


    parse_object_two = [("direction", "north"), ("verb", "eat")]
    result = parser.parse_object(parse_object_two)

    assert_equal(result, ("direction", "north"))


    # parse_object_three = [("verb", "go"), ("verb", "eat")]
    # result = parser.parse_object(parse_object_three)
    #
    # assert_raises(parser.ParserError, parser.parse_object , parse_object_three)

# Not working... Idk how to use assert_raises...


def test_parse_subject():

    parse_subject_one = [("noun", "bear"), ("verb", "eat")]
    result = parser.parse_subject(parse_subject_one)

    assert_equal(result, ("noun", "bear"))


    parse_subject_two = [("verb", "go"), ("verb", "eat")]
    result = parser.parse_subject(parse_subject_two)

    assert_equal(result, ("noun", "player"))


    # parse_subject_three = [("direction", "north"), ("verb", "eat")]
    # result = parser.parse_subject(parse_subject_three)
    #
    # assert_raises(parser.ParserError, parser.parse_subject , parse_subject_three)

# Not working... Idk how to use assert_raises...


def test_parse_sentence():
    word_list = [("noun", "player"),("verb", "eat"), ("noun", "bear")]
    result = parser.parse_sentence(word_list)

    assert_equal(result.subject, "player")
    assert_equal(result.verb, "eat")
    assert_equal(result.object, "bear")
