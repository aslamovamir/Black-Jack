import random
import art

# Face cards, Jack, Queen, King as 10, Ace as either 1 or 11 as the player desires
scores = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def print_status(player_scores, dealer_scores, player_total, dealer_total):

    print(f"\nYour cards: {player_scores}, with the score of: {player_total}")
    print(f"The Dealer Cards: {dealer_scores}, with the score of: {dealer_total}\n")


def hit():

    random_index = random.randint(0, len(scores) - 1)
    card = scores[random_index]

    return card

def checkAs(player_scores, total_so_far, assigned_card):

    # A's have to benefit the player and change from 11 to 1 accordingly
    # If there is an A with the initial value of 11, and the picked card
    # increases the total above 21, A has to turn into 1
    # Else if there is no A among the cards of the player, and A was picked
    # then if A with the initial value of 11 increases the total above 11, the
    # added A has to turn into 1
    benefit = False
    there_is_11 = False
    index = 0
    index_eleven = 0

    if assigned_card == 11:
        if assigned_card + total_so_far > 21:
            assigned_card = 1
            player_scores.append(assigned_card)
    else:
        for score in player_scores:
            if score == 11:
                there_is_11 = True
                index_eleven = index
            index += 1
        if (there_is_11):
            if assigned_card + total_so_far > 21:
                player_scores[index_eleven] = 1
                player_scores.append(assigned_card)
                benefit = True
    if (benefit):
        return player_scores
    else:
        return None



def status_analysis(party_scores_total):

    if party_scores_total <= 21:
        return True
    else:
        return False


def final_analysis(player_scores, dealer_scores, player_total, dealer_total):

    print(f"Your final hand: {player_scores}\nDealer's final hand: {dealer_scores}")
    if player_total <= 21 and dealer_total <= 21:
        if player_total == 21 or dealer_total == 21:
            if player_total == 21 and dealer_total == 21:
                print("Push!")
            elif player_total == 21 and dealer_total != 21:
                print("BlackJack! You win!")
            elif player_total != 21 and dealer_total == 21:
                print("BalckJack! You lose!")
        elif player_total < 21 and dealer_total < 21:
            if player_total > dealer_total:
                print("You win!")
            elif player_total < dealer_total:
                print("You lose!")
    elif player_total > 21 or dealer_total > 21:
        if player_total > 21 and dealer_total > 21:
            print("Push!")
        elif player_total > 21 and dealer_total <= 21:
            print("You lose!")
        elif player_total <= 21 and dealer_total > 21:
            print("You win!")


