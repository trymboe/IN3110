from array import Array

def test_nice_output():
    a = Array((5), [3,1,2,3,9])
    b = Array((3,2), [0,1,2,3,4,5])
    print(a)
    print(b)

def test_add_element_wise():
    a = Array((5), [3,1,2,3,9])
    b = Array((5), [3,1,2,3,3])
    c = a+b
    e = Array((5), [3.0,1.1,2.0,3.0,9.0])
    f = Array((5), [3.0,1.1,2.0,3.0,9.0])

    g = Array((5,2), [0.0,1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9])
    h = Array((5,2), [0.0,1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9])
    i = Array((5,2), [0,1,2,3,4,5,6,7,8,9])
    j = Array((5,2), [9,8,7,6,5,4,3,2,1,0])
    

    #Checking for element-wise 1-d add
    assert a+c == Array((5),[9,3,6,9,21])
    assert a+b == Array((5),[6,2,4,6,12])
    assert a+b+c == Array((5),[12,4,8,12,24])
    assert a+10 == Array((5), [13,11,12,13,19])
    assert 10+a == Array((5), [13,11,12,13,19])
    assert e+f == Array((5), [6.0, 2.2, 4.0, 6.0, 18.0])
    #Checking for element-wise 2-d add
    assert g+h == Array((5,2), [0.0, 2.2, 4.4, 6.6, 8.8, 11.0, 13.2, 15.4, 17.6, 19.8])
    assert i+j == Array((5,2), [9,9,9,9,9,9,9,9,9,9])
    assert i+5 == Array((5,2), [5,6,7,8,9,10,11,12,13,14])


def test_sub_element_wise():
    a = Array((5), [5,112,-2,52,0])
    b = Array((5), [70,24,24,-33,18])
    e = Array((5), [5.0,112.0,-2.0,52.0,0.5])
    f = Array((5), [70.0,24.0,24.0,-33.0,18.2])
    c = a-b

    i = Array((4,3), [0,1,2,3,4,5,6,7,8,9,10,11])

    #Checking for element-wise 1-d sub
    assert a-b == Array((5),[-65,88,-26,85,-18])
    assert a-c == Array((5),[70,24,24,-33,18])
    assert a-b-c == Array((5), [0,0,0,0,0])
    assert a-10 == Array((5), [-5,102,-12,42,-10])
    assert 10-a == Array((5), [5,-102,12,-42,10])
    assert e-f == Array((5), [-65.0,88.0,-26.0,85.0,-17.7])
    #Checking for element-wise 2-d sub
    assert 10-i == Array((4,3), [10,9,8,7,6,5,4,3,2,1,0,-1])


def test_mul_element_wise():
    a = Array((5), [3,1,2,3,9])
    b = Array((5), [3,1,2,3,3])
    c = a*b
    i = Array((4,3), [0,1,2,3,4,5,6,7,8,9,10,11])
    l = Array((4,3), [10,10,10,10,10,10,10,10,10,10,10,10])
    h = Array((4,3), [0.0,1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,11.0,11.1])

    #Checking for element-wise 1-d mul
    assert a*b == Array((5),[9,1,4,9,27])
    assert a*c == Array((5),[27,1,8,27,243])
    assert a*b*c == Array((5),[81,1,16,81,729])
    assert a*10 == Array((5), [30,10,20,30,90])
    assert 10*a == Array((5), [30,10,20,30,90])

    assert i*l == Array((4,3), [0,10,20,30,40,50,60,70,80,90,100,110])
    assert 10.0*h == Array((4,3), [0.0,11.0,22.0,33.0,44.0,55.0,66.0,77.0,88.0,99.0,110.0,111.0])

def test_eq():
    a = Array((5), [3,1,2,3,9])
    b = Array((5), [3,1,2,3,3])
    c = Array((5), [3,1,2,3,9])
    d = Array((5), [True,False,False,False,True])
    e = Array((5), [True,False,False,False,True])

    f = Array((2,2), [1.0,2.0,3.0,4.1])
    g = Array((2,2), [1.0,2.0,3.0,4.1])
    
    #Checking the __eq__ function 1D
    assert (a == b) == False
    assert (a == c) == True
    assert (b == c) == False
    assert (a == c == d) == False
    assert (e == d) == True
    #Checking the __eq__ function 2D
    assert (f == g) == True
    assert (f == a) == False

def test_is_equal():
    a = Array((5), [3,1,2,3,9])
    b = Array((5), [3,1,2,3,3])
    c = Array((5), [3,1,2,3,9])
    d = Array((5), [False,True,True,False,True])
    e = Array((5), [True,False,False,False,True])

    f = Array((2,2), [1.0, 2.0, 3.0, 4.1])
    g = Array((2,2), [1.0, 2.0, 3.0, 4.1])
    h = Array((2,2), [1.0, 2.2, 3.2, 4.1])


    #Checking is_equal function 1D
    assert (a.is_equal(b)) == Array((5), [True, True, True, True, False])
    assert (a.is_equal(c)) ==  Array((5), [True, True, True, True, True])
    assert (b.is_equal(c)) ==  Array((5), [True, True, True, True, False])
    assert (d.is_equal(e)) ==  Array((5), [False, False, False, True, True])
    #Checking is_equal function 2D
    assert (f.is_equal(g)) == Array((2,2), [True, True, True, True])
    assert (f.is_equal(h)) == Array((2,2), [True, False, False, True])


def test_min():
    a = Array((5), [3,1,2,3,9])
    b = Array((5), [3,1,2,3,-9])
    h = Array((4,3), [0.0,1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,11.0,-11.1])

    #Checking the min function
    assert a.min_element() == 1
    assert b.min_element() == -9
    assert h.min_element() == -11.1
    

test_nice_output()
test_add_element_wise()
test_sub_element_wise()
test_mul_element_wise()
test_eq()
test_is_equal()
test_min()

print("Everything seems be working")