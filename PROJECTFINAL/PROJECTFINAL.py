# source: https://github.com/JoydeepMallick/Simple-games-in-python

import random
import time
print("Welcome to our project\nGAMING WITH PYTHON\n\n")
gmmd,entry=1,0
while gmmd != 0:
    gmmd = int(input("Enter 1 to play HANGMAN\nEnter 2 to play TIC-TAC-TOE\nEnter 3 to play BLACKJACK\nPlease enter your choice : "))
    print()    
    if gmmd==1:
        dictionary = ("differences are common", "hostiles inbound", "targets spotted", "call of duty",
                  "something", "whatever", "batman", "ironman", "cpt america", "thor", "hawkeye", "black widow",
                  "deadpool", "spiderman", "winter soldier", "falcon", "star lord", "loki", "doctor strange",
                  "hulk", "scarlet witch", "quicksilver", "ultron", "ten rings", "mandarin", "hydra", "avengers",
                  "tesseract", "sceptre", "power stone", "eye of agamotto", "dormamu", "ancient one", "soul stone",
                  "red skull", "reality stone", "asgard", "bifrost", "mjolnir", "storm breaker", "heimdall"
                                                                                                 "ragnorok")
        play = "play"
        # main game loop
        while play == "play":
            import getpass
            gm = input("Enter 'pvc' for single player\nEnter 'pvp' for player vs player\nPlease enter your choice : ")
            print()
            while gm != "pvc" and gm != "pvp":
                print()
                gm = input("Wrong input\ninput again : ")
            if gm == "pvc":
                key_ = dictionary[random.randint(0, len(dictionary) - 1)]
            else:
                key_ = getpass.getpass(prompt="Input word or phrase to be guessed by other player : ")
                time.sleep(1)
                print("\nYour entered words will be hidden,no worry!\n")

            key = []
            mstk = 0
            for i in key_:
                # 1 if seen 0 if not
                key.append([i, 0])
            print("the blanks represent unidentified letters")
            print("the / represent spaces")
            # game loop
            while mstk < 8:
                print("mistakes made : ", mstk)
                # drawing blanks
                for j in key:
                    if j[1] == 0 and not (j[0].isspace()):
                        print("_", end=" ")
                    elif j[1] == 0 and j[0].isspace():
                        print("/", end=" ")
                    elif j[1] == 1:
                        print(j[0], end="")
                print()
                # draw a hangman
                if mstk >= 1:
                    print("     ----------------")
                if mstk >= 2:
                    print("     |")
                    print("     |")
                    print()
                    print()
                if mstk >= 3:
                    print("    /\\")
                    print("   /  \\")
                    print("   \\  /")
                    print("    \\/")
                if mstk == 4:
                    print("     |\n     |\n     |\n     |")
                elif mstk == 5:
                    print("    /|")
                    print("   / |")
                    print("  /  |")
                    print(" /   |")
                elif mstk >= 6:
                    print("    /|\\")
                    print("   / | \\")
                    print("  /  |  \\")
                    print(" /   |   \\")
                if mstk == 7:
                    print("     /")
                    print("    /")
                    print("   /")
                    print("  /")
                x = input("Enter the guess word : ")
                print()
                # for single letter
                if len(x) == 1:
                    ctrl = 0
                    for j in key:
                        if x == j[0]:
                            ctrl = 1
                            if j[1] == 1:
                                mstk += 1
                                print("Guess repeated\n")
                                break
                            else:
                                j[1] = 1
                    if ctrl == 0:
                        mstk += 1
                        print("Wrong guess !!!\n")
                # for words
                else:
                    if x == key_:
                        print("YOU WIN\nyour score is ", 8 - mstk)
                        print()
                        break
                    else:
                        print("Wrong guess !!!\n")
                        mstk += 1
                # victory condition
                win = 0
                for n in key:
                    win += n[1]
                spc = 0
                for m in key_:
                    if m.isspace():
                        spc += 1
                if win == (len(key_) - spc):
                    print("YOU WIN\nyour score is ", 8 - mstk)
                    print()
                    break
            if mstk == 8:
                print("     -----------------")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("    /\\")
                print("   /  \\")
                print("   \\  /")
                print("    \\/")
                print("    /|\\")
                print("   / | \\")
                print("  /  |  \\")
                print(" /   |   \\")
                print("     /\\")
                print("    /  \\")
                print("   /    \\")
                print("  /      \\")
                print("YOU LOSE ")
            print()
            play = input("\nEnter 'play' to play again\nanything else to quit : ")
            print()

            if play!='play':
                print("\n\nThank you for playing HANGMAN!!!\n\n")


    elif gmmd == 2:
        board = [" ", " ", " ",
                 " ", " ", " ",
                 " ", " ", " "]
        sample = ["1", "2", "3",
                  "4", "5", "6",
                  "7", "8", "9"]


        def print_board(brd):
            print("\t\t ",brd[6], " | ", brd[7], " | ", brd[8], sep="")
            print("\t\t-----------")
            print("\t\t ",brd[3], " | ", brd[4], " | ", brd[5], sep="")
            print("\t\t-----------")
            print("\t\t ",brd[0], " | ", brd[1], " | ", brd[2], sep="")


        def p_move(brd, sym, pos):
            if 0 < pos < 10:
                if brd[pos - 1] == " ":
                    brd[pos - 1] = sym
                else:
                    print("\nPlace is already full\n")
                    pos = int(input("Enter desired position : "))
                    p_move(brd, sym, pos)
            else:
                print("\nInvalid position!!!\n")
                pos = int(input("Enter desired position : "))
                p_move(brd, sym, pos)


        def win(brd, pos, sym):
            if (pos == 0 or 1 or 2) and (brd[0] == brd[1] == brd[2] == sym):
                return True
            elif (pos == 3 or 4 or 5) and (brd[3] == brd[4] == brd[5] == sym):
                return True
            elif (pos == 6 or 7 or 8) and (brd[6] == brd[7] == brd[8] == sym):
                return True
            elif (pos == 0 or 3 or 6) and (brd[0] == brd[3] == brd[6] == sym):
                return True
            elif (pos == 1 or 4 or 7) and (brd[1] == brd[4] == brd[7] == sym):
                return True
            elif (pos == 2 or 5 or 8) and (brd[2] == brd[5] == brd[8] == sym):
                return True
            elif (pos == 0 or 4 or 8) and (brd[0] == brd[4] == brd[8] == sym):
                return True
            elif (pos == 2 or 4 or 6) and (brd[2] == brd[4] == brd[6] == sym):
                return True
            return False


        def isempty(brd, pos):
            if brd[pos] == " ":
                return True
            else:
                return False


        def full(brd):
            for i in range(9):
                if brd[i] == " ":
                    return False
            return True


        s1 = input("Enter symbol of first player i.e. O or X(CAPITAL LETTERS ONLY): ")
        while s1 != "X" and s1 != "O":
            print("Wrong input!!!")
            s1 = input("Enter symbol of first player(O/X): ")
        if s1 == "X":
            s2 = "O"
        elif s1 == "O":
            s2 = "X"
        print("\nThe positions are as follows:-\n")
        print_board(sample)
        print()
        play = ""
        while play == "":
            print_board(board)
            while True:
                ps1 = int(input("Enter desired position Player 1 : "))
                print()
                p_move(board, s1, ps1)
                print_board(board)
                print()
                if win(board, ps1 - 1, s1):
                    print("Player with ",s1, " wins.")
                    break
                if full(board):
                    print("Match is tied.")
                    break
                ps2 = int(input("Enter desired position Player 2 : "))
                print()
                p_move(board, s2, ps2)
                print_board(board)
                print()
                if win(board, ps2 - 1, s2):
                    print("Player with ",s2, " wins.")
                    break
                if full(board):
                    print("Match is tied.")
                    break
            board = [" ", " ", " ",
                     " ", " ", " ",
                     " ", " ", " "]
            play = input("\nPress enter to play again\nanything else to quit : ")
            if play!='':
                print("\n\nThank you for playing TIC-TAC-TOE!!!\n\n")


            
    elif gmmd == 3:
        print("Welcome to Blackjack")
        name = input("Enter your name : ")
        print("\nIt is player versus dealer game\n")
        time.sleep(2)
        print("Dealer : Your computer")
        print("Player : ", name)
        time.sleep(1)
        print("The basic rules are given below(please read carefully before starting):-")
        print("\n\n")
        time.sleep(3)
        print("1.The goal of blackjack is to beat the dealer's hand without going over 21.\n")
        time.sleep(2)
        print("2.Face cards are worth 10. Aces are worth 1(soft hand) or 11, whichever makes a better hand.\n")
        time.sleep(2)
        print("3.Each player starts with two cards, one of the dealer's cards is hidden until the end.\n")
        time.sleep(2)
        print("4.To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.\n")
        time.sleep(2)
        print("5.If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.\n")
        time.sleep(2)
        print("6.If you are dealt 21 from the start (Ace & 10), you got a blackjack.\n")
        time.sleep(2)
        print("7.Blackjack usually means you win 1.5 the amount of your bet. Depends on the casino.\n")
        time.sleep(2)
        print("8.Dealer will hit until his/her cards total 17 or higher.\n")
        time.sleep(2)
        print("9.Doubling is like a hit, only the bet is doubled and you only get one more card.\n")
        time.sleep(2)
        print("10.Split can be done when you have two of the same card - the pair is split into two hands.\n")
        time.sleep(2)
        print("11.Splitting also doubles the bet, because each new hand is worth the original bet.\n")
        time.sleep(2)
        print("12.You can only double/split on the first move, or first move of a hand created by a split.\n")
        time.sleep(2)
        print("13.You cannot play on two aces after they are split.\n")
        time.sleep(1)
        print("14.You can double on a hand resulting from a split, tripling or quadrupling you bet.\n")
        time.sleep(2)
        print("\nPlease note:- Split and doubling feature has not been provided\n")
        reply = 'y'
    
        deck = [("Ace of Hearts", 11), ("2 of Hearts", 2), ("3 of Hearts", 3), ("4 of Hearts", 4), ("5 of Hearts", 5),
            ("6 of Hearts", 6), ("7 of Hearts", 7), ("8 of Hearts", 8), ("9 of Hearts", 9), ("10 of Hearts", 10),
            ("King of Hearts", 10), ("Queen of Hearts", 10), ("Jack of Hearts", 10), \
            ("Ace of Diamonds", 11), ("2 of Diamonds", 2), ("3 of Diamonds", 3), ("4 of Diamonds", 4), ("5 of Diamonds", 5),
            ("6 of Diamonds", 6), ("7 of Diamonds", 7), ("8 of Diamonds", 8), ("9 of Diamonds", 9), ("10 of Diamonds", 10),
            ("King of Diamonds", 10), ("Queen of Diamonds", 10), ("Jack of Diamonds", 10), \
            ("Ace of Club", 11), ("2 of Club", 2), ("3 of Club", 3), ("4 of Club", 4), ("5 of Club", 5), ("6 of Club", 6),
            ("7 of Club", 7), ("8 of Club", 8), ("9 of Club", 9), ("10 of Club", 10), ("King of Club", 10),
            ("Queen of Club", 10), ("Jack of Club", 10), \
            ("Ace of Spades", 11), ("2 of Spades", 2), ("3 of Spades", 3), ("4 of Spades", 4), ("5 of Spades", 5),
            ("6 of Spades", 6), ("7 of Spades", 7), ("8 of Spades", 8), ("9 of Spades", 9), ("10 of Spades", 10),
            ("King of Spades", 10), ("Queen of Spades", 10), ("Jack of Spades", 10)]
        totalreturn = totalbet = 0
    
        print()
        while (reply == 'y' or reply == 'Y'):
            print("Shuffling the deck", end="")
            for i in range(10):
                print('.', end="")
                time.sleep(1)
            print()
            bet = int(input("Enter betting amount(integers): Rs. "))
            newdeck = list(deck)
            print("\nDeck shuffled sucessfully!!!\n")
            i = sp = sd = c = cash = 0
            player, dealer = [], []  # cards present with dealer and player
            while (i < 4):
                card = newdeck[random.randint(0, len(newdeck) - 1)]
                if i % 2 == 0:
                    player.append(card)
                    sp += player[len(player) - 1][1]
                else:
                    dealer.append(card)
                    sd += dealer[len(dealer) - 1][1]
                newdeck.remove(card)
                i += 1
            print("You have received the following two cards :-")
            print()
            for i in player:
                print(i[0])
                time.sleep(1)
            print()
            print("Dealer shows up a card", end="")
            for i in range(10):
                print('.', end="")
                time.sleep(1)
            print()
            print("\nDealer : I have a/an ", dealer[random.randint(0, 1)][0], "\n")
            time.sleep(1)
    
            while (sp <= 21 and c == 0):  # for player to hit or stand and not to exceed 21
                decide = input("""Press 'h' or 'H' to hit
    Press 's' or 'S' to stand
    Enter your decision : """)
                print()
                time.sleep(2)
                if decide == 'h' or decide == 'H':
                    card = newdeck[random.randint(0, len(newdeck) - 1)]
                    if sp == 21 and len(player) == 2:
                        final = input("""Do you want to hit?You already have a sum of 21.
    If you are sure to hit and turn the Ace into soft hand i.e. value becomes 1,press 'y' or 'Y' and press enter to stand.
    Please enter your decision : """)
                        if final == 'y' or final == 'Y':
                            player.append(card)
                            newdeck.remove(card)
                            print("You have received a/an ", player[len(player) - 1][0])
                            sp += player[len(player) - 1][1] - 10
                        else:
                            print("You have got a Blackjack!!!")
                            c = 1
                    else:
                        player.append(card)
                        newdeck.remove(card)
                        print("You have received a/an ", player[len(player) - 1][0])
                        sp += player[len(player) - 1][1]
    
                elif decide == 's' or decide == 'S':
                    if sp == 21 and len(player) == 2:
                        print("You have got a Blackjack!!!")
                    c = 1
            print("Dealer is busy in carefully picking up cards.Kindly have patience", end="")
            for i in range(10):
                print('.', end="")
                time.sleep(1.5)
            print("\n\n")
    
            while (sd <= 17):  # dealer has to pick up cards until his overall turns out to at least 17
                card = newdeck[random.randint(0, len(newdeck) - 1)]
                dealer.append(card)
                newdeck.remove(card)
                sd += dealer[len(dealer) - 1][1]
    
            # cases of winning of player
            if sd > 21 and sp < 21:
                print("Dealer is busted. His overall is ", sd)
                print("You win!!!")
                cash = 2 * bet
            elif sd < sp and sp <= 21:
                print("Dealer loses. His overall is ", sd)
                print("You win!!!")
                cash = 2 * bet
            # cases of lossing of player
            elif sp > 21 and sd < 21:
                print("Dealer wins. His overall is ", sd)
                print("You are busted!You lose.")
                cash = 0
            elif sd > sp and sd <= 21:
                print("Dealer wins. His overall is ", sd)
                print("You lose!")
                cash = 0
            # cases of draw of player
            elif sd == sp:
                print("Draw!")
                print("Dealer's overall is ", sd)
                cash = bet
            elif sp > 21 and sd > 21:
                print("Both lose!")
                print("Dealer's overall is ", sd)
                cash = bet
            else:
                print("error")
            time.sleep(2)
            print("Your overall is ", sp)
            print("\n\n")
            print("Your bet : Rs.", bet)
            print("Your return :Rs.", cash)
            totalreturn += cash
            totalbet += bet
            print("\n\n\n")
            time.sleep(2)
            reply = input("""Would you like to play another round ?
    Press 'y' or 'Y' to play another round
    or Press enter to exit.
    Please enter your choice : """)
            time.sleep(3)
            print()
    
        print("Name of Player : Mr./Mrs. ", name)
        print("Total money spent in bet : Rs.", totalbet)
        time.sleep(2)
        if totalreturn == 0:
            print("Sorry! You have won no money yet.Better luck next time.")
        else:
            print("total cash earned in all the rounds : Rs.", totalreturn)
        print("\n\nThank you for playing BLACKJACK!!!\n\n")
        time.sleep(3)


    gmmd=int(input("""Do you want to play another game?
If yess press any other digit of your choice except zero.
If no,press zero.
Please enter your choice : """))
    print("\n\n")

time.sleep(3)
print("\nHope you enjoyed our little piece of code!!!\n")
time.sleep(2)
print("""Created by:-
  Subhadeep Paul
  Joydeep Mallick
  Pratyush Ghosh""")
time.sleep(5)
    



