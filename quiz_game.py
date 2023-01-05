print("Welcome to computer quiz!")

playing = input("Do you want to play (yes/no)? ").upper()

if playing == 'YES':
    print("Nice! Let's play!")
    score=0

else:
    print("Okay! Let me know when you want to play!")
    quit()


answer = input("What does CPU stand for? ").upper()
if answer == "CENTRAL PROCESSING UNIT":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    


answer = input("What does GPU stand for? ").upper()
if answer == "GRAPHICS PROCESSING UNIT":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    


answer = input("What does RAM stand for? ").upper()
if answer == "RANDOM ACCESS MEMORY":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    


answer = input("What does PSU stand for? ").upper()
if answer == "POWER SUPPLY UNIT":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + " %!")
