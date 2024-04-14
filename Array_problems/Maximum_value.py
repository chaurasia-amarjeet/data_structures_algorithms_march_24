-----Maximum value------
def max_value(ar):
    max=0
    for i in range(len(ar)):
        if max < ar[i]:
            max=ar[i]
    return max

Arr=[48,5,3,44,56,78,12]
print(max_value(Arr))