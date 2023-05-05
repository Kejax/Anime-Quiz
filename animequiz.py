score = 0

# Question 1
print("Question 1: What is the name of the main character in Naruto?")
answer = input("Your answer: ")
if answer.lower() == "naruto":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Naruto.")

# Question 2
print("Question 2: In which anime does a character named Monkey D. Luffy appear?")
answer = input("Your answer: ")
if answer.lower() == "one piece":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is One Piece.")

# Question 3
print("Question 3: What is the name of the protagonist in Attack on Titan?")
answer = input("Your answer: ")
if answer.lower() == "eren yeager" or answer.lower() == "eren jaeger":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Eren Yeager/Jaeger.")

# Question 4
print("Question 4: In which anime do characters called Titans appear?")
answer = input("Your answer: ")
if answer.lower() == "attack on titan":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Attack on Titan.")

# Question 5
print("Question 5: What is the name of the main character in Death Note?")
answer = input("Your answer: ")
if answer.lower() == "light yagami":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Light Yagami.")

# Question 6
print("Question 6: Who is the main character in Fullmetal Alchemist?")
answer = input("Your answer: ")
if answer.lower() == "edward elric" or answer.lower() == "edward":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Edward Elric.")

# Question 7
print("Question 7: In which anime does a character named Natsu Dragneel appear?")
answer = input("Your answer: ")
if answer.lower() == "fairy tail":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Fairy Tail.")

# Question 8
print("Question 8: What is the name of the main character in Sword Art Online?")
answer = input("Your answer: ")
if answer.lower() == "kirito" or answer.lower() == "kazuto kirigaya":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Kirito/Kazuto Kirigaya.")

# Question 9
print("Question 9: In which anime does a character named Kagome Higurashi appear?")
answer = input("Your answer: ")
if answer.lower() == "inuyasha":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Inuyasha.")

# Question 10
print("Question 10: What is the name of the main character in One Punch Man?")
answer = input("Your answer: ")
if answer.lower() == "saitama":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Saitama.")

print("Your final score is", score, "out of 10.")