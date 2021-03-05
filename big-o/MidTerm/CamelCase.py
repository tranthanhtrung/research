str_i = input()

cout = 1
for i in str_i:
  if ord(i) >= 65 and ord(i) <= 90:
    cout += 1

print(cout)