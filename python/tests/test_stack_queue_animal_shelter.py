from data_structure.stack_queue.stack_queue_animal_shelter import (AnimalShelter,Node,Queue)


def test_enqueu():
    actual = []
    animal = AnimalShelter()
    animal.enqueue('fifo', 'dog')
    actual += [animal.dog.peek()]
    animal.enqueue('lilo', 'cat')
    actual += [animal.cat.peek()]
    excepted = ['fifo', 'lilo']
    assert actual == excepted


def test_enqueu_fail():
    animal = AnimalShelter()
    actual = animal.enqueue('toto', 'elephant')
    excepted = 'This animal cant be in our shelter'
    assert actual == excepted


def test_dequeu():
    actual=[]
    animal = AnimalShelter()
    animal.enqueue('fifo', 'dog')
    animal.enqueue('lilo', 'cat')
    actual +=[animal.dequeue('dog')]
    actual +=[animal.dequeue('cat')]
    excepted = ['fifo', 'lilo']
    assert actual == excepted


def test_dequeu_fail():
    animal = AnimalShelter()
    actual = animal.dequeue('humester')
    excepted = 'This animal not exist'
    assert actual == excepted
