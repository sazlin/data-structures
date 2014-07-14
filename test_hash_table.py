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
    assert 448 == empty_table._hash('test')
    assert 448 == empty_table._hash('sett')
    assert 97 == empty_table._hash('a')
    assert 65 == empty_table._hash('A')
    assert 61 == empty_table._hash('Hello World!')
    with pytest.raises(TypeError):
        empty_table._hash(9)
    with pytest.raises(TypeError):
        empty_table._hash(9.)


def test_set(empty_table):
    empty_table.set('test', 1)
    empty_table.set('sett', 2)
    empty_table.set('a', 3)
    empty_table.set('A', 4)
    empty_table.set('Hello World!', 5)
    assert empty_table._bucket_list[448][0] == ('test', 1)
    assert empty_table._bucket_list[448][1] == ('sett', 2)
    assert empty_table._bucket_list[97][0] == ('a', 3)
    assert empty_table._bucket_list[65][0] == ('A', 4)
    assert empty_table._bucket_list[61][0] == ('Hello World!', 5)
    with pytest.raises(TypeError):
        empty_table.set(9, 9)


def test_get(empty_table):
    empty_table.set('test', 1)
    empty_table.set('sett', 2)
    empty_table.set('a', 3)
    empty_table.set('A', 4)
    empty_table.set('Hello World!', 5)
    assert empty_table.get('test') == 1
    assert empty_table.get('sett') == 2
    assert empty_table.get('a') == 3
    assert empty_table.get('A') == 4
    assert empty_table.get('Hello World!') == 5
