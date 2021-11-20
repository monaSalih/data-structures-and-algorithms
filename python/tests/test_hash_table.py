from data_structure.hash_table.hash_table import HashTable
import pytest

@pytest.fixture
def hashtable():
	return HashTable()

def test_hash(hashtable):
	expected = 700
	actual = hashtable._HashTable__hash("d")
	assert actual == expected

def test_hash_word(hashtable):
	expected = 376
	actual =  hashtable._HashTable__hash("dd")
	assert actual == expected


def test_add():
  hash = HashTable()
  hash.add('mona',"Alobisat")
  expected= 941
  actual=hash._HashTable__hash('mona')
  assert expected == actual

def test_none():
  hash = HashTable()
  hash.add('mona',"Alobisat")
  expected= None
  actual=hash.get('cd')
  assert expected == actual

def test_collision():
  hash = HashTable()
  hash.add('mona',"Alobisat")
  hash.add('salih',"mona")
  expected = 941
  expected2= 631
  actual=hash._HashTable__hash('mona')
  actual2=hash._HashTable__hash('salih')
  assert expected == actual
  assert expected2 == actual2

def test_collision_value():
  hash = HashTable()
  hash.add('mona',"Alobisat")
  hash.add('mona',"salih")
  expected = "salih"

  actual=hash.get('mona')

  assert expected == actual

