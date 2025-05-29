def argumento(*num):
    for i in num:
        print(i)

    return type(num)

print(argumento(10, 20, 30, 40 , 50))