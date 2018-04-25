import binascii

def convert_to_binary(string):
    binary_string = ''.join(format(ord(x), 'b') for x in string)
    return binary_string

def convert_binary_to_ascii(binary_num):
    

def XOR_gate(num1, num2):
    if num1 == num2:
        num = 1
    else:
        num = 0
    return num

def main():
    string1 = raw_input('Enter first string: ')
    string2 = raw_input('Enter second string: ')
    binary_string1 = convert_to_binary(string1)
    binary_string2 = convert_to_binary(string2)
    convert_binary_to_ascii(binary_string1)
    convert_binary_to_ascii(binary_string2)

    '''l1 = [0,0,1,1]
    l2 = [0,1,0,1]
    l = []
    for i in range(0,4):
        l.append(XOR_gate(l1[i], l2[i]))
    print l'''

main()