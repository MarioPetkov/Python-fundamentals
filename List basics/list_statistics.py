num_of_inputs = int(input())
positive_list = []
negative_list = []
positive_counter = 0
sum_of_negatives = 0
for i in range(num_of_inputs):
    current_num = int(input())
    if current_num >= 0:
        positive_list.append(current_num)
        positive_counter += 1
    elif current_num < 0:
        negative_list.append(current_num)
        sum_of_negatives += current_num
print(positive_list)
print(negative_list)
print(f"Count of positives: {positive_counter}")
print(f"Sum of negatives: {sum_of_negatives}")
