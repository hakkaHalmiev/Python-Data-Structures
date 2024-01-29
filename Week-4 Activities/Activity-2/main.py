import random


def is_sorted(_list):

    if sorted(_list) == _list:
        print("Sorted")
        return True
    else:
        print("Not sorted")
        return False


def _sorted_list(_list):

    sorted_list = sorted(_list)
    return sorted_list


def binary_search(_list, key):
    low = 0
    high = len(_list)-1
    step = 0

    while low <= high:

        step = step+1

        mid = int(low + (high - low)/2)  # To find middle value

        if _list[mid] == key:
            return step

        elif _list[mid] < key:
            low = mid + 1
        else:
            high = mid - 1



    return -1


def create_list(size):

    test_data = [y + 1 for y in range(0, size)]
    random.shuffle(test_data)
    return test_data


x = int(input("Please enter number of size of list : "))
list_1 = create_list(x)
list_1 = _sorted_list(list_1)

target = int(input("Please enter target value : "))

print("Step number is : ", binary_search(list_1, target))



