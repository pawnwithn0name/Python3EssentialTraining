from abc import ABC, abstractmethod

class Animal(ABC):
	@abstractmethod
	def walk(self):
		print('base class: walk ()')
		
# Duck IS A animal
class Duck(Animal):
	def walk(self):
		print('derived class: walk ()')
		
def main():
	donald = Duck()
	donald.walk()
	
if __name__ == "__main__": main()