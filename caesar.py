# Input the user to the key that they want the letters to be shifted.
# Input the user the plaintext: 
# The plaintext will be shifted based on the value of key. If the first letter is 'a' it should be transformed to 'c'

    # if(key <= -):
        # print("Key must be a non-negative number or equal to 0")

# Get the number of times the letter will be shifted. 
def get_key():
    key = input("Type the key value: ")
    key = int(key)
    return key
    
# Get the plaintext.   
def get_text():
    text = input("Plaintext: ")
    text = str(text).strip()
    return text
    

def get_cipher():
    user_key = get_key()
    if user_key <= 0:
        print("Key must not be non-negative integer or equal to 0")
    
    plaintext = get_text()
    str_length = len(plaintext)
    
    cipher_text = ""
    
    # Loop thorugh each iteration of the character and covnert it to its ascii value.
    for i in range(str_length):
        character = plaintext[i]
        ascii_value = ord(character)
        
        if character.isupper():
            transform = (ascii_value - ord('A') + user_key) % 26 + ord('A')
            cipher_text += chr(transform)
        elif character.islower():
            transform = (ascii_value - ord('a') + user_key) % 26 + ord('a')
            cipher_text += chr(transform)
        else:
            cipher_text += character
        
    print(f"Ciphertext: {cipher_text}")
        
   
get_cipher()

