string = "(a4b5c6)"
result = ""

for i in range(len(string)):
    if string[i].isalpha():
        result += string[i]
    elif string[i].isdigit():
        result += string[i-1] * (int(string[i]) - 1)

print(result)
