# merge function for mergesort algo
# input 2 sorted lists
# output sorted single list

def mergeSort(A):
    #   Base Case
    if len(A) == 1:
        return A
    else:
        left = mergeSort(A[len(A)//2:])
        right = mergeSort(A[:len(A)//2])
        return merge(left, right)


def merge(A, B, C = None): 
#   create list for returning at end of function
    outList = []
#   initialize indexes for A and B lists
    Ai = 0
    Bi = 0
#   set flags to show if A or B lists have been exhausted
    Agood = True
    Bgood = True
#   Total length of both lists combined
    N = len(A + B)

#   initialize splitInv to 0 if C is passed a value
    if C is not None:
        splitInv = 0
    else:
        splitInv = None

#   Loop N times to fill output array
    for i in range( N ):
#   Try to pull lowest number from each input list
#       If an Index Error is found then stop pulling
#       from that list
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
#   Check if both lists are still good. If so compare them        
        if Agood and Bgood:
            if A[Ai] <= B[Bi]:
                outList.append(A[Ai])
                Ai += 1
            elif B[Bi] <= A[Ai]:
                outList.append(B[Bi])
                Bi += 1

#   Count inversions if flagged to do so
                if splitInv is not None:
                    splitInv = splitInv + ((N/2) - i + 1)
#   if B is exhausted just add As
        elif Agood:
            outList.append(A[Ai])
            Ai += 1
#   if A is exhausted just add Bs
        elif Bgood:
            outList.append(B[Bi])
            Bi += 1

#   return tuple with splitInv converted to int if flagged
    if splitInv is not None:
        return (outList, int(splitInv))
#   otherwise return just the output list
    else:
        return outList

