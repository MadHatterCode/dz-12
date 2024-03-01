import string

example_string = '!!!!%$#@Python Community'
# example_string = 'i like python community!'
# example_string = 'Should, I. subscribe? Yes!' + 'a' * 200

hashtag = f'#{"".join(char for char in example_string if char not in string.punctuation).title().replace(" ", "")}'
if len(hashtag) > 140:
    hashtag = f"#{hashtag[1:141]}"
print(hashtag)
