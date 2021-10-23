this code for me to descripe what each line do

 def kth(self,k):  #=>[1] -> [3] -> [8] -> [2]=> 3-2
        if k<0:
          return "Exception"

        current=self.head  #data=1  next=3
        ##for loop
        counter=0   #0
        while current:   #1*   3(next 8)

            if current.next == None:   #3*   #8
                current=self.head #or line 121
                break
            else:
                counter +=1           #counter 1*  2
                current =current.next       #3   8
        print(counter)
        # counter-k=LinkedList Value
        #break loop 2 coun3
        #or current=self.head
        value_postion=counter-k #3-0=3///
        # current=1 counter=0
        if k>counter:
            return "Exception"
        counter=0
        while current: # 1 3 8 2(6)
             if current.next == None: #3   8  2 true
               pass
             elif counter ==value_postion: #0 ==3 *  1==3*   2==3*
                 return current.data
             else:
                counter +=1   #1 2  3
                current=current.next #3  8  2
