import random
number =23
running = True
current_points=0
tries_remaining=100;
c=1
while running & (c==1):
    guess=int(raw_input("enter a number to guess"))
    if guess==number:
        print "Congratulations You have guessed it right "
        current_points=current_points+1;
        print "Your Score is now increased to ->", current_points
        number=random.randint(1,100)
        c=raw_input("do u want to continue playing \n 1--yes /n 2--no")
        if c==2:
            break;



    elif guess<number:
        print "the secret number is more then what u have guessed"
        tries_remaining=tries_remaining-1
        print "tries remaining -> ", tries_remaining


    elif guess>number:
        print "the secret number is less then what u have guessed"
        tries_remaining=tries_remaining-1
        print "tries remaining ->", tries_remaining
