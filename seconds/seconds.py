    # Create a function that takes a list as a parameter,
    # and returns a new list with every second element from the orignal list
    # example: [1, 2, 3, 4, 5] should produce [2, 4]

def seconds(number_list):
    return (number_list[1::2])

print(seconds([1, 2, 3, 4, 5])) # should print [2, 4]
