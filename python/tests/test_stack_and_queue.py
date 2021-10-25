from math import exp
# from data_structure.stack_queue.stack_and_queu import __version__
from data_structure.stack_queue.stack_queue_animal_shelter import (Node,Queue ,AnimalShalter)
import pytest



def test_inqueue():
    push_node=Queue()
    push_node.enqueue(2)
    excepted=push_node.size
    actuall=1
    assert excepted==actuall


def test_push_multiple_values():
    push_node=Queue()
    push_node.enqueue(2)
    push_node.enqueue(3)
    excepted=push_node.size
    actuall=2
    assert excepted==actuall

def test_pop_off_stack():
    push_node=Queue()
    push_node.enqueue(2)
    push_node.enqueue(3)
    push_node.dequeu()
    excepted=push_node.size
    actuall=1
    assert excepted==actuall

def test_pop_all_stack():
    push_node=Queue()
    push_node.enqueue(2)
    push_node.enqueue(3)
    push_node.dequeu()
    push_node.dequeu()
    excepted=push_node.size
    actuall=0
    assert excepted==actuall

def test_empty_stack():
    stack_empty=Queue()
    stack_empty.is_empty()

def test_instantiate_empty_stack():
    stack_empty=Queue()
    stack_empty.is_empty()

# # def test_instantiate_empty_stack():
# #     stack_empty=Stack()
# #     stack_empty.is_empty()

# def test_peek_next():
#     push_node=Queue()
#     push_node.enqueue(2)
#     push_node.enqueue(3)
#     excepted=push_node.first_next()
#     actuall=2
#     assert excepted==actuall

def test_peek_empty_stack():
    stack_empty=Queue()
    with pytest.raises(Exception):
        stack_empty.first()
        stack_empty.dequeu()
