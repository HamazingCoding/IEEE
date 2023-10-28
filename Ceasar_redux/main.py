def ceasarredux(ch, shift_value, increment):
    for i in range(shift_value):
        if increment:
            if ch=='z':
                ch='a'
            else:
                ch = chr(ord(ch)+1);
        else:    
            if ch=='a':
                ch='z'
            else:
                ch = chr(ord(ch)-1);
    return ch

# Define the inputs
n = int(input())
empty_list = []
for i in range(n):
    shift_value = int(input())
    input_string = input()
    new_msg = ""
    plaintext = True

    for word in input_string.split():
        if word.lower() in " the":
            break
    else:
        plaintext = False
        
    for ch in input_string:
        if ch == ' ':
            new_msg += ch
        else:
            if plaintext:
                new_msg += ceasarredux(ch, shift_value, 0)
            else:
                new_msg += ceasarredux(ch, shift_value, 1)
    empty_list.append(new_msg)
for i in empty_list:
    print(i)