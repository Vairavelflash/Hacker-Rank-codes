def swap_case(s):
    senteence =''
    for x in s:
       
        a = x.islower()
        if a == True:
            # print (x.upper())
            senteence += x.upper()
        elif a == False:
            # print (x.lower())
            senteence += x.lower()
        else:
            senteence = senteence
    # print (senteence)  
    return senteence

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# standard code
def swap_case(sentence):
    updated_s = ""
    for c in sentence:
        if c.isupper():
            updated_s += c.lower()
        elif c.islower():
            updated_s += c.upper()
        else:
            updated_s += c
    return updated_s


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)