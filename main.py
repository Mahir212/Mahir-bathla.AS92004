LIST_QUESTIONS = [
    'Who directed the movie Savage?',
    'Did Peter Jackson direct THE LORD OF THE RINGS?',
    'What year was Ka Whawhai Tonu released?',
    'Which New Zealand filmmaker directed Thor: Ragnarok and What We Do in the Shadows?',
    'Is The Rule of the Jenny an action movie?',
    'Which New Zealand actress won an Academy Award for her role in The Piano (1993)?',
    'Which actor, famous for his roles in Deadpool and The Proposal, was born in New Zealand?',
    'Which of the following New Zealand actors starred in the Lord of the Rings trilogy as Aragorn?'
]

LIST_ANSWERS = [
    'sam kelly',
    'true',
    '2024',
    'taika waititi',
    'false',
    'anna paquin',
    'russell crowe',
    'viggo mortensen'
]

def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please choose from:", ', '.join(valid_options))

play_again = True

while play_again:
    name = input("What is your name? ")
    print("Ok " + name + ", let's start this game!\n")

    print("Here are some questions!")
    score = 0

    # Q1
    print(LIST_QUESTIONS[0])
    q1_options = ['rob savage', 'jake ryan', 'john tui', 'sam kelly']
    answer1 = get_valid_input("\n" + "\n".join(q1_options) + "\nANSWER: ", q1_options)
    if answer1 == LIST_ANSWERS[0]:
        print("That's correct!")
        score += 1
    else:
        print("That's incorrect. The correct answer is Sam Kelly.")

    # Q2
    print(LIST_QUESTIONS[1])
    answer2 = get_valid_input("\nTRUE\nFALSE\nANSWER: ", ['true', 'false'])
    if answer2 == LIST_ANSWERS[1]:
        print("That's correct!")
        score += 1
    else:
        print("That's incorrect! The correct answer is TRUE.")

    # Q3
    print(LIST_QUESTIONS[2])
    q3_options = ['2023', '2020', '2019', '2024']
    answer3 = get_valid_input("\n" + "\n".join(q3_options) + "\nANSWER: ", q3_options)
    if answer3 == LIST_ANSWERS[2]:
        print("That's correct!")
        score += 1
    else:
        print("That's incorrect. The correct answer is 2024.")

    # Q4
    print(LIST_QUESTIONS[3])
    q4_options = ['peter jackson', 'taika waititi', 'james cameron', 'guillermo del toro']
    answer4 = get_valid_input("\n" + "\n".join(q4_options) + "\nANSWER: ", q4_options)
    if answer4 == LIST_ANSWERS[3]:
        print("That's correct!")
        score += 1
    else:
        print("That's incorrect. The correct answer is Taika Waititi!")

    # Q5
    print(LIST_QUESTIONS[4])
    answer5 = get_valid_input("\nTRUE\nFALSE\nANSWER: ", ['true', 'false'])
    if answer5 == LIST_ANSWERS[4]:
        print("That's correct!")
        score += 1
    else:
        print("That's incorrect. The correct answer is FALSE — it's a horror movie.")

    # Q6
    print(LIST_QUESTIONS[5])
    q6_options = ['melanie lynskey', 'anna paquin', 'lucy lawless', 'kate winslet']
    answer6 = get_valid_input("\n" + "\n".join(q6_options) + "\nANSWER: ", q6_options)
    if answer6 == LIST_ANSWERS[5]:
        print("That's correct!")
        score += 1
    else:
        print("That's incorrect. The correct answer is Anna Paquin!")

    # Q7
    print(LIST_QUESTIONS[6])
    q7_options = ['chris hemsworth', 'ryan reynolds', 'russell crowe', 'hugh jackman']
    answer7 = get_valid_input("\n" + "\n".join(q7_options) + "\nANSWER: ", q7_options)
    if answer7 == LIST_ANSWERS[6]:
        print("That's correct!")
        score += 1
    else:
        print("That's incorrect. The correct answer is Russell Crowe.")

    # Q8
    print(LIST_QUESTIONS[7])
    q8_options = ['sam neill', 'martin freeman', 'karl urban', 'viggo mortensen']
    answer8 = get_valid_input("\n" + "\n".join(q8_options) + "\nANSWER: ", q8_options)
    if answer8 == LIST_ANSWERS[7]:
        print("That's correct! Good job!")
        score += 1
    else:
        print("That's incorrect. The correct answer is Viggo Mortensen! You're doing great — keep it up!")

    print("\nYou got " + str(score) + " questions correct.")
    print("You scored " + str((score / 8) * 100) + "%")

    print("Thanks for playing this quiz!")
    print("Made by Mahir Bathla")

    # Ask to play again
    play = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play != 'yes':
        play_again = False
