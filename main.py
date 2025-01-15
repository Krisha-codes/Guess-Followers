from art import logo
from art import vs
from game_data import data
import random
data_copy = data
def check(count_1, count_2):#To check who has more followers
    if count_1> count_2:
        return "A"
    else:
        return "B"
def generate(person_a, person_b):
    print(logo)
    print(f"Compare A: {person_a['name']},{person_a['description']},{person_a['country']}: ")
    print(vs)
    print(f"Compare B: {person_b['name']},{person_b['description']},{person_b['country']}: ")
    choice = input("Who has more followers? Type 'A' or 'B'")
    higher_followers = check(person_a['follower_count'], person_b['follower_count'])
    if choice == higher_followers:
        return 1
    else:
        return 0

should_continue = True
score = 0
a = random.choice(list(data_copy))
while should_continue:
    b = random.choice(list(data_copy))
    if a == b:
        b= random.choice(list(data_copy))
    answer = generate(a,b)
    if answer == 1:
        score+= 1
        print(f"Your right. Your score: {score}")
        a=b
        print("\n" * 20)
    else:
        print(f"So close but thats wrong!. Final score {score}.")
        should_continue = False
