# day_2_challenge_2.py

def generate_second_word(second_word):
    if second_word.lower() == "in":
        return "I always knew your English is really goooooooood, and here we are at the second word - 'In'... Just one more riddle to solve"
    else:
        return "Ayiooo, try again! You're a software engineer, man! Run the challenge again until you get the right answer :P"

def main():
    second_word = input("I'm small and common, a preposition so neat, Two letters in length, making connections sweet. Found inside 'within' and 'begin', A tiny word with a meaning akin. What am I? ")

    day_2_message_2 = generate_second_word(second_word)
    print(day_2_message_2)

if __name__ == "__main__":
    main()
