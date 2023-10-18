def is_palindrome(number_as_string:str)->bool:
    return number_as_string == number_as_string[::-1]
number = input().split(", ")
for num in number:
    print(is_palindrome(num))
