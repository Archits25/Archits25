# archits_25_init.py

def generate_welcome_message():
    return f"🚀 Hi my baby, hope you are not really tired from all these quests.. we have 9 more to goooooo 🚀"

def generate_next_step_link(day_number):
    return f"Today is day {day_number} of your birthday quest and it marks one more day closer to your big surprise <3. Do just as you were isntructed to do in your previous day quest :3"

def main():
    day_number = int(input("Enter the day number!"))

    welcome_message = generate_welcome_message()
    next_step_link = generate_next_step_link(day_number)

    print(welcome_message)
    print(next_step_link)

if __name__ == "__main__":
    main()
