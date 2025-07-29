# 1. Advanced Python Concepts

# Practice Task : 4 | Use dictionary comprehension to invert a dictionary (keys become values and vice versa).
dict_a = {
    1: "One",
    2: "Two",
    3: "Three"
}
output_dict = {value:key for key,value in dict_a.items()}
print(output_dict)

a = [1,2,3]
b = [4,5,6]

for x,y in zip(a,b):
    print(x,y)