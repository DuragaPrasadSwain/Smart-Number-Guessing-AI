# Smart Number Guessing AI

print("Think of a number between 1 and 100\n\nIf my guess number is higher then yours press -> h\nIf my guess number is lower then yours press -> l\nIf my guessed the number press -> c\n")

number_of_guess = 0
Hnum = 100
Lnum = 1
guess = 50
found = False

while True:

    print(f"Is your number {guess}?")
    ans = input("Enter your response: ")

    if ans in ['h','l','c']:
        if ans == 'h':
            Hnum = guess - 1
        elif ans == 'l':
            Lnum = guess + 1
        else:
            found = True
            break
    else:
        print("\nEnter valid response.\n\nCheck The RULE .....\nIf my guess number is higher then yours press -> h\nIf my guess number is lower then yours press -> l\nIf my guessed the number press -> c\n")
        continue
    if Lnum > Hnum:
        print("Inconsistent answers detected!")
        break
    guess = int((Hnum+Lnum) / 2)
    print(number_of_guess,guess)
    number_of_guess += 1

if found:
    print("🎉 Yay! I guessed your number!")
    print(f"Guessed in {number_of_guess} attempts")
