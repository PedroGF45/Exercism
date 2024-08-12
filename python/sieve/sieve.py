def primes(limit):

    numbers = {}

    # create a dictionary with {number: "prime / not prime"}
    for i in range(2, limit + 1, 1):
        print(numbers)
        if any(map(lambda x:  i % x == 0, range(i - 1, 1, -1))):
            numbers[i] = "not prime"
        else:
            numbers[i] = "prime"

    # return numbers which are prime
    return [number  for number in numbers if numbers.get(number) == "prime"]
