first = float(input())
second = float(input())
operation = str(input())
if operation == '+':
  print(first + second)
elif operation == '-':
  print(first - second)
if operation == '*':
  print(first * second)
elif operation == 'pow':
  print(first ** second)
if operation == '/' and second != 0:
  print(first / second)
elif operation == '/' and second == 0:
  print("Деление на 0!")
if operation == 'mod' and second != 0:
  print(first % second)
elif operation == 'mod' and second == 0:
  print("Деление на 0!")
if operation == 'div' and second != 0:
  print(first // second)
elif operation == 'div' and second == 0:
  print("Деление на 0!")



