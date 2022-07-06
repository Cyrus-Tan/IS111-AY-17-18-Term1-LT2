def get_postal_codes(file_name):
    final_list = []
    data = open(file_name)
    for each_line in data:
        each_line = each_line.strip('\n')       # To remove the empty extra line
        each_line = each_line.split(',')        # Split each line into a list of strings separated by ','
        name_of_person = each_line[0]
        postal_code = each_line[-1].split(' ')[-1]
        each_tuple = (name_of_person, postal_code)
        final_list.append(each_tuple)
    return final_list

print(get_postal_codes('addresses-1.txt'))
