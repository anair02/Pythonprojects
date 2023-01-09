

def Word_Reverse(input):
    input = input.split()
    result = []
    num = - 1
    for elements in input:
        result.append(input[num])
        num = num - 1
    print(result)
    


user = input('Enter a sentence: ')
Word_Reverse(user)


