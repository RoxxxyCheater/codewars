# 6 kyu
# Array.diff
# 347163288% of 23,920101,134 of 243,513marcinbunsch2 Issues Reported
#  Python
# 3.11
# VIM
# EMACS
# Instructions
# Output
# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.

# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]
# ARRAYSFUNDAMENTALSALGORITHMS



def array_diff(a, b):
    result = [x for x in a if x not in b]
    return result


def basic_test_cases():
    return all(array_diff([1,2], [1]), array_diff([1,2,2], [1]), array_diff([1,2,2], [2]), array_diff([1,2,2], []), array_diff([], [1,2]), array_diff([1,2,3], [1, 2]))

basic_test_cases()
