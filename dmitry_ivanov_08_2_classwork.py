#########################################
###   Classwork for lecture 8 pt. 2   ###
#########################################

# I am to lazy to format the output manually
count = 0
def ex():
    global count
    count += 1

    if len(str(count)) == 2:
        padding = ''
    else:
        padding = ' '

    print("╒═══════════════════════╕")
    print("│  Example ", padding, count, "           │", sep="")
    print("└───────────────────────┘")

# CLASSWORK


ex()

stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack [-1]
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())


ex()

class Stack:
    def __init__(self):
        print("Hi!")

stack_object = Stack()
stack_object = Stack()


ex()

class Stack:
    def __init__(self):
        self.list = []

stack_object = Stack()
print(len(stack_object.list))


ex()

class Stack:
    def __init__(self):
        self.__list = []

stack_object = Stack()
#print(len(stack_object.__list))

ex()

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

stack_instance = Stack()

stack_instance.push(3)
stack_instance.push(2)
stack_instance.push(1)

print(stack_instance.pop())
print(stack_instance.pop())
print(stack_instance.pop())

ex()

stack_obj1 = Stack()
stack_obj2 = Stack()

stack_obj1.push(3)
stack_obj2.push(stack_obj1.pop())

print("Stack obj sec:", stack_obj2.pop())



ex()

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    stack_object.pop()


ex()

class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val

print("DICT", ExampleClass.__dict__)

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)


ex()

class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

##   Typing every example takes too much time.
##   From now on I will write down only
##   examples I want to tinker with.

##

ex()


class WeirdOne:
    __one = "That was weird but it worked. NARRATOR: It didn't."
    def myself(self):
        return WeirdOne.__name__

'''
def why_tho(WeirdOne):
    print(self.__one)
'''

one = WeirdOne()
print(one.myself())
