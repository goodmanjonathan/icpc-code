def is_palindrome(num):
    num = str(num)
    for i in range(len(num)):
        if num[i] != num[len(num) - 1 - i]:
            return False

    return True

def find_greater_palindrome(num):
    if is_palindrome(num):
        return num
    #print(num)

    numstr = str(num)
    if len(numstr) % 2 == 0:
        left = numstr[:int(len(numstr) / 2)]
        mid = ''
        right = numstr[int(len(numstr) / 2):]
    else:
        left = numstr[:int(len(numstr) / 2)]
        mid = numstr[int(len(numstr) / 2)]
        right = numstr[int(len(numstr) / 2) + 1:]
        
    #print(left, mid, right)

    if int(right[::-1]) > int(left):
        left = str(int(left) + 1)
    right = int(str(left)[::-1])

    return str(left) + str(mid) + str(right)

num_of_inputs = int(input())

for i in range(num_of_inputs):
    num = int(input())
    print(find_greater_palindrome(num))
