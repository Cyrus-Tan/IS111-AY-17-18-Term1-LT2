def count_long_strings(str_list):
    """function returns the number of strings in the list that have at least 5 characters"""
    count = 0
    for each_item in str_list:
        if len(each_item) > 4:     # if 5 or more chars
            count += 1
    return count

#print(count_long_strings(["apple", "orange", "pear"]))
#print(count_long_strings(["", "S M U", "SMU"]))
print(count_long_strings([]))