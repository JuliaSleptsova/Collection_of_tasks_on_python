a = int(input())
b = int(input())
c = int(input())
d = int(input())
for counter in range(c, d+1):
  print('\t',counter, end=' ')
print(end='\n')
for counter_main in range(a, b+1):
  print(counter_main, end='\t') 
  for counter in range(c, d+1):
    value = counter_main * counter
    print(value, end='\t')
  print( end='\n')
