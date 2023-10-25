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
    for bn in b:  # Проходим по списку b
        if not bn or len(b) < 1:  # Если итерируемый bn пуст или только один элемент
            return a  # возвращаем список a

        for an in a:  # Если элементов больше одного, проходим по списку a, сравнивая с bn
            if a.count(bn) > 1:  # Если bn встречается в списке a более одного раза
                return [x for x in a if x != bn]  # Создаем новый список, исключая все вхождения bn

            if bn == an:  # Если bn равен an
                a.remove(an)  # Удаляем его вхождение bn из списка a

    return a  # Возвращаем список a


def basic_test_cases():
    return all(array_diff([1,2], [1]), array_diff([1,2,2], [1]), array_diff([1,2,2], [2]), array_diff([1,2,2], []), array_diff([], [1,2]), array_diff([1,2,3], [1, 2]))

basic_test_cases()
