from abc import ABC
from code_challenges.linked_list.linked_list import (Node,LinkedList, ziplist)
import pytest


def test_node_has_int_data():
    # Arrange any data that you need to run your test
    expected = 1

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = node.data

    # Assert
    assert actual == expected

def test_node_has_str_data():
    # Arrange any data that you need to run your test
    expected = "a"

    # Act on the subject of the test to produce some actual output
    node = Node("a")
    actual = node.data

    # Assert
    assert actual == expected


def test_node_is_a_Node():
    # Arrange any data that you need to run your test
    expected = "Node"

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = type(node).__name__

    # Assert
    assert actual == expected

def test_node_without_value():
    with pytest.raises(TypeError):
         Node()




def test_new_linked_list_is_empty():
  expected = None

  ll = LinkedList()
  actual = ll.head

  assert actual == expected

def test_linked_list_insert():
  # Arrange
  expected = 1
  ll = LinkedList()

  # Act
  ll.insert(1)
  node = ll.head
  actual = node.data

  # Assert
  assert actual == expected

def test_linked_list_insert_twice():
  # Arrange
  expected = 0
  ll = LinkedList()

  # Act
  ll.insert(1)
  ll.insert(0)
  node = ll.head
  actual = node.data
  # Assert
  assert actual == expected
  assert ll.head.next.data == 1


def test_includes():
    # Arrange
    ll=LinkedList()
    ll.insert(1)
    ll.insert(0)
    # Act
    expected=True
    actuall=ll.includes(1)
    # Assert
    assert actuall==expected


def test__str__():
    ll=LinkedList()
    ll.insert(1)
    ll.insert(0)

     #output
    expected= "{ 0 } -> { 1 } -> NULL"
    actul=ll.__str__()

    assert expected==actul


def test_append():
    ll=LinkedList()
    ll.append(3)
    ll.append(4)
    #output
    expected= "{ 3 } -> { 4 } -> NULL"
    actull=ll.__str__()
    assert expected==actull


def test_insert_before():
  ll=LinkedList()
  ll.append(3)
  ll.append(4)
  ll.insert_before(4,8)
  #output
  expected= "{ 3 } -> { 8 } -> { 4 } -> NULL"
  actull=ll.__str__()
  assert expected==actull


def test_insert_after():
  ll=LinkedList()
  ll.append(3)
  ll.append(4)
  #output
  ll.insert_after(4,8)
  expected= "{ 3 } -> { 4 } -> { 8 } -> NULL"
  actull=ll.__str__()
  assert expected==actull

def test_kth():
    ll=LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)

    expected=3
    actuall=ll.kth(2)
    assert expected==actuall



def test_zlist():
    list1=LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(2)

    list2=LinkedList()
    list2.append(5)
    list2.append(9)
    list2.append(4)

    expected="{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> NULL"
    actuall=ziplist(list1,list2)
    assert expected==actuall


