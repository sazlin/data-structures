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


def test_set(empty_table, word_list):
    empty_table.set('first', 1)
    empty_table.set('second', 2)
    empty_table.set('third', 3)

