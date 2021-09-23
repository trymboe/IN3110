# README.md Assignment3 

## Task 3.1/3.2/3.3/3.4

### Prerequisites

You need to have python 3 installed and both array.py and test_Array.py in the same folder

### Functionality

This is the implementation of the datatype array in python. This array is a completely homogeneus datatype. That means that each array only can contain one datatype. It only supports int, float or bool. This array can be used in 1D and 2D, but not more dimensions.
This array supports:
__add__, __sub__, __mul__, __eq__, __radd__, __rsub__, __rmul__, __getitem__ and 
.is_equal() 

exact functionality of these methods can be found in the respective docstring in array.py


### Missing Functionality

The array can only be made if the number of values are exactly the same as the shape allows 

### Usage

To make an array you need to define the shape, as well as the data you want to put in the array.

1D array:
a = Array((5), [3,1,2,3,9])
gives:
[3, 1, 2, 3, 9]

2D array:
b = Array((3,2), [0,1,2,3,4,5])
gives:
[[0, 1], [2, 3], [4, 5]]

add:
a+b / b+a / 10+a / a+10
Returns the answer to the calculation

sub:
a-b / b-a / 10-a / a-10
Returns the answer to the calculation

mul:
a*b / b*a / 10*a / a*10
Returns the product of the multiplication

eq:
a == b / b == a
Returns true or false

getitem:
a[0]
Gives the 0th element of Array a

