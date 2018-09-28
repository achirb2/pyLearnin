# merge function for mergesort algo
# input 2 sorted lists
# output sorted single list

def merge(A, B):
    outList = []
    Ai = 0
    Bi = 0
    Agood = True
    Bgood = True
    for i in range( len(A + B) ):
        try:
            if A[Ai]:
                Agood = True
        except IndexError:
            Agood = False
        try:
            if B[Bi]:
                Bgood = True
        except IndexError:
            Bgood = False
        
        if Agood and Bgood:
            if A[Ai] <= B[Bi]:
                outList.append(A[Ai])
                Ai += 1
            elif B[Bi] <= A[Ai]:
                outList.append(B[Bi])
                Bi += 1
        elif Agood:
            outList.append(A[Ai])
            Ai += 1
        elif Bgood:
            outList.append(B[Bi])
            Bi += 1

    print(outList)
    return outList

