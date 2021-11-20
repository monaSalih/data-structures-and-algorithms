#  Python 3 Program for
#  Find second largest number in linked list

#  Linked list node
class LinkNode :
	def __init__(self, data) :
		self.data = data
		self.next = None


class SingleLL :
	def __init__(self) :
		self.head = None
		self.tail = None

	#  Add new node at the end of linked list
	def insert(self, value) :
		#  Create a new node
		node = LinkNode(value)
		if (self.head == None) :
			self.head = node
		else :
			self.tail.next = node

		self.tail = node

	#  Display linked list element
	def display(self) :
		if (self.head == None) :
			return

		temp = self.head
		#  iterating linked list elements
		while (temp != None) :
			print(temp.data , end = " → ")
			#  Visit to next node
			temp = temp.next

		print("null")

	#  Find second largest node in linked list
	def secondLargest(self) :
		if (self.head == None) :
			print("\nEmpty linked list")
			return

		#  Display given linked list element
		self.display()
		#  Define some auxiliary variables
		big = None
		result = None
		temp = self.head
		#  iterating linked list elements
		while (temp != None) :
			if (big == None) :
				#  Get first node
				big = temp
			elif (big.data < temp.data) :
				#  Get a new big node
				#  Get second largest node
				result = big
				#  Get current largest node
				big = temp
			elif (big.data != temp.data) :
				if (result == None) :
					#  If in case second largest node empty
					result = temp
				elif (result.data < temp.data) :
					#  Get new second largest node
					result = temp


			#  Visit to next node
			temp = temp.next

		if (result == None) :
			#  When second largest node are not exist in linked list
			print("Second largest element are not exist")
		else :
			print("Second largest : ", result.data)



def main() :
	#  Testing linked list
	list1 = SingleLL()
	# list2 = SingleLL()
	# list3 = SingleLL()
	# list4 = SingleLL()
	#  Add node in first linked list
	#  6 → 4 → 5 → 10 → 3 → 7 → 9 → 2 → 8 → null
	list1.insert(6)
	list1.insert(4)
	list1.insert(5)
	list1.insert(10)
	list1.insert(3)
	list1.insert(7)
	list1.insert(9)
	list1.insert(11)
	list1.insert(8)
	list1.secondLargest()
	#  Add node in second linked list
	#  1 → 1 → 4 → 2 → 3 → 1 → null



if __name__ == "__main__": main()
