# def reverse_list(ll):
#     """Reverses a linked list
#     Args:
#         ll: linked list
#     Returns:
#         linked list in reversed form
#     """
#     # put your function implementation here
#     return ll


revArr =[1,2,3,4,5,6]
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
#[89, 2354, 3546, 23, 10, -923, 823, -12]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def Reverse(inputArr):
      x=0
      for i in inputArr:
            x+=1    #10
      if (x==1):
         return inputArr

      return Reverse(inputArr[1:]) + inputArr[0:1]




print(Reverse(revArr))
