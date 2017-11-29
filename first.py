number =23
running = True
current_points=0
tries_remaining=100;

while running:
    guess=int(raw_input("enter a number to guess"))
    if guess==number:
        print "Congratulations You have guessed it right "
        print "your Score is now increased to "+current_points++
        number=Math.rand(1,7000)
        tries_remaining--
        c=raw_input("do u want to continue playing /n 1--yes /n 2--no")
        if c==1:
            continue
        else:
            break;


    else if guess<number:
        print "the secret number is more then what u have guessed"
        tries_remaining--
        print tries remaining + tries_remaining


    else if guess>number:
        print "the secret number is less then what u have guessed"
        tries_remaining--
        print tries remaining + tries_remaining
