import pickle
import random



def openEncryptedMessage(filename="EncryptedMessage.txt"):
    """Loads the encrypted text file and returns its contents"""
    infile = open(filename)
    contents = infile.read()
    infile.close()
    return contents


def buildCipher() -> dict:
    cypher = {}
    storage = []

    # upper case  --> chr(x-32)   
    # lowecase -->  (97,122)

    # Iterate through the alphabet and create key value pairs ...
    # check if the letter has been used in the random output generator
    # append to storage & create key for dict if completed check
    for x in range(97 , 123 , 1):
        value = chr(random.randint(97,122))
        while value in storage:
            value = chr(random.randint(97,122))
        storage.append(value)
        cypher[chr(x)] =  value
    
    # GENERATE CYPHER KEY FOR DECRYPTION
    with open("passkey.txt" , "w") as file:
        file.write(str(cypher))

    return cypher


def encryptMessage(text: str, cipher: dict):
    output = ""
    for char in text:
        if char.lower() in cipher:
            encrypt = cipher[char.lower()]
        else:
            encrypt = char
        output += encrypt

    return output


def loadCipher(fileName: str):
    tool = pickle.load(open(fileName, "rb"))
    return tool

    






def decrypt(text: str, cipher: dict):
    # reverse cipher dictionary
    dec = {}
    for key,value in cipher.items():
        dec[value] = key

    # use decryption dictionary to build output
    output = ""
    for x in range(0,len(text), 1):
        char = text[x]
        if char.lower() in dec:
            output += dec[char.lower()]
        else:
            output += char

    return output





def main():
    """ Test Area
        Remove or add comments for functions to test
    """
    print("TESTING PART 1")
    cipher = buildCipher()
    print(cipher)  # displays your cypher


    message = "The Quick Brown Fox, Jumps Over the lazy Dog"
    encryptedMessage = encryptMessage(message, cipher)
    print(encryptedMessage)

    # Part 2
    print("\nTesting Part 2")
    decryptedMessage = decrypt(encryptedMessage, cipher)
    print(decryptedMessage)


    new_cipher = loadCipher("cipher.dat")
    print(decrypt(openEncryptedMessage(), new_cipher))


if __name__ == '__main__':
    main()