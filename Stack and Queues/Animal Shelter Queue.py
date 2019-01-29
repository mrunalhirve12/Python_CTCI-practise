#https://github.com/jwhite007/python-practice/tree/master/practice_modules
from queue import Queue


class AnimalShelter(object):
    def __init__(self):
        # super(animalShelter, self).__init__()
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.current_queue = self.queue1
        self.next_queue = self.queue2

    def enqueue(self, kind, name):
        self.current_queue.put((kind, name))

    def dequeue(self, kind='any'):
        if self.current_queue.empty():
            return "The animal shelter currently has no animals for adoption."
        if kind == 'any':
            animal, name = self.current_queue.get()
            return "You have adopted a " + animal + " named " + name + "."
        else:
            adopted = False
            name = None
            while not self.current_queue.empty():
                pet = self.current_queue.get()
                if adopted is False and pet[0] == kind:
                    adopted = True
                    name = pet[1]
                    if self.next_queue.empty():
                        break
                else:
                    self.next_queue.put(pet)
            if self.current_queue.empty():
                self.current_queue, self.next_queue = self.next_queue, self.current_queue
            if adopted is False:
                return "The animal shelter currently has no " + kind + "s."
            else:
                return "You have adopted a " + kind + " named " + name + "."


if __name__ == '__main__':
    shelter = AnimalShelter()
    shelter.enqueue('dog', 'Bear')
    shelter.enqueue('cat', 'Buffy')
    shelter.enqueue('cat', 'Yoda')
    print (shelter.dequeue('cat'))
    print (shelter.dequeue('cat'))
    shelter.enqueue('cat', 'Chelsea')
    print (shelter.dequeue('any'))
    print (shelter.dequeue('dog'))
    shelter.enqueue('cat', 'Oscar')
    print (shelter.dequeue('cat'))