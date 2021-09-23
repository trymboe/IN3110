from os import error
from typing import Type, ValuesView


class Array:
    arrayType = None
    arr = []
    shape = 0

    def __init__(self, shape, *values,):
        self.arr = []
        """
        Initialize an array of 1 or 2-dimensionality. Elements can only be of type:
        - int
        - float
        - bool
        Array is true homogeneous
        
        Args:
            shape (tuple - 2d) (int - 1d): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.
        Raises:
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """
        self.shape = shape
        values = tuple(values[0])
        if isinstance(shape, int):
            values = list(values)
            if shape != len(values):
                raise ValueError("ValueError: the number of values does not fit with the shape.")
            self.arr = values
            self.arrayType = type(self.arr[0])
            for value in self.arr:
                if  isinstance(value, self.arrayType):
                    pass
                else:
                    raise ValueError("The values are not of the same type")
        if isinstance(shape, tuple):
            self.make_two_d(values)
                 
    def make_two_d(self,values):
        """Takes a list of 1D elements and appends it into self.arr as a 2D list
        Args:
            values (Bool, foat, int)
        """

        self.arrayType = type(values[0])
        l = len(values)
        x = self.shape[0]
        y = self.shape[1]
        count = 0
        if (x*y) == l:
            for i in range(x):
                self.arr.append([])
                for j in range(y):
                    if isinstance(values[i], self.arrayType):
                        self.arr[i].append(values[count])
                        count += 1
                    else:
                        raise ValueError("The values are not of the same type")
        else:
            raise ValueError("Number of values does not match dimensions")
       
    def __str__(self):
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """
        return str(self.arr)

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        Raises:
            TypeError if types do not match
            ValueError if length of arrays do not match
        """
        new = [None] * len(self.arr)
        first = self.arr

        #when it is 2D array
        if isinstance(self.shape, tuple):
            first = self.flat_array(self)
            if isinstance(other, Array):
                length = other.shape[0]*other.shape[1]
                other = Array((length), self.flat_array(other))
            new = [None] * len(first)
        

        #check if other is number og array
        if isinstance(other, Array):
            if len(first) == len(other.arr):
                for i in range(len(first)):
                    if isinstance(other.arr[i], self.arrayType):
                        new[i] = first[i] + other.arr[i]
                    else:
                        raise TypeError("Type do not match")
            else:
                raise ValueError("Length do not match")
        elif isinstance(other, self.arrayType):
            for i in range(len(first)):
                new[i] = first[i] + other
        else:
            raise TypeError("The values are not of the same type, expected", self.arrayType, "or Array type")
            
        return Array(self.shape, new) 

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        return self.__add__(other)     

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.
        Returns:
            Array: the difference as a new array.
        Raises:
            TypeError if types do not match
            ValueError if length of arrays do not match
        """
        new = [None] * len(self.arr)
        first = self.arr

        #when it is 2D array
        if isinstance(self.shape, tuple):
            first = self.flat_array(self)
            if isinstance(other, Array):
                length = other.shape[0]*other.shape[1]
                other = Array((length), self.flat_array(other))
            new = [None] * len(first)
        

        #check if other is number og array
        if isinstance(other, Array):
            if len(first) == len(other.arr):
                for i in range(len(first)):
                    if isinstance(other.arr[i], self.arrayType):
                        new[i] = first[i] - other.arr[i]
                    else:
                        raise TypeError("Type do not match")
            else:
                raise ValueError("Length do not match")
        elif isinstance(other, self.arrayType):
            for i in range(len(first)):
                new[i] = first[i] - other
        else:
            raise TypeError("The values are not of the same type, expected", self.arrayType, "or Array type")
            
        return Array(self.shape, new) 
 
    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number being subtracted from.
        Returns:
            Array: the difference as a new array.
        Raises:
            TypeError if types do not match
            ValueError if length of arrays do not match
        """
        new = [None] * len(self.arr)
        first = self.arr

        #when it is 2D array
        if isinstance(self.shape, tuple):
            first = self.flat_array(self)
            if isinstance(other, Array):
                length = other.shape[0]*other.shape[1]
                other = Array((length), self.flat_array(other))
            new = [None] * len(first)
        

        #check if other is number og array
        if isinstance(other, Array):
            if len(first) == len(other.arr):
                for i in range(len(first)):
                    if isinstance(other.arr[i], self.arrayType):
                        new[i] = other.arr[i] - first[i]
                    else:
                        raise TypeError("Type do not match")
            else:
                raise ValueError("Length do not match")
        elif isinstance(other, self.arrayType):
            for i in range(len(first)):
                new[i] = other - first[i]
        else:
            raise TypeError("The values are not of the same type, expected", self.arrayType, "or Array type")
            
        return Array(self.shape, new) 

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        Raises:
            TypeError if types do not match
            ValueError if length of arrays do not match
        """

        new = [None] * len(self.arr)
        first = self.arr

        #when it is 2D array
        if isinstance(self.shape, tuple):
            first = self.flat_array(self)
            if isinstance(other, Array):
                length = other.shape[0]*other.shape[1]
                other = Array((length), self.flat_array(other))
            new = [None] * len(first)
        

        #check if other is number og array
        if isinstance(other, Array):
            if len(first) == len(other.arr):
                for i in range(len(first)):
                    if isinstance(other.arr[i], self.arrayType):
                        new[i] = first[i] * other.arr[i]
                    else:
                        raise TypeError("Type do not match")
            else:
                raise ValueError("Length do not match")
        elif isinstance(other, self.arrayType):
            for i in range(len(first)):
                new[i] = first[i] * other
        else:
            raise TypeError("The values are not of the same type, expected", self.arrayType, "or Array type")
            
        return Array(self.shape, new) 

    def __rmul__(self, other):
        '''new = self
        #check if other is number og array
        if len(self) == len(other):
            new = self
            for i in self:
                for j in other:
                    pass'''
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        return self.__mul__(other)       
        
    def __eq__(self, other):
        """Compares an Array with another Array.
        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.
        Args:
            other (Array): The array to compare with this array.
        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.
        """

        first = self.arr
        #when it is 2D array
        if isinstance(self.shape, tuple):
            first = self.flat_array(self)
            if isinstance(other.shape, tuple):
                length = other.shape[0]*other.shape[1]
                other = Array((length), self.flat_array(other))
            new = [None] * len(first)

        if isinstance(other, Array) and (len(first) == len(other.arr)):
            for i in range(len(first)):
                if first[i] != other.arr[i]:
                    return False
        else:
            return False
        return True

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.
        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.
        Args:
            other (Array, float, int): The array or number to compare with this array.
        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.
        Raises:
            ValueError: if the shape of self and other are not equal.
            TypeError: if type in Array is not the same
        """
        new = [None] * len(self.arr)
        first = self.arr

        #when it is 2D array
        if isinstance(self.shape, tuple):
            first = self.flat_array(self)
            if isinstance(other.shape, tuple):
                length = other.shape[0]*other.shape[1]
                other = Array((length), self.flat_array(other))
            new = [None] * len(first)


        if isinstance(other, Array):
            if len(other.arr) == len(first):
                for i in range(len(first)): 
                    if first[i] == other.arr[i]:
                        new[i] = True
                    else:
                        new[i] = False
            else:
                raise ValueError("Size is not equal")
        else:
            raise TypeError("Not an array of same type")
        
        return Array(self.shape, new) 
        
        
        pass
    
    def min_element(self):
        """Returns the smallest value of the array.
        Only needs to work for type int and float (not boolean).
        Returns:
            float/int: The value of the smallest element in the array.
        """
        first = self.arr
        if isinstance(self.shape, tuple):
            first = self.flat_array(self)

        min_el=first[0]
        for i in first:
            if i < min_el:
                min_el = i
        return min_el

    def __getitem__(self, item): 

        """Returns value of item in array.
        Args:
            item (int): Index of value to return.
        Returns:
            value: Value of the given item.
        """
        return self.arr[item]

    def flat_array(self, too_be_flattened):
        """Flattens the N-dimensional array of values into a 1- dimensional array.
        Returns:
            list: flat list of array values.
        """
        
        flat_array = [None] * (too_be_flattened.shape[0]*too_be_flattened.shape[1])
        count = 0
        for i in range(too_be_flattened.shape[0]):
            for j in range(too_be_flattened.shape[1]):
                flat_array[count] = too_be_flattened.arr[i][j]
                count += 1
        return flat_array
