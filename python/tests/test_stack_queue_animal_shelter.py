from data_structure.stack_queue.stack_queue_animal_shelter import (AnimalShelter,Node,Queue)


def test_enqueue():
    actual = []
    animal = AnimalShelter()
    animal.enqueue('fifo', 'dog')
    actual += [animal.dog.peek()]
    animal.enqueue('lilo', 'cat')
    actual += [animal.cat.peek()]
    excepted = ['fifo', 'lilo']
    assert actual == excepted


def test_enqueue_fail():
    animal = AnimalShelter()
    actual = animal.enqueue('toto', 'elephant')
    excepted = 'This animal cant be in our shelter'
    assert actual == excepted


def test_dequeue():
    animal = AnimalShelter()
    animal.enqueue('fifo', 'dog')
    animal.enqueue('lilo', 'cat')
    actual = [animal.dequeue('dog'), animal.dequeue('cat')]
    excepted = ['bull', 'soker']
    assert actual == excepted


def test_dequeue_fail():
    animal = AnimalShelter()
    actual = animal.dequeue('rabbit')
    excepted = 'This animal not exist'
    assert actual == excepted
