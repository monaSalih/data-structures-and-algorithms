from code_challenges.tree_fizz_buzz.tree_fizz_buzz import *

def test_fizz_buzz():
    tree=Ktree()
    tree.add(2)
    tree.add(7)
    tree.add(3)
    tree.add(5)
    tree.add(15)
    tree.add(21)
    tree.add(25)


    exceptected=['2','7','fizz','buzz','fizzbuzz','fizz','buzz']
    actuall=tree.fizz_buzz(tree)
    assert exceptected == actuall

