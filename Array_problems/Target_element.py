----Target element--------------
def target_element(ar,tr):
    for i in range(len(ar)):
        if ar[i] == tr:
            return True
    return False

Arr=[48,5,3,44,56,78,12]
print(target_element(Arr,78))
