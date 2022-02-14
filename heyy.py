

import os

phone_number = 

def send_message(phoneNumber, message):
    # sends given message to given phone number
    os.system('osascript sendtext.scpt {} "{}"' .format(phoneNumber, message))

if __name__ == '__main__':
    send_message(phone_number, 'Goodmorning champ. Have a lovely day ahead')    