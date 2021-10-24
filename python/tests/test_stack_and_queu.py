from math import exp

from data_structure.stack_queue.stack_queue_pseudo import (Pseudo_Queue,Stack)
from data_structure.stack_queue.stack_and_queu import (Queue, Stack,Node)
import pytest

#========================================================stack test
def test_push():
    push_node=Stack()
    push_node.push(2)
    excepted=push_node.size
    actuall=1
    assert excepted==actuall

# # @pytest.mark.skip('todo')
def test_push_multiple_values():
    push_node=Stack()
    push_node.push(2)
    push_node.push(3)
    excepted=push_node.size
    actuall=2
    assert excepted==actuall

def test_pop_off_stack():
    push_node=Stack()
    push_node.push(2)
    push_node.push(3)
    push_node.pop()
    excepted=push_node.size
    actuall=1
    assert excepted==actuall

def test_pop_all_stack():
    push_node=Stack()
    push_node.push(2)
    push_node.push(3)
    push_node.pop()
    push_node.pop()
    excepted=push_node.is_empty()
    actuall=True
    assert excepted==actuall

def test_empty_stack():
    stack_empty=Stack()
    stack_empty.is_empty()

def test_instantiate_empty_stack():
    stack_empty=Stack()
    stack_empty.is_empty()

# def test_instantiate_empty_stack():
#     stack_empty=Stack()
#     stack_empty.is_empty()

def test_peek_next():
    push_node=Stack()
    push_node.push(2)
    push_node.push(3)
    excepted=push_node.peek_next()
    actuall=2
    assert excepted==actuall

def test_peek_empty_stack():
    stack_empty=Stack()
    with pytest.raises(Exception):
        stack_empty.peek()
        stack_empty.pop

#========================================================queue test

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
#=========================================
def test_pesudo_enqueue():
    queu=Pseudo_Queue()
    queu.enqueue(1)
    actuall=1
    excepted=queu.first_stack.top.value
    assert actuall==excepted
#=========================================
def test_psudo_enqueue2():
    queu=Pseudo_Queue()
    queu.enqueue(1)
    queu.enqueue(2)
    #output
    actul=2
    expected=queu.first_stack.top.value
    assert  actul==expected
#=========================================
# @pytest.mark.skip
# def test_pesudo_denqueue():
#     queu=Pseudo_Queue
#     queu.enqueue("1")
#     queu.dequeue()
#     actul=1
#     expected=queu.secound_stack.pop()

#     assert  actul==expected
