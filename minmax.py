def max(A):
    max = A[0]
    for i in range(1, len(A)):
        if A[i] > max:
            max = A[i]
        else:
            continue
    return max
def min(A):
    min = A[0]
    for i in range(1, len(A)):
        if A[i] < min:
            min = A[i]
        else:
            continue
    return min
    
A = [2,2,5,7,6,9]
print("le max et le min sont: ",max(A), min(A))