prices = [500, 1200, 800, 2500, 300]
#create discount
def apply_discount(price,discount=10):
    return price - (price * discount / 100)

#print(f"apply_discount(1000) -> {apply_discount(1000)}")

# *args and **kwargs functions

def total(*args):
    return sum(args)

def describe(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

# list comprehension

above_1000 = [p for p in prices if p > 1000]

# map and lambda

with_gst = list(map(lambda p : round(p * 1.18,2),prices))
below_1000 = list(filter(lambda p : p < 1000 , prices))
#print result
print(f"apply_discount(1000) -> {apply_discount(1000)}")
print(f"apply_discount(1000,25) -> {apply_discount(1000,25)}")
print(f"total(5,10,15) -> {total(5,10,15)}")
print(f"Above 1000:{above_1000}")
print(f"with gst: {with_gst}")
print(f"below 1000: {below_1000}")
