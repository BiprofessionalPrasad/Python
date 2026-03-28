if __name__ == '__main__':
    s = input()
    flag = 0
    for i in range(0, len(s)):
        if (s[i].isalnum() == True):
            flag = 1
            break
    if flag == 1:
        print ("True")
    else:
        print ("False")
    flag = 0
    for i in range(0, len(s)):
        if (s[i].isalpha() == True):
            flag = 1
            break
    if flag == 1:
        print ("True")
    else:
        print ("False")
    flag = 0
    for i in range(0, len(s)):
        if (s[i].isdigit() == True):
            flag = 1
            break
    if flag == 1:
        print ("True")
    else:
        print ("False")
    flag = 0
    for i in range(0, len(s)):
        if (s[i].islower() == True):
            flag = 1
            break
    if flag == 1:
        print ("True")
    else:
        print ("False")
    flag = 0
    for i in range(0, len(s)):
        if (s[i].isupper() == True):
            flag = 1
            break
    if flag == 1:
        print ("True")
    else:
        print ("False")