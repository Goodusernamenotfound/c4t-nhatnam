scores = [13, 62, 25, 79, 33]
scores.sort(reverse=True)
print("High scores:")
for i, item in enumerate(scores):
    print(i+1, ". ", item, sep='')
newscore = int(input("Enter your score: "))
scores.append(newscore)
scores.sort(reverse=True)
scores.pop(5)
print("New high scores:")
for j, item in enumerate(scores):
    print(i+1, ". ", item, sep='')