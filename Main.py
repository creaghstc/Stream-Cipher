from Encrypt import *
from Decrypt import *
from LFSR import *
from Converter import *

def main(message):
	key = LFSR("011001101", (8,6,5,4), len(message))
	print("Encrypted Binary:",encrypt(message, key))
	print("Decrypted Binary:",decrypt(encrypt(message, key), key))
	print("Origional Message:",fromBits(decrypt(encrypt(message, key), key)))


message = input("Enter your message: ")
BinMessage = toBits(message)
main(BinMessage)
input("Press any key to close")
