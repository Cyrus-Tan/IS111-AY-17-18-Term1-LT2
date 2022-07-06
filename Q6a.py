def scramble(letters, file_name):
    final_list = []
    data = open(file_name)
    for each_line in data:
        each_line = each_line.rstrip('\n')     # to remove lines between
        for number in range(len(letters)):
            possible_word = letters[number:] + letters[:number]
            print(possible_word)
            if possible_word == each_line:
                final_list.append(possible_word)
    return final_list

print(scramble('rteid', 'english_words.txt'))

# LEFTOVER ISSUE: How to keep swapping the alphabets