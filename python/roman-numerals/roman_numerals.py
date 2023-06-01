THOUSANDS = 'M'
HUNDREDS = 'C'
HUNDREDS_SUBTRACTOR = 'D'
TENS = 'X'
TENS_SUBTRACTOR = 'L'
UNITS = 'I'
UNITS_SUBTRACTOR = 'V'

def roman(number):
    
    res = ''
    number = str(number)

    for i in range(len(number)):

        # if the number is 0 then ignore it and move to next one
        if int(number[i]) != 0:

            #check if it's a thousand number
            if (len(number) - i == 4):
                res += int(number[i]) * THOUSANDS
            
            #check if it's an hundred number
            if (len(number) - i == 3):

                if (int(number[i]) < 4):
                    res += int(number[i]) * HUNDREDS
                elif (int(number[i]) == 4):
                    res += HUNDREDS + HUNDREDS_SUBTRACTOR 
                elif (int(number[i]) == 9):
                    res += HUNDREDS + THOUSANDS
                else:
                    res += HUNDREDS_SUBTRACTOR + (int(number[i]) - 5) * HUNDREDS

            #check if it's a ten number
            if (len(number) - i == 2):

                if (int(number[i]) < 4):
                    res += int(number[i]) * TENS
                elif (int(number[i]) == 4):
                    res += TENS + TENS_SUBTRACTOR 
                elif (int(number[i]) == 9):
                    res += TENS + HUNDREDS
                else:
                    res += TENS_SUBTRACTOR + (int(number[i]) - 5) * TENS

            #check if it's an unit number
            if (len(number) - i == 1):

                if (int(number[i]) < 4):
                    res += int(number[i]) * UNITS
                elif (int(number[i]) == 4):
                    res += UNITS + UNITS_SUBTRACTOR 
                elif (int(number[i]) == 9):
                    res += UNITS + TENS
                else:
                    res += UNITS_SUBTRACTOR + (int(number[i]) - 5) * UNITS

    return res
