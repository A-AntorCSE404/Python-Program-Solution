import random

choices  = ['rock', 'paper', 'scissors']
beats    = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
score    = {'You': 0, 'CPU': 0}

print("=== ROCK · PAPER · SCISSORS — BEST OF 3 ===\n")

for rnd in range(1, 4):
    print(f"--- Round {rnd} ---")
    player = input("Your move (rock/paper/scissors): ").strip().lower()

    if player not in choices:
        print("Invalid choice! Round forfeited.\n")
        score['CPU'] += 1
        continue

    cpu = random.choice(choices)
    print(f"CPU chose: {cpu}")

    if player == cpu:
        print("==> Tie!\n")
    elif beats[player] == cpu:
        print("==> You win this round!\n")
        score['You'] += 1
    else:
        print("==> CPU wins this round!\n")
        score['CPU'] += 1

print(f"=== FINAL: You {score['You']} — CPU {score['CPU']} ===")
if score['You'] > score['CPU']:
    print("==> YOU WIN THE MATCH!")
elif score['CPU'] > score['You']:
    print("==> CPU WINS THE MATCH!")
else:
    print("==> IT'S A DRAW!")
