
from collections import Counter

test_str = 'life is best,when you are healthy'

print("The original string is : " + str(test_str))

res = Counter(test_str.split())

print("The words frequency : " + str(dict(res)))
