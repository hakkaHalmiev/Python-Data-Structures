import random


def linear_search_steps(runs, elements):
    test_data = [y + 1 for y in range(elements)]
    random.shuffle(test_data)
    target = random.randrange(1, len(test_data))


    while 0 < runs:
        for index in range(0, len(test_data)):
            if test_data[index] == target:
                return index

            runs = runs - 1

            if runs <= 0:
                break


        return -1


linear_search_steps(25, 50)

print(linear_search_steps(25, 50))

