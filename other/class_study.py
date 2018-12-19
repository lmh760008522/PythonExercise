class Dog():
	"""docstring for ClassName"""
	def __init__(self, age,name):
		self.age = age
		self.name = name

	def rollover(self):
		print("the dog "+self.name.title()+" is rollover")

	def  call(self):
		print(self.name.title()+" is "+str(self.age)+" yesrs old")
	

class HappyDog(Dog):
		"""docstring for HappyDog"""
		def __init__(self, age, name):
			super().__init__(age, name)
			self.len_leg = 1.2

		def describe(self):
			print("your_dog's len_leg is",self.len_leg)		

		def rollover(self):
			print(self.name.title(),"never roll over")


my_dog = Dog(6,'ssr')
my_dog.call();
my_dog.rollover();

your_dog  = HappyDog(3,'lmh')
your_dog.call()
your_dog.describe()
your_dog.rollover()
