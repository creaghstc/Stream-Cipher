from Encrypt import *
from Decrypt import *
from LFSR import *

def main(message):
	key = LFSR("011001101", (8,6,5,4), len(message))
	print(encrypt(message, key))
	print(decrypt(encrypt(message, key), key))


main("11001")
input("Press any key to close")