import re

def add (n):
     pattern = '[A-Z]+'
     num = sorted(re.findall(pattern, n))
     array = []
     for s in range(len(num)):
         count = 0
         for w in range (len(num[s])):
             value = ord(num[s][w]) - 64
             count += value
         array.append(count * (s+1))
     return sum(array)
