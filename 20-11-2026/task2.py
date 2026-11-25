
def add(a, b):
    return a + b


def average(numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    print("Addition:", add(10, 20))
    print("Average:", average([10, 20, 30, 40]))


from utils.math_tools import add, average

# Addition
result = add(10, 20)
print("Addition:", result)

# Average
numbers = [10, 20, 30, 40, 50]
avg = average(numbers)

print("Average:", avg)





