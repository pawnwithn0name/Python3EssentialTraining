class Node:

	def __init__(self, contents = None, next = None):
		self.contents = contents
		self.next = next
	
	def getContents(self):
		return self.contents
	
	def __str__(self):
		return str(self.contents)
	
	def print_list(self, node):
		while node:
			print(node.getContents())
			node = node.next
		print()

	def testList(self):
		node1 = Node("C++")
		node2 = Node("Java")
		node3 = Node("Python")
		node4 = Node("Perl")
		node5 = Node("HTML")
		node1.next = node2
		node2.next = node3
		node3.next = node4
		node4.next = node5
		self.print_list(node1)

n = Node()
n.testList()
