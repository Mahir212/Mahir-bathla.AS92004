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
