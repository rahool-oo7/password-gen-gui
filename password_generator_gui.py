# password_generator_gui.py

# This script basically generate password of the required length
# Password will include alphabets(both case), numbers and special characters

import random     # Random password Generation
import time       # Generating delay
import sys        # Typing effect
import pyperclip  # Copy to clipboard

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$&!"

choice = 'y'

while(choice.lower()=='y'):
    # resets the password 
    password = ""
    try:
        password_length = int(input("\nEnter password length : "))

        # Security check
        if(password_length < 6):
            print("❌ Minimum length should be 6 for security")
            continue

        # Typing effect
        message = "🔑 Generating a secure password..."
        for letter in message:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.05)

        # Generating effect
        time.sleep(1.4)

        ## USING FOR LOOP
        '''
        for i in range(password_length):
            password+=random.choice(chars)
        '''

        ## USING CHOICES AND JOIN
        '''
        password = ''.join(random.choices(chars, k=password_length))
        '''

        ## FOR UNIQUE PASSWORD
        password = ''.join(random.sample(chars, k=password_length))

        print("\n🔒 Generated password : ", end = "")
        # Typing effect
        for psswd in password:
                sys.stdout.write(psswd)
                sys.stdout.flush()
                time.sleep(0.05)

        # Copy password to clipboard
        pyperclip.copy(password)
        print("\n📋 Password copied to clipboard!\n")

        # Ask if user wants to regenerate or not
        choice = input("🔁 Generate another? (y/any key): ")
        if(choice.lower() != 'y'):
            exit()

    except ValueError:
        print("❌ Enter a valid numeric length.")
    
