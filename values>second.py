howmany = []
def valgreatersec(*numbers):
    for i in range(len(numbers)):
        if numbers[i] > numbers[1]:
            howmany.append(numbers[i])
        else:
            continue
    print(len(howmany))
    return howmany
print(valgreatersec(1,2,3,4,5))