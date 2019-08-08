import random
x = str(input("Enter word: "))
a = list(x)
random.shuffle(a)
y = ''.join(a)
print("Jumbled word:", y)