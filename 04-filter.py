def filter_function(a):
    return a>4
l = [1,2,3,4,5,6,7,8,9]
newl = list(filter(filter_function,l))
print (newl)