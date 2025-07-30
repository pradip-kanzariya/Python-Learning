from collections import Counter, deque

# 11. Advanced Data Structures

# Practice Task : 1 | Create a frequency counter for characters in a string.
def frequency_counter():
    """
    Frequency counter for characters in a string.
    """
    my_string = input("Enter string : ")
    return Counter(my_string)


print(frequency_counter())


# Practice Task : 2 | Implement a queue using deque.
class MyQueue:

    def __init__(self):
        self.queue = deque()
        
    def enqueue(self, item):
        return self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft()

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.queue)

q = MyQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())
print(q.is_empty())
print(q.size())


# Practice Task : 2.1 | Create a function to reverse a string using deque.
def rev_string():
    """
    Converts provided string into reverse order.

    Example
    -------
        "abc" -> "cba"
    """
    input_string = input("Enter String : ")
    de_q_str = deque(input_string)
    de_q_str.reverse()
    return "".join(de_q_str)


print(rev_string())

# Practice Task : 2.2 | Create a function to reverse a string using deque and without using built in function reverse().
def rev_string():
    """
    Converts provided string into reverse order.

    Example
    -------
        "abc" -> "cba"
    """
    input_string = input("Enter String : ")
    de_q_str = deque(input_string)
    e_str = deque()
    for x in de_q_str:
        e_str.appendleft(x)
    abc = "".join(e_str)
    return abc


print(rev_string())
