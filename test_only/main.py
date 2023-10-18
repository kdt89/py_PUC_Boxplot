import timeit

def clear_list():
    my_list.clear()

def assign_empty_list():
    my_list = []

def slice_assignment():
    my_list[:] = []

def del_statement():
    del my_list[:]

my_list = [1, 2, 3, 4, 5]

clear_time = timeit.timeit(clear_list, number=1000000)
assign_time = timeit.timeit(assign_empty_list, number=1000000)
slice_time = timeit.timeit(slice_assignment, number=1000000)
del_time = timeit.timeit(del_statement, number=1000000)

print("clear():", clear_time)
print("assign empty list:", assign_time)
print("slice assignment:", slice_time)
print("del statement:", del_time)
