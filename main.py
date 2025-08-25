from ascii_art import INTRO
from caesar_cipher import caesar_cipher

def main():
    print(f"{INTRO}\n")

    while True:
        mode = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower()
        if mode not in ["encode", "decode"]:
            print("Invalid choice. Please enter 'encode' or 'decode'.")
            continue

        text = input("\nEnter your message: ")
        try:
            shift = int(input("\nEnter the shift number: "))
        except ValueError:
            print("Please enter a valid number for shift.")
            continue

        result = caesar_cipher(text, shift, mode)
        print(f"\nResult: {result}")

        restart = input("\nDo you want to go again? (Yes/No): ").lower()
        if restart != "yes":
            print("\nYour secret is safe with me. Until we meet again!")
            break


if __name__ == "__main__":
    main()
