# #connect nodes of lists and each node has a value. 
# #class for nodes
# #nodes have head and tail ends of a list

class Node(object):
	def __init__(self, value):
		self.value = value
		self.prev = None
		self.next = None

class createDLL(object):
	def __init__(self,initial_val):
		self.initial_val = initial_val
		self.head = Node(initial_val)
		self.tail = None
	def add_node(self, value):
		new_node = Node(value)
		if self.tail == None:
			self.head.next = new_node
			new_node.prev = self.head
		else:
			self.tail.next = new_node
			new_node.prev = self.tail
		self.tail = new_node
		return self
	def delete_node(self, value):
		current_node = self.head
		while current_node != None:
			if current_node.value == value:
				if current_node.prev != None:
					if current_node.next == None:
						self.tail = current_node.prev
						current_node.prev.next = None
					else:
						current_node.prev.next = current_node.next
						current_node.next.prev = current_node.prev
				else:
					current_node.next.prev = None
					self.head = current_node.next
			current_node = current_node.next
		return self
	def display(self):
		current_node = self.head
		result = []
		while current_node != None:
			result.append(current_node.value)
			current_node = current_node.next
		print result
		return self

dll = createDLL(1)
dll.add_node(2).add_node(3).add_node(4).display()
dll.delete_node(4).display().delete_node(1).display()

dll = createDLL(1)
dll.add_node(2).display()

