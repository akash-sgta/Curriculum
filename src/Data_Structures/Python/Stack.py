class Stack(object):

	def __init__(self, typeof="class", size=None):
		self.top = -1
		self.typeof = typeof
		self._size = 5 if size == None else size
		self.array = [None for _ in range(self.size)]

	def push(self, data=None):
		if data == None:
			return False,"Invalid Argument"
		else:
			if self.top == self.size-1:
				return False,"Overflow"
			else:
				if self.typeof in str(type(data)):
					self.top += 1
					self.array[self.top] = data
					return True,data
				else:
					return False,"Invalid DataType"

	def pop(self):
		if self.top == -1:
			return False,"Underflow"
		else:
			data = self.array[self.top]
			self.array[self.top] = None
			self.top -= 1
			return True,data
	
	@property
	def size(self):
		return self._size

	def __str__(self):
		stack_ = ""
		for i in range(0, self.size):
			stack_ += f'[{self.array[i]}] '
		return stack_

def main():
	
	stack  = Stack('int',10)
	print(stack.size)
	print(str(stack))
	print(stack.push(10))
	print(str(stack))
	print(stack.push(20))
	print(str(stack))
	print(stack.push(30))
	print(str(stack))
	print(stack.push(40))
	print(str(stack))
	print(stack.push(50))
	print(str(stack))
	print(stack.push(60))
	print(str(stack))
	print(stack.push(70))
	print(str(stack))
	print(stack.push(80))
	print(str(stack))
	print(stack.push(90))
	print(str(stack))
	print(stack.push(100))
	print(str(stack))
	print(stack.push(200))
	print(str(stack))
	print(stack.push(300))
	print(str(stack))
	print(stack.push(400))
	print(str(stack))
	print(stack.pop())
	print(str(stack))
	print(stack.pop())
	print(str(stack))
	print(stack.pop())
	print(str(stack))
	print(stack.pop())
	print(str(stack))
	print(stack.pop())
	print(str(stack))
	print(stack.pop())
	print(str(stack))
	print(stack.pop())
	print(str(stack))
	print(stack.pop())
	print(str(stack))
	print(stack.pop())
	print(str(stack))
	print(stack.pop())
	print(str(stack))
	print(stack.pop())
	print(str(stack))
	print(stack.pop())
	print(str(stack))

	return None



# main()

#----Documentation----
'''
	returns True/False depending on success followed by desired output or error message
'''