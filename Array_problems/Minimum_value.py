----minimum value------
def min_value(ar):
    minimum=100
    for i in range(len(ar)):
        if minimum > ar[i]:
            minimum=ar[i]
            #return minimum
    return minimum

Arr=[48,5,3,44,56,78,12]
print(min_value(Arr))
