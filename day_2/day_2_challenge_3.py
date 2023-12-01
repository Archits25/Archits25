# day_2_challenge_3.py

def generate_third_word(third_word):
    if third_word.lower() == "premium":
        return "Yayyyyyy...just a change of plans - there's one more thing left now - can you concatenate all the three words?"
    else:
        return "Ayiooo, try again! You're a software engineer, man! Run the challenge again until you get the right answer :P"

def generate_day_2_message(final_word):
    return f"yayyyyyy....here's your second present - here's a two month Linkedin premium for you that mostly I will be using to send your applications to diff people over linkedIn or you can also use it :P"
    
def main():
    third_word = input("I'm not just standard, I stand above the rest, An elevated status, considered the best. Exclusive perks, a step beyond, In a world of value, my name is fond. What am I? (PS. it starts with a 'P' and ends with a 'm' and rhymes with Opium :P)")

    day_2_message_3 = generate_third_word(third_word)
    print(day_2_message_3)
    
    final_word = input("press Y when done")
    day_2_message = generate_day_2_message(final_word)
    print(day_2_message)

if __name__ == "__main__":
    main()
