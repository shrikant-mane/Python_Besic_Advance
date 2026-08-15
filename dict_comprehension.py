def dictionary_comprehension():
    square_dict = {x:x**2 for x in range(10)}
    print(square_dict)

    even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
    print(even_squares)

    multiplication_table = {(x,y): x*y for x in range(1,3) for y in range(1,3)}
    print(multiplication_table)

    original = {'x':100, 'y':200, 'z':300}
    rev_dict = {v: k for k,v in original.items()}
    print(rev_dict)

dictionary_comprehension()

