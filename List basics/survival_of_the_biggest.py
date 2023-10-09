num_as_str_in_list = input().split()
integers_to_remove = int(input())
num_list = [int(num_str) for num_str in num_as_str_in_list]
smallest_num = 0
for num in range(integers_to_remove):
    smallest_num = min(num_list)
    num_list.remove(smallest_num)
#for element in num_list:
#    print(element, end= " ")
remaining_integers = [str(num) for num in num_list]
result_str = ', '.join(remaining_integers)

print(result_str)