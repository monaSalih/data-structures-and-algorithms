from data_structure.linked_list.linked_list.ziped_linked_list import ziplist
from data_structure.linked_list.linked_list.linked_list import (LinkedList,Node)



def test_zlist():
    list1=LinkedList()
    list1.append(1)
    list1.append(3)

    list2=LinkedList()
    list2.append(5)
    list2.append(9)

    expected="{ 1 } -> { 5 } -> { 3 } -> { 9 } -> NULL"
    actuall=ziplist(list1,list2)
    assert expected==actuall


def test_zlist2():
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
