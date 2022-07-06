def get_all_permutations(letters):
    final_list = []
    # add first possible
    final_list.append(letters)
    list_of_letters = list(letters)

    print(list_of_letters)
    return final_list
print(get_all_permutations('abc'))

# LEFTOVER ISSUE: How to get all the possible permutations without using itertools.permutations
# -------------> How to swap positions of char of the string