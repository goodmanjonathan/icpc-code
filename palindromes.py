# South Central USA 2014 - 6795 - Palindrome Numbers

import random

def is_palindrome(num):
    num = str(num)
    for i in range(len(num)):
        if num[i] != num[len(num) - 1 - i]:
            return False

    return True

def find_greater_palindrome(num):
    if is_palindrome(num):
        return num

    numstr = str(num)
    if len(numstr) % 2 == 0:
        left = numstr[:len(numstr) // 2]
        mid = ''
        right = numstr[len(numstr) // 2:]

        if int(right) > int(left[::1]):
            left = str(int(left) + 1)
        right = left[::-1]
    else:
        left = numstr[:len(numstr) // 2]
        mid = numstr[len(numstr) // 2]
        right = numstr[(len(numstr) // 2) + 1:]

        if int(right) > int(left[::1]):
            mid = str((int(mid) + 1) % 10)
            left = str(int(left) + 1) if int(mid) == 0 else left
        right = left[::-1]

        
    return str(left) + str(mid) + str(right)

num_of_inputs = int(input())
for i in range(num_of_inputs):
    num = int(input())
    print(find_greater_palindrome(num))

# while True:
#     randstr = ''
#     for _ in range(random.randint(0, 80)):
#         randstr += str(random.randint(0, 9))
    
#         if is_palindrome(find_greater_palindrome(randstr)):
#             print("Success")
#         else:
#             print("Failure")
#             break
