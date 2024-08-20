import game_data
import art
import random
print(art.logo)

def pick_options():
    option_a = random.choice(game_data.data)
    option_b = random.choice(game_data.data)
    print(f"Compare A: {option_a['name']}, {option_a['description']}, from {option_a['country']}")
    print(art.vs)
    print(f"Compare B: {option_b['name']}, {option_b['description']}, from {option_b['country']}")
    follower_counts = [option_a['follower_count'], option_b['follower_count']]
    return follower_counts

def has_max_followers(follower_counts, user_choice):
    max_followers = max(follower_counts)
    if user_choice == 'A':
        user_followers = follower_counts[0]
    else:
        user_followers = follower_counts[1]

    if max_followers == user_followers:
        return True
    else:
        return False


def game():
    game_over = False
    user_score = 0
    while not game_over:
        follower_counts = pick_options()
        user_choice = input("Who has more followers? Type 'A' or 'B': ")
        user_is_right = has_max_followers(follower_counts, user_choice)
        if user_is_right:
            user_score += 1
            print("\n" * 20)
            print(art.logo)
            print("You're right! Current score: ")
        else:
            print(f"Sorry, that's wrong. Final score: {user_score}")
            game_over = True


game()