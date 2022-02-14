we want to preform a binary search so lets consider x is the middle element in rotated array [4,5,6,7,0,1,3] so x = 7 and firstElement is the first element in list so firstElement = 4, the inflection point which is the point were the actual start of list exists

if x > firstElement this means x is before the inflection point
if x < firstElement this means x is after the inflection point

if x is before the inflection point this means the minimum number must reside in the right
if x is after the inflection point this means the minimum number must reside on the left
