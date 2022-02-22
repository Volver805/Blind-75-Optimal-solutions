In order to solve this problem we basically want to get the middle elemment node and start inserting it in reverse between each node from the first half 
Lets break down this problem into smaller problems
1. we need to get the middle node
2. reverse the right half
3. insert each element from right half after each element of the right half

1. Get middle node
in order to get the middle node of a linked list efficiently we want to make use of slow and fast algorithm
```
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
```
`slow` will be pointing to the middle item right now

2. Reverse the right half
com'on you know how to [reverse a linked list](https://github.com/Volver805/Blind-75-Optimal-solutions/tree/master/206-reverse-linked-list)
```
      # you might improve this section of code
      prev = slow
      curr = slow.next
      prev.next = None
      while curr:
          next = curr.next
          curr.next = prev
          prev = curr
          curr = next
```
3. after each element from first half insert an item from next half
this is pretty much self explanatory we just want to iterate on each item on the left half and insert element from right half
```
        node = head
        while prev.next:
            temp = prev
            prev = prev.next
            temp.next = node.next
            node.next = temp
            node = node.next.next
        return head
```
