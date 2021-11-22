# Challenge Summary
<!-- Description of the challenge -->
write function that take two binary trees as parameters.
Using Hashmap implementation as a part of your algorithm, return a set of values found in both trees.
## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
time O(logn)
space O(n)

## Solution
<!-- Show how to run your code, and examples of it in action -->
write following code
```
def tree_intersection(tree1, tree2):
    arr=[]
    hash = HashTable()
    if tree1.root== None or tree.root==None:
        return 'input tree is empty'
    def walk(node:Node):
        if node:
            hash.add(str(node.data),None)
        if node.left:
            walk(node.left)
        if node.right:
            walk(node.right)
    walk(tree1.root)
    def walk2(node:Node):
        if node:
            if hash.contains(str(node.data)):
                arr.append(node.data)
        if node.left:
            walk2(node.left)
        if node.right:
            walk2(node.right)
        return arr
    return walk2(tree2.root)

```

Solve the lab with these girl:
- Dua AL-jaradat
- Tasnem alabsi
- Tahany Ali
- Haneen Hashlamoun
