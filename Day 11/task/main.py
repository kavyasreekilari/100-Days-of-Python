import random
import art


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(deal_cards):
    if len(deal_cards) == 2 and score == 21:
        return 0

    if 11 in deal_cards and sum(deal_cards) > 21:
        deal_cards.remove(11)
        deal_cards.append(1)

    return sum(deal_cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        print("It's a draw.")
    elif computer_score == 0:
        print("User lsoes")
    elif user_score == 0:
        print("user wins🥇")
    elif user_score > 21:
        print("User loses")
    elif computer_score > 21:
        print("Computer loses")
    elif computer_score > user_score:
        print("Computer wins")
    else:
        print("You win")

# Blackjack game
def blackjack():
    print(art.logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    # draw 2 cards first
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            deal_again = input("Type 'y' to get another card, type 'n' to pass: ")
            if deal_again == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 or computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))

while input("Do you want to play game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 20)
    blackjack()




#     user_card_deck += random.sample(cards, 2)
#     computer_card_deck += random.sample(cards, 2)
#
#     # first hand of cards
#     user_hand = sum(user_card_deck)
#     print(f"Your cards: {user_card_deck}, current score: {user_hand}")
#
#     computer_hand = sum(computer_card_deck)
#     print(f"Computer's first card: {computer_card_deck[0]}")
#
#     get_another_card = True
#
#     # get another card
#     while get_another_card:
#         get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
#         if get_another_card == 'y':
#
#             new_user_card = random.sample(cards, 1)
#             user_card_deck += new_user_card
#             user_hand += new_user_card
#
#             new_computer_card = random.sample(cards, 1)
#             computer_card_deck += new_computer_card
#             computer_hand += new_computer_card
#
#         else:
#             get_another_card = False
#
#     # check blackjack
#
#
#     # decide winner
#     if computer_hand > user_hand:
#         print("Opponent went over. You win🥇")
#     elif computer_hand == user_hand:
#         print("Its a draw!")
#     else:
#         print("Computer won!")
#
#
#
#     # Print Final scores
#     print(f"Your final hand: {user_card_deck}, final score: {user_hand}")
#     print(f"Computer's final hand: {computer_card_deck}, final score: {computer_hand}")
#
#
# # start of game
# while play_game:
#     play_blackjack = input("Do you want to play game of Blackjack? Type 'y' or 'n': ")
#     if play_blackjack == 'y':
#         print("\n" * 10)
#         print(art.logo)
#         blackjack()
#     else:
#         play_game = False
#         print("GoodBye!")
