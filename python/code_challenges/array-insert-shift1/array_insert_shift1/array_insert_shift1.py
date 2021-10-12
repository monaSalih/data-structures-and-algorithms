import math
#[2,4,6,-8] insert 5
#[2,4,5,6,-6]
def insertShiftArray(arr,x):
    z=0
    for i in arr:
            z+=1    #10
    y=math.ceil(z/2)
    newShiftArray=[]
    l=arr[-1]
    for j in range(0, z-1):

        if y==j:
            newShiftArray+=[x]
            newShiftArray+=[arr[j]]
        else:
            newShiftArray+=[arr[j]]

        # elif j==len(arr)-1:
        #     newShiftArray+=[l]

    newShiftArray+=[l]

    return newShiftArray

