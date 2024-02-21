import hashlib
import getpass
import os
import pyperclip
import sys
import base64
from cryptography.fernet import Fernet, InvalidToken
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB connection
MONGODB_CONNECTION_STRING = os.getenv('mongodb_string')
client = MongoClient(MONGODB_CONNECTION_STRING)
db = client['password_manager']
password_collection = db['passwords']

# Function for hashing the Master Password.
def hash_password(password):
    sha = hashlib.sha256()
    sha.update(password.encode())
    return sha.hexdigest()

# Generating a key to encrypt the data and decrypting it.
def generate_key():
    return Fernet.generate_key()

# Encrypt the encryption key using the user's master password.
def encrypt_key(master_password, key):
    cipher = Fernet(key)
    encrypted_key = cipher.encrypt(master_password.encode())
    return encrypted_key

# Decrypt the encrypted key using the user's master password.
def decrypt_key(master_password, encrypted_key):
    cipher = Fernet(master_password.encode())
    decrypted_key = cipher.decrypt(encrypted_key)
    return decrypted_key

# Initializing the Fernet cipher with the generated key.
def initialize_cipher(key):
    return Fernet(key)

# Function to encrypt a password.
def encrypt_password(cipher, password):
    return cipher.encrypt(password.encode())

# Function to decrypt a password.
def decrypt_password(cipher, encrypted_password):
    try:
        decrypted_password = cipher.decrypt(encrypted_password).decode()
        return decrypted_password
    except InvalidToken:
        # Handle the InvalidToken exception here
        print("Invalid token provided for decryption")
        return None  # Or handle it based on your specific requirements

# Function to save the data to the MongoDB.
def register(username, master_password):
    existing_user = password_collection.find_one({'username': username})
    if existing_user:
        print("\n[-] Username already exists. Please choose a different username.")
        return

    hash_master_password = hash_password(master_password)
    key = generate_key()
    encrypted_key = encrypt_key(master_password, key)
    user_data = {'username': username, 'master_password': hash_master_password, 'encrypted_key': encrypted_key}
    password_collection.insert_one(user_data)
    print('\n[+] User registered successfully! \n')

def login(username, entered_password):
    user_data = password_collection.find_one({'username': username})
    if user_data:
        stored_password_hash = user_data.get('master_password')
        entered_password_hash = hash_password(entered_password)
        if entered_password_hash == stored_password_hash:
            encrypted_key = user_data.get('encrypted_key')
            key = decrypt_key(entered_password, encrypted_key)
            cipher = initialize_cipher(key)
            print("\n[+] Login Successful...\n")
            return cipher
        else:
            print('\n[-] Invalid Login credentials. Please use the credentials you used to register')
            sys.exit()
    else:
        print("\n[-] You have not registered. Please do that. \n")
        sys.exit()

def view_website():
    view = password_collection.find({}, {'website': 1, '_id': 0})
    if view:
        print("\nWebsite you saved...\n")
        for x in view:
            print(x['website'])
        print()
    else:
        print("\n[-] You have not saved any password!\n")

# Function to add password
def add_password(cipher, website, password):
    encrypted_password = encrypt_password(cipher, password)
    encrypted_password = base64.b64encode(encrypted_password).decode('utf-8')

    password_entry = {'website': website, 'password': encrypted_password}

    password_collection.insert_one(password_entry)

# Function to get password
def get_password(cipher, website):
    entry = password_collection.find_one({'website': website})
    if entry:
        decrypted_password = decrypt_password(cipher, base64.b64decode(entry['password']))
        return decrypted_password
    else:
        return None

while True:
    print("[1] Register")
    print("[2] Login")
    print("[3] Quit")

    choice = input("[+] Enter your choice : ")
    if choice == "1":
        username = input("[+] Enter your Username :")
        master_password = getpass.getpass("[+] Enter your master password: ")
        register(username, master_password)

    elif choice == "2":
        username = input("[+] Enter your username :")
        master_password = getpass.getpass("[+] Enter your master password: ")
        cipher = login(username, master_password)

        while True:
            print("[+] Add password")
            print("[+] Get password")
            print("[+] View saved websites")
            print("[+] Quit")

            password_choice = input("[+] Enter your choice: ")
            if password_choice == '1':
                website = input("[+] Enter Website: ")
                password = getpass.getpass("[+] Enter password: ")
                add_password(cipher, website, password)
                print("\n[+] Password added! \n")
            
            elif password_choice == "2":
                website = input("[+] Enter website: ")
                decrypted_password = get_password(cipher, website)
                if decrypted_password:
                    pyperclip.copy(decrypted_password)
                    print(f"\n[+] Password for {website}: {decrypted_password}\n[+] Password copied to clipboard.\n")
                else:
                    print("\n[+] Password not found! Did you save the password? "
                          "\n[-] Use option 3 to see the website you saved.\n")
                        
            elif password_choice == '3':
                view_website()
                        
            elif password_choice == '4':
                break
    elif choice == '3':
        break
