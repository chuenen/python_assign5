def add ():
     with open('abc.txt') as f:
         num = sorted(f.read().replace('"','').split(','))
     array = []
     for s in range(len(num)):
         for w in range (len(num[s])):
             value = ord(num[s][w]) - 64
             value += values
         array.append(value * (s+1))
     return sum(array)
