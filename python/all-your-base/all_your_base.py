def rebase(input_base, digits, output_base) -> list:
    
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    if any(map(lambda x: x < 0 or x >= input_base, digits)):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if input_base == 10:
        return convert_to_output_base(digits, output_base)
    elif output_base == 10:
        return convert_to_decimal(digits, input_base)
    else:
        base_ten = convert_to_decimal(digits, input_base)
        return convert_to_output_base(base_ten, output_base)

def convert_to_output_base(digits, output_base) -> list:
    # divide base number by the output base and record the remainder
    # keep dividing and recording the remainder till the result is 0
    ans = []
    remainder = 0
    result = None

    base = int(''.join(str(digit) for digit in digits))

    while result != 0:
        result = base // output_base # keep floor dividing
        remainder = base % output_base # store the remainder
        ans.insert(0, remainder) # insert always at the beginning of the list
        base = result

    return ans

def convert_to_decimal(digits, input_base) -> list:

    # (digit0 * base ** exponent) + (digit1 * base ** exponent - 1)..
    sum_value = sum(map(lambda x: int(digits[x]) * (input_base ** (len(digits) - x - 1)) , range(0, len(digits), 1)))

    return [int(digit) for digit in str(sum_value)] # return a list with digits