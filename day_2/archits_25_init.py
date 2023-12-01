# archits_25_init.py

def generate_welcome_message():
    return f"🚀 Welcome back my baby! I know today was a bit low...but worry not!!! 🚀"

def generate_next_step_link(day_number):
    return f"Today is day {day_number} of your birthday quest and it marks one more day closer to your big surprise <3"

def main():
    day_number = int(input("Enter the day number!"))

    welcome_message = generate_welcome_message()
    next_step_link = generate_next_step_link(day_number)

    print(welcome_message)
    print(next_step_link)

if __name__ == "__main__":
    main()
