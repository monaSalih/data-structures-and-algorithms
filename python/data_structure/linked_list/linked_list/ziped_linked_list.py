from linked_list import (Node,LinkedList)

def ziplist(list1,list2):
    #temp1,temp2,
    current1=list1.head
    current2=list2.head
    print(current1,current2,"result curr")
    new_list=LinkedList()
    while current1 and current2:
        new_list.append(current1.data)
        new_list.append(current2.data)
        current1=current1.next
        current2=current2.next
    return str(new_list)


if __name__=="__main__":
    list1=LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(2)
    
    list2=LinkedList()
    list2.append(5)
    list2.append(9)
    list2.append(4)

    test2=ziplist(list1,list2)
    print(test2)
