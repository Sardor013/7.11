#16
'''def sum_it_up(numbers_with_bases):
    total_sum = 0
    for number, base in numbers_with_bases:
        total_sum += int(number, base)
    return total_sum
'''


#17
def stem_and_leaf(numbers):
    plot = {}

    for number in numbers:
        stem = number // 10
        leaf = number % 10

        if stem not in plot:
            plot[stem] = []

        plot[stem].append(leaf)

    for stem in plot:
        plot[stem].sort()

    return plot


#18
def replace_all(data, old, new):
    if isinstance(data, list):
        return [new if item == old else item for item in data]
    elif isinstance(data, str):
        return data.replace(old, new)
    else:
        raise TypeError("Input data should be either a list or a string")


#19
def reverse_invert(lst):
    # Helper function to reverse and invert a single integer
    def reverse_and_invert(n):
        reversed_str = str(abs(n))[::-1]
        reversed_int = int(reversed_str)
        return -reversed_int if n > 0 else reversed_int

    return [reverse_and_invert(x) for x in lst if isinstance(x, int)]


#20
def candies(candies):
    if len(candies) < 2:
        return -1

    max_candies = max(candies)
    total_extra_candies = sum(max_candies - candy for candy in candies)

    return total_extra_candies