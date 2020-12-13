class Node:
    def __init__(self, contained_object, next):
        self.contained_object = contained_object
        self.next = next


class MyQueue:
    def __init__(self):
        self.head = None

    def add(self, object):
        new_obj = Node(object, None)
        if self.head is None:
            self.head = new_obj
            return

        last_obj = self.head
        while last_obj.next:
            last_obj = last_obj.next

        last_obj.next = new_obj

    def remove(self):
        if self.head is None:
            return None
        head_obj = self.head
        self.head = self.head.next
        return head_obj

    def clear(self):
        self.head = None

    def turn_into_array(self):
        array = []
        if self.head is not None:
            current_obj = self.head
            while current_obj:
                array.append(current_obj.contained_object)
                current_obj = current_obj.next
        return array


class Country:
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = population

    def __str__(self):
        return "{0}, capital is {1}, population is {2}".format(self.name, self.capital, self.population)


numbers = MyQueue()
for i in range(10):
    MyQueue.add(numbers, 2 * i)

countries = MyQueue()
MyQueue.add(countries, Country('Russia', 'Moscow', 144500000))
MyQueue.add(countries, Country('France', 'Paris', 66990000))
MyQueue.add(countries, Country('Japan', 'Tokyo', 126500000))

numbers_array = MyQueue.turn_into_array(numbers)
print(numbers_array)
countries_array = MyQueue.turn_into_array(countries)
for element in countries_array:
    print(element)
