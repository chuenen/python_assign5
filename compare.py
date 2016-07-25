with open ('file.txt', 'r') as f:
     num = f.read().split('\n')
     num = map(int, num)

def compare():
     Max = num[0]
     for i in range (len(num)):
         if num[i] > Max:
             Max = num[i]
     print Max
     num.remove(Max)

for _ in range (3):
     compare()

