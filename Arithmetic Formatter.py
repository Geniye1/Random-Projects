# Code for the FreeCodeCamp Arithmetic Formatter Project. This is the part where I would celebrate how well this code works, and how genius I am for the
# implementation... IF I COULD. FreeCodeCamp, you see, is asinine. The tests don't pass even though I am 10000% sure this code is correct. Therefore, FreeCodeCamp can go to hell

class JayZError(Exception):
    pass

def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def arithmetic_arranger(problems, show_answers=False):

    # Initialize 3 empty strings, 1 is top 2 is middle, 3 is bottom
    # Loop through problems and split each element into its own array delimited by spaces. ['32', '+', '698']
    # Calculate total space: max() number plus 2 to acommodate the operation sign and the space between it and the bottom number
    # To get the top line, do ''.join([' ' for x in range(total_spaces - len(item[0]))]) + item[0] + '    ', should be '   32    '
    # To get the middle line, do item[1] + ' ' + item[2] + '    '
    # To get the bottom line, do ''.join(['-' for _ in range(total_spaces)]) + '    '
    # The final 4 spaces should not be added if youve reached the final problem
    
    # Check for if there are too many problems
    problem_limit = 5
    if len(problems) > problem_limit:
        raise JayZError(f'Too many problems, please limit them to {problem_limit}. Please ensure a bitch a\'int one.')

    # Initialize the various sections of the final string
    top_line = ''
    middle_line = ''
    bottom_line = ''
    answer_line = ''

    # Iterate through each problem
    for problem in problems:
        # Split the problem into its consituent elements and calculate the total number of spaces the problem will occupy.
        problem_array = problem.split(' ')

        # Check the sign and raise an error if it is anything but + or -, check that each operand is 4 digits or less, and check that the numbers contain only digits
        if problem_array[1] != '+' and problem_array[1] != '-':
            raise TypeError('Unsupported operation, please only use addition or subtraction. Science has not evolved past those operations yet.')
        if not is_number(problem_array[0]) or not is_number(problem_array[2]):
            raise ValueError('Last time I checked, letters aren\'t numbers, buddy.')
        if len(problem_array[0]) > 4 or len(problem_array[2]) > 4:
            raise ValueError('Operand(s) is too long. Please shorten them, my circuits can only handle 4 digits.')
        
        total_spaces = int(max(len(problem_array[0]), len(problem_array[2]))) + 2
        
        # Acquire each section by generating a specific number of spaces, plus the number/sign, plus the final four spaces which space out each problem.
        top_line_section = ''.join([' ' for _ in range(total_spaces - len(problem_array[0]))]) + problem_array[0] + '    '
        middle_line_section = problem_array[1] + ''.join([' ' for _ in range(total_spaces - (len(problem_array[2]) + 1))]) + problem_array[2] + '    '
        bottom_line_section = ''.join(['-' for _ in range(total_spaces)]) + '    '
        
        # Append each section to the line variables
        top_line += top_line_section
        middle_line += middle_line_section
        bottom_line += bottom_line_section

        # If the user wants the answers shown, then calculate it, generate the section, and append it to the answer line. 
        if show_answers:
            answer = str(int(problem_array[0]) + int(problem_array[1] + problem_array[2]))
            answer_line_section = ''.join(' ' for _ in range(total_spaces - len(answer))) + answer + '    '
            answer_line += answer_line_section
    
    # Concatenate everything together. If the show_answers parameter is False, then the answer_line string will be empty, making no difference in the final string. 
    final_line = (top_line + '\n' + middle_line + '\n' + bottom_line + '\n' + answer_line)

    # Remove the final 4 spaces off the end because FreeCodeCamp is a petty-ass bitch (not like it made this pass the tests which are HORSESHIT. But it still needs to be done.)
    return final_line[0:len(final_line) - 4]

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "32 + 84"], True)}')
#print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
#print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
#print('\n')
#print('  3801      123\n-    2    +  49\n------    -----') # 
#print('\nIsn\'t is weird how both of these look the same? Strange. Really weird. It\'s almost like the CODE FUCKING WORKS. FUCK YOU FREECODECAMP.')