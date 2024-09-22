# BASED ON THE FIRST LESSON IN THE SCIENTIFIC COMPUTING WITH PYTHON COURSE ON FREECODECAMP

# ANSI Escape Sequence codes: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
class EscapeSequence:
    CLEAR_SCREEN = '\033[1J'
    CURSOR_RETURN_HOME = '\033[H'
    DEFAULT_STYLE = '\033[0m'
    UNDERLINE = '\033[4m'
    RED = '\033[31m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    CHOICE = '\033[4;35m' # Underlines mageneta

# Enumerator to help make the direction parameter more readable, rather than just using
# 1 or -1, then creating seperate functions for encryption and decryption that call the same
# function 
class CipherDirection:
    ENCRYPT = 1
    DECRYPT = -1

text = 'My balls itch!'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
custom_shift = 3

def Caesar(message, offset, direction=CipherDirection.ENCRYPT):
    final_message = ''
    for char in message.lower():
        # Pass through any character that isn't a letter
        if not char.isalpha():
            final_message += char
        else:
            # Get index and shift it, including wrap around in case the shifted index is beyond the length of alphabet
            index = alphabet.find(char)
            offset_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[offset_index]
    return final_message

def Vigenere(message, key, direction=CipherDirection.ENCRYPT):
    key_index = 0
    final_message = ''
    for char in message.lower():
        # Pass through any character that isn't a letter
        if not char.isalpha():
            final_message += char
        else:
            # Get letter in key and use index to produce offset
            key_letter = key[key_index % len(key)]
            offset = alphabet.index(key_letter)
            key_index += 1

            # Get index and shift it, including wrap around in case the shifted index is beyond the length of alphabet
            index = alphabet.find(char)
            offset_index = (index + (offset + 1) * direction) % len(alphabet)
            final_message += alphabet[offset_index]
    return final_message

def GetUserInput():
    print(EscapeSequence.CYAN)
    user_input = input()
    print(EscapeSequence.DEFAULT_STYLE)
    return user_input

# MAIN EXECUTION (string sanitization? You gotta be outta your fuckin' mind.)
cipher_direction = None

print(EscapeSequence.CLEAR_SCREEN + EscapeSequence.CURSOR_RETURN_HOME)
print('I will obscure your most ' + EscapeSequence.RED + 'clandestine' + EscapeSequence.DEFAULT_STYLE + ' thoughts from the most hollow minded of people, and reveal the most deplorable thoughts that have been otherwise hidden from your massive brain.' +
      '\n(LEGAL NOTE: If you are using this to hide secrets from smart people then I am not legally responsible for the reprehensible damage that will definitely cause you.')
print('\nAre you looking for ' + EscapeSequence.CHOICE + 'encryption(1) or decryption(2)?')
cipher_choice = int(GetUserInput())

if cipher_choice == 1:
    cipher_direction = CipherDirection.ENCRYPT
elif cipher_choice == 2:
    cipher_direction = CipherDirection.DECRYPT

print('Which cipher do you want to use?')
print(EscapeSequence.CHOICE + '1. CAESAR\n2. VIGENERE')
cipher_choice = int(GetUserInput())

if cipher_choice == 1:
    caesar_message = ''
    caesar_shift = 0

    print('Fantastic choice! (I couldn\'t give less of a shit.) And what is the value to caesar shift?')
    caesar_shift = int(GetUserInput())
    print('Now, what incredibly deplorable message is it you are inquiring about?')
    caesar_message = str(GetUserInput())

    print('Wow. That\'s... oh my god. What the hell is wrong with y- you know what, no. No, I\'m not going to judge. Here\'s the result, now please leave.')
    print('\nResult: ' + Caesar(caesar_message, caesar_shift, cipher_direction))
elif cipher_choice == 2:
    vigenere_message = ''
    vigenere_key = ''

    print('\nFantastic choice! (I couldn\'t give less of a shit.) And what is the key associated with this vigenere cipher?')
    vigenere_key = str(input())
    print('\nNow, what incredibly deplorable message is it you are inquiring about?')
    vigenere_message = str(input())

    print('Wow. That\'s... oh my god. What the hell is wrong with y- you know what, no. No, I\'m not going to judge. Here\'s the result, now please leave.')
    print('\nResult: ' + Vigenere(vigenere_message, vigenere_key, cipher_direction))

