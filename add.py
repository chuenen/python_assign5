def add (n):
     num = sorted(n.replace('"','').split(','))
     array = []
     for s in range(len(num)):
         count = 0
         for w in range (len(num[s])):
             value = ord(num[s][w]) - 64
             count += value
         array.append(count * (s+1))
     return sum(array)
