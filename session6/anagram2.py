import random
words = ["lime", "lemon", "word", "singular", "cake", "agressive"]
word = random.choice(words)
newword = list(word)
random.shuffle(newword)
a = ''.join(newword)
b = ''.join(word)
print(a)
answer = str(input("What word is this? "))
if answer == b:
    print("Correct!")
else:
    print("Incorrect answer, please try again")
