## Stacks and Queues

## Stack
 Stack is said to be overflown if the space left in the memory heap is not enough to create a node.
![stack](https://static.javatpoint.com/ds/images/ds-linked-list-implementation-stack.png)


## Challenge
<!-- Description of the challenge -->
Create Stack impelement using Linked list to create class named Stack ,also this class take following method(peek,is empty,pop,push)


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Python table challenge
Method | Efficiency
------------ | -------------
push |  O(1)   space=O(1)
 pop |  O(1)   space=O(n)
  peek | O(1)   space=O(1)
  linked-list | O(1)   space=O(1)

## API
<!-- Description of each method publicly available to your Stack and Queue-->
<!-- Description of the challenge -->
* create stack class have,top property,and create an empty stack with instantiated
* the class should contain the following:
1. push:
   * input:value
   * action: new node with value in the top
2. pop:
    * input:none
    * output:return the value in the top  of the stack.
    * action:raise exception when call empty stack
3. peek:
    * input:none
    * output:return boolean if the stack is empty
    * action:raise exception when call empty stack
4. is_empty:
    * input:none
    * action:return boolean if the stack is empty
    <!-- * output:return boolean if the stack is empty -->
## Queue


## Queues
 In a linked queue, each node of the queue consists of two parts i.e. data part and the link part. Each element of the queue points to its immediate next element in the memory.

![stack](https://static.javatpoint.com/ds/images/linked-list-implementation-of-queue.png)


## Challenge
<!-- Description of the challenge -->
Create Querue impelement using Linked list to create class named Querue ,also this class take following method(enqueue,dequeue,peek,is empty)


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Python table challenge
Method | Efficiency
------------ | -------------
enqueue |  O(1)   space=O(1)
dequeue |  O(1)   space=O(n)
  peek | O(1)   space=O(1)
is empty | O(1)   space=O(1)

## API
<!-- Description of each method publicly available to your Stack and Queue-->
<!-- Description of the challenge -->
* create stack class have,top property,and create an empty stack with instantiated
* the class should contain the following:
1. enqueue:
   * input:value
   * action: new node with value in the back of the queue
2. dequeue:
    * input:none
    * output:return the value from thr front of the stack.
    * action:raise exception when call empty queue
3. peek:
    * input:none
    * output:return boolean if the queue is empty
    * action:raise exception when call empty queue
4. is_empty:
    * input:none
    * action:return boolean if the queue is empty
    <!-- * output:return boolean if the stack is empty -->