print("hello there!,wanna play a quiz game about New Zealand actors? ")
answer1 = input().lower()

if answer1 != 'yes':
    quit()

print("so, here are some rules for this quiz")

print("1. in multi choice don't put a,b,c,d, just only the names and don't put space before and after the answer! you can put space in the answers who have first and last name like sam kelly!")

print("Thanks, and good luck :)")
    
name = input ("what is your name?")
print("ok " +name+",let's start this game ")
 
print("Here are some questios!")
score = 0

answer1 = input("Who directed the movie Savage? \n a. Rob Savage \n b. Jake Ryan \n c. John Tui \n d. Sam Kelly \n ANSWER:").lower()
if answer1== 'sam kelly':
    print("That's correct!")
    score += 1
    
    

else:
    print("That's incorrect the correct answer is sam kelly")
    

    
answer2 = input("Did Peter Jackson directed THE LORD OF THE RINGS? \n 1. TRUE \n 2. FALSE \n ANSWER:").lower()
if answer2== 'true':
    print("That's correct!")
    score += 1
    
    
else:
    print("That's incorrect!, the correct answer is true")
    

    

    
answer3  = input("What year did Ka Whawhai Tonua released? \n a. 2023 \n b. 2020 \n c. 2019 \n d. 2024 \n ANSWER:")
if answer3 == '2024':
    print("That's correct!")
    score += 1
    
    
else:
    print("That's incorrect, the correct answer is 2024")
    


answer4 = input("Which New Zealand filmmaker directed Thor: Ragnarok and What We Do in the Shadows? \n a. Peter Jackson \n b. Taika Waititi \n c.James Cameron \n d.Guillermo del Toro \n ANSWER:").lower()
if answer4 == 'taika waititi':
    print(" That's correct!")
    score += 1
    
    
    
else:
    print("That's incorrect, the correct answer is taika waititi!")


    
answer5 = input("Is the rule of the jenny movie action? \n TRUE \n FALSE \n ANSWER:").lower()
if answer5 == 'false':
    print("That's correct")
    score += 1
    
    
    
else:
    print("That's incorrect, the correct answer is false,its an horror movie")
    


answer6 = input("Which New Zealand actress won an Academy Award for her role in The Piano (1993)? \n a. Melanie Lynskey \n b. Anna Paquin \n c. Lucy Lawless \n d. Kate Winslet \n ANSWER:").lower()
if answer6 == 'anna paquin':
    print("That's correct!")
    score += 1
    
    

else:
    print("That's incorrect, The correct answer is anna paquin!")
    

    
answer7 = input("Which actor, famous for his roles in Deadpool and The Proposal, was born in New Zealand? \n a. Chris Hemsworth \n b. Ryan Reynolds \n c. Russell Crowe \n d. Hugh Jackman \n ANSWER: ").lower()
if answer7 == 'russell crowe':
    print("That's correct")
    score += 1
    
    
else:
    print(" That's incorrect, The correct answer is russell crowe")


 
answer8 = input("Which of the following New Zealand actors starred in the Lord of the Rings trilogy as Aragorn? \n a. Sam Neill \n b. Martin Freeman \n c. Karl Urban \n d. Viggo Mortensen \n ANSWER:").lower()
if answer8 == 'viggo mortensen':
     print("That's correct, good job!")
     score += 1
     
     
else:
    print("That's incorrect the correct answer is viggo mortensen! by the way you are doing great job keep it up!")


print("you got" + str(score)  + "questions correct")
print ("you got" + str(score/4 *100)  + "%")

print("thank's for playing this quiz")
print("Made by Mahir Bathla")
