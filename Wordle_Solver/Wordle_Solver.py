import os

guess = ""
feedback = ""
guess_list = []

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

try:
  with open("answers.txt", "r") as file:
    for line in file:
      words = line.strip().split(",")
      guess_list.extend(words)
except FileNotFoundError:
  print("File not found")

for guesses in range(6):
    guess = input("\nEnter guess: ")
    if len(guess.lower()) != 5:
        print("Invalid input")
        continue
    else:
        feedback = input("\nEnter feedback (g, y, w): ").lower()
        if len(feedback) != 5:
            print("Invalid input")
            continue
        elif feedback.count("g") + feedback.count("y") + feedback.count("w") != 5:
            print("Invalid input")
            continue
        else:
            if feedback == "ggggg":
                print("You win!")
                break

    temp_tuple = tuple(guess_list)

    for word in temp_tuple:
        for i in range(5):
            if feedback[i] == "w" and guess[i] in word and guess.count(guess[i]) == 1:
                guess_list.remove(word)
                break
            elif feedback[i] == "g" and guess[i] != word[i]:
                guess_list.remove(word)
                break
            elif feedback[i] == "y" and guess[i] not in word:
                guess_list.remove(word)
                break
            elif feedback[i] == "y" and guess[i] == word[i]:
                guess_list.remove(word)
                break

    counter = 0
    for i, word in enumerate(guess_list):  # Use enumerate for index access
        print(word, end=", " if i < len(guess_list) - 1 else "")  # Conditional comma
        counter += 1
        if counter == 8:
            counter = 0
    print("\n")