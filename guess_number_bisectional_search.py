import time

high=100
low=0
secret=50

print ("Please think of a number between 0 and 100! \n")
time.sleep(2)

print ("Is your secret number",secret,"?")
answer = input ("""Enter 'h' to indicate the guess is too high. Enter 'l to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.\n""")

while answer != 'c' :
    
    if answer == 'h':
        high = secret
        secret = (low + high) // 2
        print ( "Is your secret number",secret,"?")
        answer = input ("""Enter 'h' to indicate the guess is too high. Enter 'l to indicate the guess is too low.Enter 'c' to indicate I guessed correctly.\n""")

    elif answer == 'l':
        low = secret
        if secret == 99:
            secret = 100
            break
            
            
        secret = (low + high) // 2
        print ( "Is your secret number",secret,"?")
        answer = input ("""Enter 'h' to indicate the guess is too high. Enter 'l to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.\n""")

    
print ("Game over. Your secret number was: ",secret)
