def saisie():
    n = int(input("Enter le nombre d'éléments: "))
    A = []
    for i in range(1, n+1):
        print("Entrer l'élément ", i, ": ")
        x = int(input())
        A.append(x)
    return A

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
    
A = saisie()
print("le max et le min sont: ",max(A), min(A))