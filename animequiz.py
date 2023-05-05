score = 0

questions = {
    "Question 1: What is the name of the main character in Naruto?": "Naruto",
    "Question 2: In which anime does a character named Monkey D. Luffy appear?": "One Piece",
    "Question 3: What is the name of the protagonist in Attack on Titan?": ["Eren Yeager", "Eren Jaeger"],
    "Question 4: In which anime do characters called Titans appear?": "Attack on Titan",
    "Question 5: What is the name of the main character in Death Note?": "Light Yagami",
    "Question 6: Who is the main character in Fullmetal Alchemist?": ["Edward", "Edward Elric", "Elric"],
    "Question 7: In which anime does a character named Natsu Dragneel appear?": "Fairy Tail",
    "Question 8: What is the name of the main character in Sword Art Online?": ["Kirito", "Kazuto Kirigaya"],
    "Question 9: In which anime does a character named Kagome Higurashi appear?": "Inuyasha",
    "Question 10: What is the name of the main character in One Punch Man?": "Saitama",
    "Question 11: What is the name of the main character of Akame ga kill" : "Tatsumi"
}
    
for key, value in questions.items():
    answer = input(key + "\n")
    if(isinstance(value, list) and answer.lower() in [i.lower() for i in value]) or (isinstance(value, str) and answer.lower() == value.lower()):
        print("Correct")
        score += 1
    else:
        print("Incorrect. The correct answer is " + ("/".join(i for i in value) if isinstance(value, list) else value))

print("Your final score is", score, "out of 10.")
