
one_to_nineteen = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
                           
tens = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]

def number_to_length(number):

    length = 0

    thou = number // 1000

    hund = number // 100

    remain = number % 100    

    if thou >= 1:
        length += one_to_nineteen[thou] + 8
        return length

    if number % 100 == 0:
        return one_to_nineteen[hund] + 7

    if number > 100: # x hundred and...
        length += one_to_nineteen[hund] + 10

    if remain < 19: # when under 20 the lengths are unique

        length += one_to_nineteen[remain]

    else:  # breaking down remainder into tens and digits
        t = remain // 10

        ones = remain % 10

        length += tens[t]
        length += one_to_nineteen[ones]
        

    return length
    

def one_to_thou():
    total = 0
    for i in range(1,1001):
        print(i)
        print(number_to_length(i))
        total += number_to_length(i)

    print(total)


def one_to_x(x):
    total = 0
    for i in range(1,x):
        # print("Curr Total: " + str(total))
        total += number_to_length(i)

    return total

one_to_thou()

