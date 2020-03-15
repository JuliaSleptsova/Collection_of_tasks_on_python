a = int(input())
b = int(input())
syma = 0
counter_cycle = 0 
for counter in range(a, b+1):
  if counter % 3 == 0:
    syma = counter + syma
    counter_cycle += 1
print(syma / counter_cycle)
