"""
Higher or Lower

Author: Alan
Date: September 1st 2024

This script performs the popular higher or lower game, where the user has to guess who has more followers on Instagram
"""

import random
from art import logo, vs
from game_data import data

def format_data(data_list):
    """Return a formatted text of the Instagram account."""
    name = data_list["name"]
    description = data_list["description"]
    country = data_list["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(followers_1, followers_2, answer):
    """Return True if the user guessed correctly or False if they didn't"""
    return (followers_1 > followers_2 and answer == "A") or (followers_1 < followers_2 and answer == "B")

def play_higher_lower():
    """
    This script runs the higher and lower game, where the use user has to guess correctly who has more followers

    If they guess right, they score a point and can continue playing
    """
    score = 0
    is_game_over = False

    print(logo)

    data_list_2 = random.choice(data)

    while not is_game_over:

        # We keep one of the accounts for the next round, so we can compare them with a new one
        data_list_1 = data_list_2
        data_list_2 = random.choice(data)

        #Prints the accounts and descriptions so the user gets an idea
        print(f"Compare A: {format_data(data_list=data_list_1)}")
        print(vs)
        print(f"Compare B: {format_data(data_list=data_list_2)}")

        # Let the user make a guess
        answer = input("Who has more followers? Type 'A' or 'B'\n")

        followers_1 = data_list_1["follower_count"]
        followers_2 = data_list_2["follower_count"]

        # Check if the user guessed correctly
        is_correct = check_answer(followers_1, followers_2, answer)

        # Preparing the environment for the next round
        print("\n"*20)
        print(logo)

        # If it's correct, they score a point and they can continue playing.
        # Else, they lose and final score is printed
        if is_correct:
            score += 1
            print(f"You are right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            is_game_over = True

play_higher_lower()
