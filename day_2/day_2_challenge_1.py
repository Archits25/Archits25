# day_2_challenge_1.py

def generate_first_word(first_word):
    if first_word.lower() == "linked":
        return "Veryyyy good...you got the first word correct - Linked. Just two steps to go, and you'll find your day 2 present! Go checkout the next day_2 challenge"
    else:
        return "Ayiooo, try again! You're a software engineer, man! Run the challenge again until you get the right answer :P"

def main():
    first_word = input("I'm a chain of nodes, not made of gold, Connections strong, a story unfolds. In lists and trees, I gracefully bind, A structure of data, what am I, defined? What am I? (PS. it starts with an 'L' and ends with a 'd') ")

    day_2_message_1 = generate_first_word(first_word)
    print(day_2_message_1)

if __name__ == "__main__":
    main()
