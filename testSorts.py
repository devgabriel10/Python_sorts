import random
from sorts import selection_sort


any_numbers = random.sample(range(1, 1000), 42)

if __name__ == "__main__":
    list = any_numbers
    print(list)
    selection_sort(list)
    print("\n Ordered List:")
    print(list)