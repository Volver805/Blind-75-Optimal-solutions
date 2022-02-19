## Approach One - Hash Map [Memory O(n)]
in this we simply define a hash map `hashMap` and iterate on the linked list notes, if node in hashMap return True if not add it to hashMap and check next node

## Approach Two - slow and fast [Memory O(1)]
we use two variables, slow and fast
slow: starts as head, moves one step at a time
fast: starts at head.next, moves on step at a time
if fast is at any point None this mean that there's no cycles so return False
if fast == slow return True
[for more info about slow and fast pointers approach](https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed)
