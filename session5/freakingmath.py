import random
def eval(x,op,y,err):
    if op == 0:
        return x + y + err
    else:
        return x - y + err

print("Welcome to the game! Equations will appear in the terminal. Type Y or N (not case-sensitive) if the equations are correct are incorrect, respectively.")
score = 0
exitcond = 0
while True:
    x = random.randrange(0,30)
    y = random.randrange(0,30)
    op = random.randrange(0,3)
    err = random.randrange(-1,1)
    correct=eval(x,op,y,err)
    if exitcond == 1:
        break
    else:
        while True:
            if op == 0:
                print(x, "+", y, "=", correct, sep='')
            else:
                print(x, "-", y, "=", correct, sep='')
            answer = str(input("Correct or incorrect? "))
            print(x,op,y,err,correct,answer)
            if((answer == 'y' or answer == 'Y') and err == 0):
                print("Correct!")
                score = score + 1
                break
            elif((answer == 'n' or answer == 'N') and err != 0):
                print("Correct!")
                score = score + 1
                break
            elif((answer == 'y' or answer == 'Y') and err != 0):
                print("Score: ", score)
                exitcond = exitcond + 1
                break
            elif((answer == 'n' or answer == 'N') and err == 0):
                print("Score:", score)
                exitcond = exitcond + 1
                break
            else:
                print("Invalid input, please try again")