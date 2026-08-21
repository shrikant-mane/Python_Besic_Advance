try:
    print(100/2)
    print(100/4)
    print(100/5)

    try:
        print(100/10)
        print(100/0)
        print(100/25)

    except EOFError:
        print(100/50)
        print(100/100)
        print(100/1)
    finally:
        print("inner finally block 1")
        print("inner finally block 2")
except EOFError:
    print(200)
    print(300)
    print(400)
finally:
    print("outer finally block 1")
    print("outer finally block 2")

