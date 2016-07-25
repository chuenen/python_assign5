def fib():
      f1, f2 = 0, 1
      while True:
          yield f1
          f1, f2 = f2, f1 + f2
