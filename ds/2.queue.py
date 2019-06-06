class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)
	
	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

q = Queue()
q.enqueue(55)
q.push('python')
q.push('is easy')
print('Size of the queue: ', q.size())
print(q.dequeue())
print('Size of the queue:', q.size(	)) 
