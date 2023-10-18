def odd_or_even_sum(some_number: str):
    sum_of_odd = 0        
    sum_of_even = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            sum_of_even += int(digit)
        else:
            sum_of_odd += int(digit)
    return sum_of_odd, sum_of_even

single_number = input()
sum_of_odd_digits, sum_of_even_digits = odd_or_even_sum(single_number)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
