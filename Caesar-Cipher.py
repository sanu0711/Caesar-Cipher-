logo = """
   _____                                   _____ _       _               
  / ____|                                 / ____(_)     | |              
 | |     __ _  ___  ___  __ _ _ __   ____ | |     _ _ __ | |__   ___ _ __ 
 | |    / _` |/ _ \/ __|/ _` | '__| |___| | |    | | '_ \| '_ \ / _ \ '__|
 | |___| (_| |  __/\__ \ (_| | |          | |____| | |_) | | | |  __/ |   
  \_____\__,_|\___||___/\__,_|_|          \_____|_| .__/|_| |_|\___|_|   
                                                  | |                    
                                                  |_|                    
"""

alphabet_character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z',' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                      'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']


def caesar(message, shift_amount, direct):
    end_text = ""
    if direct == "decode":
        shift_amount *= -1
    for char in message:
        if char in alphabet_character:
            position = alphabet_character.index(char)
            new_position = position + shift_amount
            end_text += alphabet_character[new_position]
        else:
            end_text += char
    print("---------------------------------------------------------------")
    print(f" \t\t {direct} message : {end_text}")
    print("---------------------------------------------------------------")


print(logo)

cont = True
while cont:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt : ")
    text = input("Type your message : ").lower()
    shift = int(input("Type the shift number : "))
    shift = shift % 27

    caesar(text, shift, direction)

    restart = input("Type 'yes' for again message operation else type 'no' to exit : ")
    if restart == "no":
        cont = False
        print("---------------------------------------------------------------")
        print("\t\t\tThanks ! ")
        print("---------------------------------------------------------------")