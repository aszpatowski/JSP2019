import random
import time
def qsort(A):
    if len(A) <= 1:
        return A
    p = A.pop()
    left =  [a for a in A if a < p]
    right = [a for a in A if a >= p]
    return  qsort(left) + [p] + qsort(right)
N= int(input("Podaj ilość elementów w liscie: "))
A =[random.randrange(1,10000,1) for i in range(N)]
print("Nieposortowana:",A,"\n")
start = time.time()
n = len(A)
end = time.time()
print(end-start,"sekund.")
print("\nPosortowana: ",qsort(A))