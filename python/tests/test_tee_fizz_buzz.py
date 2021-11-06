from data_structure.tree_fizz_buzz.tee_fizz_buzz import (Node,Binary_search_tree, fizzbuzz)
# fizzBuzz,fizzBuzzTree,BinaryTree,
def test_fizzbuzztree():
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

    expected = ['Fizz', 'Buzz', 'Fizz', 'FizzBuzz', '4', '2']
    actual = fizzbuzz(tree).bfs()
    assert actual == expected
    print("test_bfs passed")

