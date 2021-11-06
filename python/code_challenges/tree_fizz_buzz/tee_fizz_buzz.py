class Node:
    def __init__(self, data):
        self.data = data
        self.node_child = []


class Queue:
    def __init__(self, collection=[]):
        self.data = collection

    def peek(self):
        if len(self.data):
            return True
        return False

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)


class Binary_search_tree:
    def __init__(self):
        self.root = None

    def bfs(self):
        """
        binary tree method
        input:none
        output: binary tree
        """
        breadth = Queue()
        breadth.enqueue(self.root)

        list_of_items = []
        while breadth.peek():
            front = breadth.dequeue()
            list_of_items += [front.data]
            if front.node_child:
                for item in front.node_child:
                    breadth.enqueue(item)
        return list_of_items


def fizzBuzz_checker(node):
    """
        check tree node can divide on 3 or 5 or both
        input: node
        output: fizz/buzz/fizzbuzz
    """
    if not node.data % 5 and not node.data % 3:
        return "FizzBuzz"
    elif not node.data % 3:
        return "Fizz"
    elif not node.data % 5:
        return "Buzz"
    else:
        return str(node.data)


def fizzbuzz(tree):

    """
    binary tree convert to k-tree
    input: ktree
    output:fizzBuzz ktree
    """
    breadth = Queue()
    breadth.enqueue(tree.root)
    while breadth.peek():
        current = breadth.dequeue()
        current.data = fizzBuzz_checker(current)
        if current.node_child:
            for item in current.node_child:
                breadth.enqueue(item)

    tree2 = Binary_search_tree()
    tree2=tree

    return tree2


tree = Binary_search_tree()
a_node = Node(3)
b_node = Node(5)
c_node = Node(4)
d_node = Node(9)
e_node = Node(2)
f_node = Node(15)


a_node.node_child.append(b_node)
a_node.node_child.append(d_node)
b_node.node_child.append(c_node)
c_node.node_child.append(e_node)
a_node.node_child.append(f_node)

tree.root = a_node


print(fizzbuzz(tree).bfs())
