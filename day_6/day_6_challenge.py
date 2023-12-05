# day_6_challenge.py

def generate_welcome_message():
    return f"🚀 Hi my baby, couldn't stop myself today soooo we'll go a bit earlyyyyyyyyyy 🚀"

def generate_next_step_link(day_number):
    return f"Today is day {day_number} of your birthday quest and it marks one more day closer to your big surprise <3. Do just as you were instructed to do :P"

def download_ext():
    return f"Download the zip folder form here - and follow the next steps"
  
def main():
    day_number = int(input("Enter the day number!"))

    welcome_message = generate_welcome_message()
    next_step_link = generate_next_step_link(day_number)
    down_ext = download_ext()

    print(welcome_message)
    print(next_step_link)
    print(down_ext)
    new_answer = int(input("Have you downloaded? Say 0 or 1: "))
    if new_answer == 1:
        print("Follow the following steps - ")
        print("1. Open Google Chrome")
        print("2. Go to extensions 'chrome://extensions/'")
        print("3. Toggle the Developer mode button - on the top")
        print("4. Go to 'Load Unpacked' and select the unzipped folder")
        print("5. Go to Leetcode and long with the credentials shared over email to you")
        print("6. click on companies name and try - are you able to work on the company questions?")
        print("7. is it working?????? - say yes say yessssssss I want to knowwwww")
    else:
        download_ext()

if __name__ == "__main__":
    main()
