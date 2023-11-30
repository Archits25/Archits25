# archits_25_init.py

def generate_welcome_message():
    return f"🚀 Welcome to Archit's 25th Birthday Quest, Aru! Your adventure begins now. 🚀"

def generate_next_step_link(day_number):
    return f"🔗 [Click here](https://github.com/Archits25/Archits25/tree/main/day_{day_number}) to access Day {day_number} of the Archit's 25th Birthday Quest."

def main():
    day_number = int(input("Enter the day number!"))

    welcome_message = generate_welcome_message()
    next_step_link = generate_next_step_link(day_number)

    print(welcome_message)
    print(next_step_link)

if __name__ == "__main__":
    main()
