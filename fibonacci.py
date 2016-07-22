def fib():
    f1, f2 = 0, 1
    while True:
        yield f1
         f1, f2 = f1, f1+f2

# 命名使解釋更容易
# 符號間格
# while True replace while 1
