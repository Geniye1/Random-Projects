# BASED ON THE LUHN ALGORITHM LESSON ON FREECODECAMP

from random import randint

# ALGORITHM
# -----------
# REVERSE STRING
# SUM UP ALL NUMBERS IN EVEN POSITIONS
# DOUBLE ALL NUMBERS IN ODD POSITIONS
# (IF >= 10 THEN ADD THE TWO DIGITS TOGETHER)
# ADD THE SUM OF EVEN AND ODD NUMBERS TOGETHER
# IF THE SUM % 10 != 0 THEN IT IS NOT VALID, OTHERWISE IT IS VALID!

# CHECK IF NUMBER IS VALID OR NOT
# GENERATE NEW NUMBER USING CHECK DIGIT CALCULATION => 10 - (SUM % 10) = CHECK DIGIT

class EscapeSequences:
    DEFAULT_STYLE = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'

def applyAlgorithm(numberIn, isPayload=True):
    
    # Reverse the string and check if the check digit is included; if it is, remove it.
    reversedCardNumber = ''
    if isPayload:
        reversedCardNumber = numberIn[::-1]
    else:
        checkDigitRemoved = numberIn[:len(numberIn) - 1]
        reversedCardNumber = checkDigitRemoved[::-1]

        #print(f'Number to Check: {numberIn}\nCheck Digit Removed: {checkDigitRemoved}')

    evenNumbers = reversedCardNumber[::2]
    oddNumbers = reversedCardNumber[1::2]

    totalEvenSum = 0
    for num in oddNumbers:
        totalEvenSum += int(num)
    
    totalOddSum = 0
    for num in evenNumbers:
        doubled = int(num) * 2
        if doubled >= 10:
            firstDigit = doubled // 10 # Get first digit
            secondDigit = doubled % 10 # Get second digit
            totalOddSum += firstDigit + secondDigit
        else:
            totalOddSum += doubled
    
    totalSum = totalOddSum + totalEvenSum
    return totalSum

def verifyNumber(number):
    #print('Verifying...')

    # Check if the number is valid by adding the sum of the payload with the check digit and validating that the total sum % 10 is 0 (the sum ends in 0)
    totalSum = applyAlgorithm(number, False)
    checkDigit = int(number[len(number) - 1])
    #print(f'Payload sum: {totalSum}\nCheck Digit: {checkDigit}\nTotal sum: {totalSum + checkDigit}')
    return (totalSum + checkDigit) % 10 == 0

def generateValidNumber():
    # The range is 1 less than the desired length so as to accomadate the check digit that is added later
    generatedNumber = str(randint(pow(10, lengthOfGeneratedNumber - 2), pow(10, lengthOfGeneratedNumber - 1) - 1)) 
    
    # Get the sum of the generated number, then compute the required check digit to make it valid. Add hyphens to make it fancy.
    payloadSum = applyAlgorithm(generatedNumber)

    # If the payload sum already ends in 0, then it is valid and the check digit is simply 0; otherwise, calculate it
    numberString = generatedNumber
    if payloadSum % 10 == 0:
        numberString += '0'
    else:
        checkDigit = (10 - (payloadSum % 10))
        numberString = generatedNumber + str(checkDigit)
    
    # If needed, make it pretty
    #return '-'.join(numberString[i:i+4] for i in range(0, len(numberString), 4))
    return numberString

# SIMULATION TEST
lengthOfGeneratedNumber = 11
simLength = 100
validRuns = 0
invalidRuns = 0
invalidNumbers = []

for i in range(0, simLength):
    generatedNumber = generateValidNumber()
    if verifyNumber(generatedNumber):
        validRuns += 1
    else:
        invalidRuns += 1
        invalidNumbers.append(generatedNumber)

print('Simulation results!')
print(f'Valid runs: {validRuns}')
print(f'Invalid runs: {invalidRuns}')

if len(invalidNumbers) != 0:
    print(f'Invalid numbers: {invalidNumbers}')


#numberToCheck = '17893729974' #SHOULD BE VALID
#numberToCheck = generateValidNumber()
#numberToCheck = '688086172220'

#print(f'\nGenerated number to check: {numberToCheck}\n')

# This is how you remove specific characters from a string
#transTable = str.maketrans({'-': ''})
#numberToCheck = numberToCheck.translate(transTable)

#if verifyNumber(numberToCheck):
#    print(EscapeSequences.GREEN + '\nVALID!')
#else:
#    print(EscapeSequences.RED + '\nINVALID!')


#print(EscapeSequences.DEFAULT_STYLE + '\nNow SCRAM!')