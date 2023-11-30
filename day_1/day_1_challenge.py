# day_1_challenge.py

def generate_day_1_message(days_left):
    return f"Do you know what's special about {days_left}?"

def generate_day_fact():
    return f"The earth will take exactly 12 months to come at this very position where she is today :P"

def generate_day_message():
    return f"But the special fact is that exactly 12 days are left for THE BIG DAY <3"

def main():
    days_left = input("What comes after 11?")

    day_1_message = generate_day_1_message(days_left)
    day_fact = generate_day_fact()
    day_message = generate_day_message()

    print(day_1_message)
    print(day_fact)
    print(day_message)

if __name__ == "__main__":
    main()
