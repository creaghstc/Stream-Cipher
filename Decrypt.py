from Encrypt import encrypt


def decrypt(CipherText, key):
    # since this process is the same as encryption we simply use that function
    message = encrypt(CipherText, key)
    return message  # return the decoded message
