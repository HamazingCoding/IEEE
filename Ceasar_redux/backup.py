#Firstly we must define a function that performs caeser cipher
def ceasarredux(shift_value, text, encryption=True):
    final_message = ""
    for char in text:
        if char.isalpha():
            if encryption:
                if char.isupper():
                    final_message += chr((ord(char) - ord('A') + shift_value) % 26 + ord('A'))
                else:
                    final_message += chr((ord(char) - ord('a') + shift_value) % 26 + ord('a'))
            else:  # Decryption
                if char.isupper():
                    final_message += chr((ord(char) - ord('A') - shift_value) % 26 + ord('A'))
                else:
                    final_message += chr((ord(char) - ord('a') - shift_value) % 26 + ord('a'))
        else:
            final_message += char
    return final_message


# Define the inputs
n = 2
instances = [
    (19, "we accept the ieeextreme challenge"),
    (19, "qbspbz jhlzhy olsk aol vmmpjl vm wvuapmle theptbz wypvy av iljvtpun kpjahavy")
]

for i in range(n):
    shift_value, text = instances[i]

    if "the" in text:
        # Encrypt the message
        ciphertext = ceasarredux(shift_value, text, True)
        print(ciphertext)
    else:
        # Decrypt the message
        plaintext = ceasarredux(shift_value, text, False)
        print(plaintext)