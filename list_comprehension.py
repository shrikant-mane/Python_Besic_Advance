def list_comprehension():
    squares = [x**2 for x in range(10)]
    print(squares)

    evens = [x for x in range(10) if x % 2 == 0]
    print(evens)

    pairs = [(x,y) for x in range(3) for y in range(3)]
    print(pairs)

    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    flattered = [item for row in matrix for item in row]
    print(flattered)

    numbers = [-5, 10, 2, -78, -2, 0]
    negative_numbers = [x if x<0 else 0 for x in numbers]
    print(negative_numbers)

    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    dictionary = {k: v for k,v in zip(keys, values)}
    print(dictionary)

list_comprehension()