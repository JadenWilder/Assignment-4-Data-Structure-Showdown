# Timed Challenge: First Repeated Value
#
# Question:
# Return the first value that repeats in the collection.
# Input: [1, 4, 3, 5, 3, 2, 1]
# Output: 3


def first_repeated_value(values):
    seen = set()

    for value in values:
        if value in seen:
            return value
        seen.add(value)

    return None


# Design justification:
# I chose a set because the main requirement is to quickly determine whether
# each value has already appeared. Set membership and insertion are O(1) on
# average, so the function runs in O(n) time and uses O(n) additional space.


# Test cases
print(first_repeated_value([1, 4, 3, 5, 3, 2, 1]))  # Expected: 3
print(first_repeated_value([10, 20, 30, 20, 40]))    # Expected: 20
print(first_repeated_value([1, 2, 3, 4, 5]))         # Expected: None
print(first_repeated_value([]))                      # Expected: None
print(first_repeated_value(["apple", "banana", "apple"]))  # Expected: apple


"""
Reflection:

For this timed challenge, I chose a set because the problem requires me to
keep track of values that I have already seen. A set makes sense because it
allows me to quickly check whether a value is already present before adding
it. Set membership checks and insertions are O(1) on average, which gives the
overall solution an O(n) time complexity. The set can store up to n values, so
the space complexity is O(n).

The 30-minute time limit shaped my decision because I wanted to use a data
structure that I already understood instead of spending too much time trying
to create a more complicated solution. I focused first on getting a working
solution, then tested it with different inputs and edge cases. This helped me
stay focused on the main requirement instead of overcomplicating the problem.

One trade-off I made was using additional memory to store the values that had
already appeared. A different approach could compare values against other
items in the collection, but that could take O(n^2) time. Under time pressure,
I chose the set because it gave me a simple and efficient solution that was
easy to explain and test.

This challenge showed me that choosing the right data structure can make a
big difference in how efficiently a program runs. It also helped me practice
thinking about runtime and space complexity while solving a problem.
"""