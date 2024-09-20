# Redemption for the failed pyramid assignment in that COP python programming class

# Generate a pyramid of * characters at a specified height.
#
# Height = 5:
#
#     *
#    ***
#   *****
#  *******
# *********

# 5 is 9, 6 is 11, 7 is 13
# to get the total number of stars (spaces) plug the height into the following equation: y = 2x - 1

# reverse(range(height))

# 5 is 8 spaces and 1 star,
# 4 is 6 spaces and 3 stars
# 3 is 4 spaces and 5 stars
# 2 is 2 spaces and 7 stars
# 1 is no space and 9 stars

# totalstars - numofstars gives # of spaces
# half the # of spaces and generate that amount of spaces in a string, then concat the star, then add the spaces again

# This is so concise and smol my god im a fucking genius.

generate_characters = lambda char, number : ''.join([char for _ in range(number)])

def generate_pyramid(height):
    final_string = '\n'
    total_number_of_stars = (2 * (height + 1)) - 1
    for number_of_stars in range(1, total_number_of_stars, 2):
        number_of_spaces = total_number_of_stars - number_of_stars
        final_string += generate_characters(' ', int(number_of_spaces / 2)) + generate_characters('*', number_of_stars) + generate_characters(' ', int(number_of_spaces / 2)) + '\n'
    
    return final_string

height = 50

print(generate_pyramid(height))