def blackjack():

    print(art.logo)
    player_scores = []
    dealer_scores = []
    player_total = 0
    dealer_total = 0



    # By default player is randomly assigned 2 cards
    # By default the dealer is assigned 2 cards
    indexing = 0
    for i in range(2):
        player_scores.append(scores[random.randint(0, len(scores) - 1)])
        if indexing == 1 and player_scores[indexing] == 11:
            player_scores[indexing] = 1
        player_total += player_scores[i]

    indexing = 0
    for i in range(2):
        dealer_scores.append(scores[random.randint(0, len(scores) - 1)])
        if indexing == 1 and player_scores[indexing] == 11:
            player_scores[indexing] = 1
        dealer_total += dealer_scores[i]

    # results are printed
    print_status(player_scores, dealer_scores, player_total, dealer_total)

    # the programs halts: The player is asked to choose: Hit() OR Stand() as long as
    # the total score is < 21
    dealer_progression = True
    player_progression = True
    while(player_progression):
        player_choice = input("Would you like to 'Hit' or 'Stand'?: ").lower()

        # IF the player chooses Hit():
        if player_choice == 'hit':
            picked_card = hit()
            pot_cards = checkAs(player_scores, player_total, picked_card)
            if pot_cards == None:
                player_scores.append(picked_card)
            else:
                player_scores = pot_cards
            player_total += player_scores[len(player_scores) - 1]
            print_status(player_scores, dealer_scores, player_total, dealer_total)

            # the status analysis is performed: the total has to be < 21 for the player
            # to be given the choice of Hit() or Stand() again
            player_progression = status_analysis(player_total)

            # if the player total is greater than 21, in which case the player progression is False,
            # the dealer is now randomly presented with the choice of Hit() or Stand():
            if (not player_progression):
                print("Your total score is currently exceeding 21, the dealer is presented with the choice now.")

                # the choices the dealer has are Hit() or Stand()
                # a random index will be used for the dealer between the two choices

                # this boolean will indicate whether the dealer is to be continually given
                # the choice of Hit() or Stand()
                dealer_progression = True
                while(dealer_progression):
                    dealer_choice = random.randint(0, 1)

                    # if the dealer chooses Hit():
                    # the dealer is randomly assigned 1 card:
                    if dealer_choice == 1:
                        picked_card = hit()
                        pot_cards = checkAs(dealer_scores, dealer_total, picked_card)
                        if pot_cards == None:
                            dealer_scores.append(picked_card)
                        else:
                            dealer_scores = pot_cards
                        dealer_total += dealer_scores[len(dealer_scores) - 1]

                        # results printed
                        print_status(player_scores, dealer_scores, player_total, dealer_total)

                        # status analysis is performed: the total has to be < 21 for
                        # for the dealer to be given the choice of Hit() or Stand() again
                        dealer_progression = status_analysis(dealer_total)

                        if dealer_progression == False:
                            player_progression = False

                        # if the dealer total is greater than 21, in which case the dealer progression is False,
                        # the final results are analyzed: the results are printed, winner is decided
                        if (not dealer_progression):
                            final_analysis(player_scores, dealer_scores, player_total, dealer_total)

                            # the player is asked wether to restart the game
                            # if the player chooses 'yes': the program recursively calls
                            # itself, restarting the game, else if the player chooses 'no',
                            # the program terminates: 'Goodbye' is printed
                            player_choice = input("Would you like to play Blackjack again?('yes' or 'no'): ").lower()
                            if player_choice == 'yes':
                                blackjack()
                            else:
                                print("\nGoodbye")
                                player_progression = False
                                dealer_progression = False


                    # else if the dealer chooses Stand(), final analysis is performed
                    # the player is asked whether to restart the game: if the player chooses 'yes':
                    # the program recursively loops back into the function game()
                    # else: the program terminates: 'Goodbye' is printed
                    elif dealer_choice == 0:
                        final_analysis(player_scores, dealer_scores, player_total, dealer_total)

                        player_choice = input("Would you like to play Blackjack again?('yes' or 'no'): ").lower()
                        if player_choice == 'yes':
                            blackjack()
                        else:
                            print("\nGoodbye")

                            player_progression = False
                            dealer_progression = False

        elif player_choice == 'stand':

            # the choices the dealer has are Hit() or Stand()
            # a random index will be used for the dealer between the two choices

            # this boolean will indicate whether the dealer is to be continually given
            # the choice of Hit() or Stand()
            dealer_progression = True
            while(dealer_progression):
                dealer_choice = random.randint(0, 1)

                # if the dealer chooses Hit():
                # the dealer is randomly assigned 1 card:
                if dealer_choice == 1:
                    picked_card = hit()
                    pot_cards = checkAs(dealer_scores, dealer_total, picked_card)
                    if pot_cards == None:
                        dealer_scores.append(picked_card)
                    else:
                        dealer_scores = pot_cards
                    dealer_total += dealer_scores[len(dealer_scores) - 1]

                    # results printed
                    print_status(player_scores, dealer_scores, player_total, dealer_total)

                    # status analysis is performed: the total has to be < 21 for
                    # for the dealer to be given the choice of Hit() or Stand() again
                    dealer_progression = status_analysis(dealer_total)

                    if dealer_progression == False:
                        player_progression = False

                    # if the dealer total is greater than 21, in which case the dealer progression is False,
                    # the final results are analyzed: the results are printed, winner is decided
                    if (not dealer_progression):
                        final_analysis(player_scores, dealer_scores, player_total, dealer_total)

                        # the player is asked wether to restart the game
                        # if the player chooses 'yes': the program recursively calls
                        # itself, restarting the game, else if the player chooses 'no',
                        # the program terminates: 'Goodbye' is printed
                        player_choice = input("Would you like to play Blackjack again?('yes' or 'no'): ").lower()
                        if player_choice == 'yes':
                            blackjack()
                        else:
                            print("\nGoodbye")
                            player_progression = False
                            dealer_progression = False











# main

wish_to_play = input("Do you want to play Blackjack?('yes' or 'no'): ").lower()
if wish_to_play == 'yes':
    blackjack()
else:
    print("\nGoodbye")

    
    
