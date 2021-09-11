

# def average(l):
#     if not l:
#         return None
#     return sum(l)/len(l)
# L = [1, 2, 3, 4, 5]
# print(average(L))


# def average(l):
#     if not l:
#         return None
#     return sum(l)/len(l)
#
# if __name__ == "__main__":
#     L = [1, 2, 3, 4, 5]
#     print(average(L))

#
# def average(l):
#     if not l:
#         return None
#     return sum(l)/len(l)
#
# if __name__ == "__main__":
#     L = [1, 2, 3, 4, 5]
#     expected_result = 3
#     if average(L) == expected_result:
#         print("Test passed")
#     else:
#         print("Expected Result is ", expected_result, "and", "Avarage Result is ", average(L))


# assert

assert 2 == 2
assert 2 == 2.0

li = []
assert [] == li

# assert li == [1]
s = "123"
assert s == "123"
# assert s == 123


# assert 3 > 2, "Offcouse 3 is greather then 2"
# assert 3 < 2, "How can 3 be less then 2 ??"



# def average(l):
#     if not l:
#         return None
#     return sum(l)/len(l)
#
# if __name__ == "__main__":
#     L = [1, 2, 3, 4, 5]
#     expected_result = 3.0
#     assert expected_result == average(L), "avarage() produced incorrect result"



# def average(l):
#     if not l:
#         return None
#     return sum(l)/len(l)
#
# def test_average():
#     assert 3.0 == average([1, 2, 3, 4, 5])


#
# def average(l):
#     if not l:
#         return None
#     return sum(l)/len(l)
#
# def test_average():
#     test_cases = [
#         {
#             "Name": "Simple case 1",
#             "input": [1, 2, 3],
#             "expected": 2.0
#         },
#         {
#             "Name": "Simple case 2",
#             "input": [1, 2, 3, 4],
#             "expected": 2.5
#         },
#         {
#             "Name": "list with one item",
#             "input": [100],
#             "expected": 100.0
#         },
#         {
#             "Name": "empty list",
#             "input": [],
#             "expected": None
#         },
#     ]
#
#     for test_case in test_cases:
#         assert test_case["expected"] == average(test_case["input"])#, test_case["Name"]
#
