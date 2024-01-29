def linear_search(target, elements):
    for index in range(0, len(elements)):
        if elements[index] == target:
            return index
    return -1





theList = ['e1', 'e2', 'e3', 'e4', 'e5']
theTarget = 'e4'
secondTarget = 'e100'
print(linear_search(theTarget, theList))
print(linear_search(secondTarget, theList))
