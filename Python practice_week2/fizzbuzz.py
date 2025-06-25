for i in range(1, 101):
    print(i)
    if i % 3 == 0:       # divisible only by 3
        print("Fizz")
    elif i % 5 == 0:       # divisible only by 5
        print("Buzz")
    else:                  # all other numbers
        print(i)