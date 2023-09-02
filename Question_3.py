lst = list(map(int,input("Enter a list of numbers separated by spaces: ").split()))
logic = lambda x : x*x
result = list(map(logic,lst))
print(result)