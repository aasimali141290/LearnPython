def isPallindorme(str):
    str_length = len(str)
    number_of_iterations = int(str_length / 2)

    is_pal = True

    backward_index = -1
    for forwardIndex in range(0, number_of_iterations, 1):
        backward_index = str_length - (forwardIndex + 1)
        forward_char = str[forwardIndex]
        backward_char = str[backward_index]
        if forward_char != backward_char:
            is_pal = False
            break
        else:
            print("comparing {0} at index {1} with {2} at index {3}".format(forwardIndex, forward_char, backward_index, backward_char))

    return is_pal

str = input("input number  ")
print("is palindrome : ", isPallindorme(str))