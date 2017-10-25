def is_palindrome(num):
    num = str(num)
    for i in range(len(num)):
        if num[i] != num[len(num) - 1 - i]:
            return False

    return True

def find_greater_palindrome(num):
    while True:
        if is_palindrome(num):
            return num
        num += 1

num_of_inputs = int(input())

for i in range(num_of_inputs):
    num = int(input())
    print(find_greater_palindrome(num))
