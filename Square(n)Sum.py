
# 8 kyu
# Square(n) Sum
# 134332792% of 16,14869,645 of 225,661jhoffner1 Issue Reported

#     Python
#     3.11

#         VIM
#         EMACS

# Instructions
# Output

# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 12+22+22=91^2 + 2^2 + 2^2 = 912+22+22=9.
# Arrays
# Lists
# Fundamentals

def square_sum(numbers):
    print('numbers: ', numbers)
    return sum



def basic_test_cases():
    return True if square_sum([1,2]) == 5
    return True if square_sum([0, 3, 4, 5]) == 50)
    return True if square_sum([]) == 0)
    return True if square_sum([-1,-2]) == 5)
    return True if square_sum([-1,0,1]) == 2)

basic_test_cases()
