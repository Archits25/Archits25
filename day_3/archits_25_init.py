# archits_25_init.py

def generate_welcome_message():
    return f"🚀 Welcome back my baby! And the quest goes on just like our happy life - we know we have an happy ending but let's live this journey very happily too!!! 🚀"

def generate_next_step_link(day_number):
    return f"Today is day {day_number} of your birthday quest and it marks one more day closer to your big surprise <3. You know the drill - run the day_3 file :P"

def main():
    day_number = int(input("Enter the day number!"))

    welcome_message = generate_welcome_message()
    next_step_link = generate_next_step_link(day_number)

    print(welcome_message)
    print(next_step_link)

if __name__ == "__main__":
    main()
