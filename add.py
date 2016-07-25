with open('abc.txt') as f:
     num = f.read().replace('"','').split(',')
     num = sorted(num)

def add ():
     array = []
     n = 0
     for s in range(len(num)):
         for w in range (len(num[s])):
             value = ord(num[s][w])-64
             value += value
         array.append(value * (s+1))
     for i in range (len(array)):
          n += array[i]
      print n

