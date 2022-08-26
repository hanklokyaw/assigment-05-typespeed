from data import sentences
from random import randint
import time
import textwrap

sentence = sentences[randint(0,8)]
formatted_txt = textwrap.wrap(sentence, width=120)
print("\n")
for line in formatted_txt:
    print(line)
print("\n")

char_counter = 0
word_count = 0
space = " "

words = sentence.split()
# for word in words:
#     for char in word:
#         print(char)
#     print(space)

game_continue = False

# Typing Speed Second Counter

# Ask to start the timer
start_btn = input("Would you like to start the type speed test? Yes/No:").lower()

# Count user input time in second
if start_btn == "yes":
    # time.sleep(60)
    start_time = time.time()
    user_input = input("Counting started:\n")
    stop_time = time.time()
    total_sec = stop_time - start_time
    print(f"Total time: {total_sec:.2f}")

    # break sentence into words
    user_words = user_input.split()

    # loop throught two list to compare words and count the correct words
    for i in range(0,len(user_words)):
        if user_words[i] == words[i]:
            word_count += 1
        elif user_words[i] == words[i+1]:
            word_count += 1

    print(f"Word count: {word_count}")
    # calculate word per minute
    WPM_ratio = total_sec/60
    WPM = word_count/WPM_ratio
    print(f"Your word per minute(WPM): {WPM}.")

            # for char in word:
            #     print(char)
            #     char_counter += 1
            # print(space)
else:
    print("OK, Goodbye!")