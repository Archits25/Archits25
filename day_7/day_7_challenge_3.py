def decode_code(message):
    # Your code here
    decoded_message = ""
    for char in message:
        if char.isalpha():
            # Preserve the case (upper/lower)
            is_upper = char.isupper()
            char = char.lower()

            # Apply Caesar cipher with reverse shift
            decoded_char = chr((ord(char) - ord('a') - 3) % 26 + ord('a'))

            # Restore the case
            decoded_char = decoded_char.upper() if is_upper else decoded_char

            decoded_message += decoded_char
        else:
            decoded_message += char

    return decoded_message

def main():
    coded_message = 'Wkh dwayl rq ehvw errslqj txlfnv lv - DUFLWLQ PDJHVWKBWX'
    decoded_message = decode_code(coded_message)
    print("Decoded Message:", decoded_message)

if __name__ == "__main__":
    main()
