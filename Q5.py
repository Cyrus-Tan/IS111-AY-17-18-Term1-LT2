def get_family_members(head):
    """returns all the members of this person’s family (including himself/herself) in a list. The members should be ordered by generation"""
    final_list = []
    flag_variable = True                # Create flag variable for while loop
    # Add the 1st generation
    final_list.append(head[0])
    # Add 2nd generation
    while flag_variable:                # while True
        for each_tuple in head:
            if len(each_tuple) > 1:
                for each_person in each_tuple:
                    next_gen_person = each_person[0]
                    if len(next_gen_person) > 1:            # So that individual letters not included
                        final_list.append(next_gen_person)

            # Add 3rd generation
                for each_person in each_tuple:
                    next_gen_person = each_person[0]       # repeat code so that n gen will be after n-1 gen
                    if len(next_gen_person) > 1:
                        if len(each_person[1]) > 0:           # if list not empty
                            following_gen_person = each_person[1][0][0]
                            final_list.append(following_gen_person)
                    if len(next_gen_person) == 0:
                        flag_variable = False
    return final_list

#print(get_family_members(('Mary', [])))
#print(get_family_members(('Jane', [('Nick', []), ('Wendy', [])])))
#print(get_family_members(('Frank', [('Mary', []), ('Jane', [('Nick', [])])])))
#print(get_family_members(('Alan', [('Bob', [('Chris', [])]), ('Eric', [])])))
print(get_family_members(('Alan', [('Bob', [('Chris', []), ('Debbie', [('Cindy', [])])]), ('Eric', [('Dan', []), ('Fanny', [('George', [])])]), ('Hannah', [])])))

# LEFTOVER ISSUE: Use while loop to keep looping many generations