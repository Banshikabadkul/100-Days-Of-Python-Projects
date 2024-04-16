alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(plain_text, shift_amount,list_alpha,cipher_direction):
  cipher_text = ""
  if cipher_direction == "decode":
    shift_amount *=-1
  for letter in plain_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = int(position + shift_amount)
      cipher_text += alphabet[new_position]
    else:
      cipher_text += letter
    
  print(f"The {cipher_direction}d text is {cipher_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
flag = "yes"
while flag == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
  #Hint: Think about how you can use the modulus (%).
  shift = shift % 26

  caesar(plain_text=text, shift_amount=shift,list_alpha = alphabet, cipher_direction = direction)
  flag = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
print("Good Bye")

# def encrypt(plain_text, shift_amount,list_alpha):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = int(position + shift_amount)
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")

# #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(cipher_text, shift_amount,list_alpha):
#   #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#   #e.g. 
#   #cipher_text = "mjqqt"
#   #shift = 5
#   #plain_text = "hello"
#   #print output: "The decoded text is hello"
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = int(position - shift_amount)
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift,list_alpha = alphabet)
# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift,list_alpha = alphabet)

