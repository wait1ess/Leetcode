#push(x) -- Push element x to the back of queue.
#pop() -- Removes the element from in front of queue.
#peek() -- Get the front element.
#empty() -- Return whether the queue is empty.
class MyQueue(object):

    def __init__(self):
        self._data=[]
        """
        Initialize your data structure here.
        """
        

    def push(self, x):
        self._data.append(x)
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        return self._data.pop(0)
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
    def peek(self):
        return self._data[0]
        """
        Get the front element.
        :rtype: int
        """
        

    def empty(self):
        return len(self._data)==0
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
