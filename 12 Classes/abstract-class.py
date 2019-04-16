from abc import ABC, abstractmethod
 
class AbstractClassExample(ABC):
	def __init__(self, value):
		self.value = value

	@abstractmethod
	def do_something(self):
		print('base class func()!')
		
class DoAdd42(AbstractClassExample):
	def do_something(self):
		super().do_something()
		return self.value + 42
    
class DoMul42(AbstractClassExample):
	def do_something(self):
		super().do_something()
		return self.value * 42

def main():
	sum = DoAdd42(10)
	prod = DoMul42(10)
	print(sum.do_something())
	print(prod.do_something())
	
if __name__=="__main__": main()