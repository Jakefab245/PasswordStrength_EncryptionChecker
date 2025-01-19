#Import statement that is used to import Fernet from the Cryptography package in the fernet library
from cryptography.fernet import Fernet
import string
#import re
#Asks the User for their Password
password=input("Enter the Password to be Encrypted: ")
#Generates the key using generate_key() method and stores result in key
key=Fernet.generate_key()
#Sets the value of the key equal to the variable f
f=Fernet(key)
#Used to encrypt the user provided password //.encode() is used to change data from string to bytes
encrypted_passwd=f.encrypt(password.encode())
#Printing the Encrypted Password
print("Encrypted Password is: ",encrypted_passwd)
#decrypt method used to decrypt the encrypted_passwd into original value
#def decrypt_password(passwd):
    #decrypted_passwd=f.decrypt(passwd)
#Prints out the value of the decrypted password
    #print("Decrypted Password is: ",decrypted_passwd)
#Function calling decrypt_password with encrypted password
#decrypt_password(encrypted_passwd) #Password Strength Checker
#Determined using NIST Standards for Secure and Strong Passwords
length_of_passwd=len(password)
passwd_strength_score=0
#Conditional used to check if length of password exceeds or is equal to NIST recommendation
if length_of_passwd>=16:
    passwd_strength_score+=1
else:
    print("Password needs to be at least 16 characters long to be considered a secure password")
#Complexity checking
lower_case=any([1 if c in string.ascii_lowercase else 0 for c in password]) #Returns true if password contains a lowercase letter and false if no lowercase letter
upper_case=any([1 if c in string.ascii_uppercase else 0 for c in password]) #Returns true if password contains an uppercase letter and false if no uppercase letter
special_chars=any([1 if c in string.punctuation else 0 for c in password]) #Returns True if password contains a character such as ! and # returns False if not
digits=any([1 if c in string.digits else 0 for c in password]) #Returns true if password contains a digit from 0-9 and false if no digit is contained
#Creating an array of all types of characters
characters=[lower_case,upper_case,special_chars,digits]
#If password contains a combination of all of these then add strength score +1
if lower_case and upper_case and special_chars and digits:
    passwd_strength_score+=1
#Simple start of a Password Strength Checker
print("Password Strength is: ",passwd_strength_score, "out of 2")