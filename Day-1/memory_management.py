# Python Performance Optimization & Memory Management 
# Python Use Automatic Memory Management.

# 1. Referance Counting
# 2. Garbage Collection


# Referance Counting - sys.getrefcount()
# Each python object keep track of how many reference(varible) point to it.
# when the reference count reaches 0 , the memory is relesed.

# Garbage Collection - It is Memory management technique used in programming language to automatically reclaim the memory. that no longer accessible 


# shallow copy - make a new copy but nested object still referanced to original object. modifying copied nested object affect original object.

# deep copy - make a new copy and recursively copies all nested objects.modify the copied object does not affect the original object.



import copy

#shallow copy -

array = [1,2,[4,10]]

new_copy = array.copy()

new_copy[2][0] = 90

print("original",array)
print("copy",new_copy)


#deep copy -

data =[1,2,[4,10]]

new_deep_copy = copy.deepcopy(data)

new_copy[2][0] = 90

print("original",array)
print("copy",new_copy)



