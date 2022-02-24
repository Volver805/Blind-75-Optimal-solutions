We want to allocate a prehead variable `prehead` and another pointer for iteration `prev`
iterate on nodes from both lists simultaneously until we reach end of one list `while list1 and list2` 
check everytime which element is smaller and set it as next item to our prev then move prev to next element and node from this list only to next element (don't move the other list)
at the end we want to check if one of the lists still has elemented that we didn't iterate on so
```
if list1:
  prev.next = list1
if list2:
  prev.next = list2
