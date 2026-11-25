# create variables of different data types #
var_int=10
var_float=2.1
var_str="Training"
var_list=[1,2,3]
var_dict={"name":"Bavani","age":30}
var_set={10,20,30}
var_tuple=(100,200,300)
# Print values and their data types #
print(var_int,type(var_int))
print(var_float,type(var_float))
print(var_str,type(var_str))
print(var_list,type(var_list))
print(var_dict,type(var_dict))
print(var_set,type(var_set))
print(var_tuple,type(var_tuple))

# setup the sales data and loop#

sales=[12000,0,8500,15000,-200,9800]
total=0

#loop

for amount in sales:
    #skip zero or negative values
    if amount<=0:
        print(f"skipped invalid values {amount}")
        continue
#update the running total
    total += amount
    print(f"added {amount} total {total}")

    if total > 30000:
        break
#target was reached after the loop
    if total >30000:
        print(f"target reached.stopped at {total}")
    elif total==30000:
        print(f"target reached exactly at{total}")
    else:
        print("target not reached")        