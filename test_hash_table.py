import pytest
from hash_table import HashTable


@pytest.fixture(scope='module')
def word_list():
    with open('/usr/share/dict/words', 'r') as f:
        words = f.readlines()
    return words


@pytest.fixture(scope='function')
def empty_table():
    return HashTable()


def test_hash_table_base_init(empty_table):
    assert len(empty_table._bucket_list) == 1024


def test_hash_table_init():
    table = HashTable(512)
    assert len(table._bucket_list) == 512


def test_hash(empty_table):
    assert 448 == empty_table.hash('test')
    assert 448 == empty_table.hash('sett')
    assert 97 == empty_table.hash('a')
    assert 65 == empty_table.hash('A')
    assert 61 == empty_table.hash('Hello World!')
    with pytest.raises(TypeError):
        empty_table.hash(9)
    with pytest.raises(TypeError):
        empty_table.hash(9.)


def test_set(empty_table):
    table = empty_table
    table.set('test', 1)
    table.set('sett', 2)
    table.set('a', 3)
    table.set('A', 4)
    table.set('Hello World!', 5)
    table.set('Hello World!', 6)
    assert table._bucket_list[448][0] == ['test', 1]
    assert table._bucket_list[448][1] == ['sett', 2]
    assert table._bucket_list[97][0] == ['a', 3]
    assert table._bucket_list[65][0] == ['A', 4]
    assert table._bucket_list[61][0] == ['Hello World!', 6]
    with pytest.raises(TypeError):
        empty_table.set(9, 9)


def test_get(empty_table):
    table = empty_table
    table.set('test', 1)
    table.set('sett', 2)
    table.set('a', 3)
    table.set('A', 4)
    table.set('Hello World!', 5)
    assert table.get('test') == 1
    assert table.get('sett') == 2
    assert table.get('a') == 3
    assert table.get('A') == 4
    assert table.get('Hello World!') == 5
    with pytest.raises(KeyError):
        table.get("not there")
    with pytest.raises(TypeError):
        table.get(9)


def test_big_table(word_list):
    table = HashTable(4096)
    [table.set(word, word) for word in word_list]
    assert [table.get(word) == word for word in word_list]
    for word in word_list:
        print "expected: {}, seen: {}".format(word, table.get(word))
