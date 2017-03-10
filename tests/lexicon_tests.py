from nose.tools import *
from lexicon import lexicon

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'), ('direction', 'south'), ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go drink open")
    assert_equal(result, [('verb', 'go'), ('verb', 'drink'), ('verb', 'open')])

def test_nouns():
    assert_equal(lexicon.scan("table"), [('noun', 'table')])
    result = lexicon.scan("table door")
    assert_equal(result, [('noun', 'table'), ('noun', 'door')])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', '1234')])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', '3'), ('number', '91234')])

def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lexicon.scan("door IAS chair")
    assert_equal(result, [('noun', 'door'), ('error', 'IAS'), ('noun', 'chair')])
