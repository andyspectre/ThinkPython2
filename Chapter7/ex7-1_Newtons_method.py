import math

def mysqrt(v):
    """Compute the square root of v using Newton's method: start with an
    approximate answer and iteratively improving it
    """
    estimate = v/2+1    # Arbitrary estimate of the square root of v
    epsilon = 0.0000001  
    while True:
        approx = (estimate + v/estimate)/2    # Newton's formula
        if abs(approx - estimate) < epsilon:
            return approx
        estimate = approx

def test_square_root(v):
    """Print a table that, for all the numbers in the range v, 
    compares the square roots calculated with the 
    Newton's method with those calculated with the built in function sqrt()
    and display the absolute error between the two.
    """
    n = float(1) 
    print('n', ' '*10, 'mysqrt(n)', ' '*10, 'math.sqrt(n)', ' '*10, 'diff') 
    print('-', ' '*10, '---------', ' '*10, '------------', ' '*10, '----') 

    for i in range(v):
        my_square = mysqrt(n) 
        math_square = math.sqrt(n) 
        abs_error = abs(math_square - my_square)
        x = str(n)
        if (len(x) >= 4):
            val = x+(' '*(9-(len(x)-3)))
        else:
            val = x+' '*9

        perfect_square = math_square*math_square == n
        my_square = format(my_square, '.12f') 
        math_square = format(math_square, '.12f')
        abs_error = format(abs_error, '.12g')

        if (perfect_square): 
            my_square = my_square[:3]
            math_square = math_square[:3]
            space1 = ' '*16
            space2 = ' '*19
        else:
            space1 = ' '*5
            space2 = ' '*8
                
        print(val, my_square, space1, math_square, space2, abs_error) 
        n += 1

def ask_user():
    """Prompt the user to enter how many numbers to be calculated"""
    v = int(input('Enter how many numbers you want to calculate: '))
    test_square_root(v)

ask_user()
