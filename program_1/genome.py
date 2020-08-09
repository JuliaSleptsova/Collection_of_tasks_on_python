genome = input()
genome = genome.lower()
counter = 0
counter_cycle = 0
part = 0
for nucl in genome:
   
  if nucl == 'g' or nucl == 'c':
      counter +=1
  counter_cycle +=1
  part = counter/counter_cycle * 100
print(part)
