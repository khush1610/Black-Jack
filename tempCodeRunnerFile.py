import random

us=input("Do you want to play BlackJack? (y/n) ")

cards = [11, 2, 3, 4, 5 , 6, 7, 8, 9, 10, 10, 10, 10]

ourCards=[]
computerCards=[]
continueGame=True

def deal_cards():
    return random.choice(cards)

while continueGame:
    if us.lower() == "y":
        print("Your cards are: ")
        for i in range (2):
            dealt=deal_cards()
            ourCards.append(dealt)
        for cards in ourCards:
            print(cards)
        

        comp=deal_cards()
        computerCards.append(comp)
        print(f"Computer's first card is: {comp}")

        again=input("Do you want to hit? (y/n) ")
        if again.lower() == "y":
            newest=deal_cards()
            ourCards.append(newest)
        print(f"Your new card is: {newest}")
    
        ourTotal=0
        for cards in ourCards:
            ourTotal+=cards
        if ourTotal<17:
            newest=deal_cards()
            ourCards.append(newest)
        print(f"Your cards are: {ourCards} and the total is {ourTotal}")

        compTotal=0
        for cards in computerCards:
            compTotal+=cards
        if compTotal < 17:
            newest=deal_cards()
            computerCards.append(newest)
        print(f"Computer's cards are: {computerCards} and the total is {compTotal}")

        if(ourTotal > 21):
            print("You lose")
        elif(compTotal > 21):
            print("You win")
        elif(ourTotal > compTotal):
            print("You win")
        elif(ourTotal < compTotal):
            print("You lose")
        else:
            print("Draw")

        gameAgain=input("Do you want to play again? (y/n) ")
        if gameAgain == "y":
            continueGame=True
        else:
            continueGame=False

    

