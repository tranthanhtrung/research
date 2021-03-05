n = int(input())

r = []
for _ in range(n):
  str_input = input()
  longest = 0
  stack = []

  for i in range(len(str_input)):
    if str_input[i] == '<':
      stack.append(str_input[i])
    elif len(stack) > 0:
      stack.pop()
      longest = i + 1 if len(stack) == 0 else longest
    else:
      break
  print(longest)
