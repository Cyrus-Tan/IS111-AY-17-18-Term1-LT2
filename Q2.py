def get_sum_of_odd_numbers(num_list):
    """returns the sum of all the odd numbers in num_list"""
    final_output = 0
    for each_number in num_list:
        if each_number % 2 == 1:         # if remainder is 1, will be odd number
            final_output += each_number
    return final_output
#print(get_sum_of_odd_numbers([9, 4, 6, 7]))
#print(get_sum_of_odd_numbers([4, 13, 8, 12]))
#print(get_sum_of_odd_numbers([6, 18, 44]))
print(get_sum_of_odd_numbers([]))