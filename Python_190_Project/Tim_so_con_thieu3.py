def FindMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output
listOfNumbers = [1, 3, 5, 9]
print(FindMissingNumbers(listOfNumbers))