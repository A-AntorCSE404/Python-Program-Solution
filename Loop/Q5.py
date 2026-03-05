low, high = 1, 10000
attempts = 0

print("Think of a number between 1 and 10,000. I'll guess it!")

while low <= high:
    guess = (low + high) // 2
    attempts += 1
    feedback = input(f"Attempt {attempts}: Is it {guess}? [h/l/c]: ").strip().lower()

    if feedback == 'c':
        print(f"\n==> Your number was {guess}!")
        print(f"==> Cracked in {attempts} attempt(s).")
        break
    elif feedback == 'h':
        low = guess + 1
    elif feedback == 'l':
        high = guess - 1
    else:
        print("Invalid input. Use h, l, or c.")
else:
    print("Something went wrong — did you change the number?")
