def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    print(total)

#unpacking a collection in individual elements
nums = (1,2,3,4,5,6)
sum_all_values(*nums)