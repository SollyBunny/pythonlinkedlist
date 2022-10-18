#!/usr/bin/env python3

"""
A linked list class which acts almost identically to the built-in list class with the exception of being... linked.
### Summary of implemented actions:
#### Init
`linkedlist(*iterable)`  
    - Create a new linked list optionally from a preexisting iterable such as a list or another linked list  
#### Methods
`.append(value)`  
    - Add a value to the end  
`.push(value)`  
    - Add a value to the start  
`.insert(index, value)`  
    - Add a value to any index  
`.extend(iterable)`  
    - Add an iterable to the end  
`.copy()`  
    - Create a shallow clone  
`.count(value)`  
    - Count the occurences of a value  
`.index(value, *start, *end)`  
    - Find the first index of a value searching from start to end  
`.remove(value)`  
    - Remove the first index of the item  
`.pop(index)`  
    - Remove the item at index  
`.sort(*key)`  
    - Sort the list with optional swap check function  
#### Arithmatic
`+ iterable`  
    - Append the iterable to the end  
`* int`  
    - Copy the list multiple times  
`+= iterable`  
    - Append the iterable to the end then set  
`*= int`  
    - Copy the list multiple times then set  
"""

class linkedlist:
    class node: pass
    def __init__(self, data = None):
        self.len = 0
        self.head = None
        self.tail = None
        if data == None or len(data) == 0: return
        self.len = 1
        self.head = linkedlist.node()
        self.head.value = data[0]
        self.head.next = None
        temp = self.head
        for i in range(1, len(data)):
            temp.next = linkedlist.node()
            temp = temp.next
            temp.value = data[i]
            self.len += 1
        temp.next = None
        self.tail = temp

    def __rawstr__(self):
        data = ""
        temp = self.head
        i = 0
        while temp and i < self.len:
            data += str(temp.value)
            temp = temp.next
            if temp: data += ", "
            i += 1
        return data
    def __str__(self):
        return "%s([%s])" % (
            self.__class__.__name__, 
            self.__rawstr__()
        )
    def __repr__(self):
        self.__str__()

    def __iter__(self):
        self.iter = self.head
        return self
    def __next__(self):
        if self.iter == None:
            raise StopIteration
        temp = self.iter
        self.iter = self.iter.next
        return temp.value

    def __len__(self):
        return self.len

    def clear(self):
        self.head = None
        self.tail = None
        self.len = 0
    def copy(self):
        return linkedlist(self)

    def extend(self, data):
        self.len += len(data)
        for i in range(len(data)):
            self.tail.next = linkedlist.node()
            self.tail = self.tail.next
            self.tail.value = data[i]
        self.tail.next = None
    def __add__(self, data):
        return self.copy().extend(data)
    def __iadd__(self, data):
        return self.extend(data)
    def __mul__(self, val):
        if val <= 0: return linkedlist()
        out = self.copy()
        if val == 1: return out
        temp = self.head
        val -= 1
        for i in range(out.len * val):
            out.tail.next = linkedlist.node()
            out.tail = out.tail.next
            out.tail.value = temp.value
            if i % out.len == out.len - 1:
                temp = out.head
            else:
                temp = temp.next
        out.tail.next = None
        out.len += out.len * val  
        return out
    def __imul__(self, val):
        if val <= 0:
            self.clear()
            return self
        if val == 1: return self
        temp = self.head
        val -= 1
        for i in range(self.len * val):
            self.tail.next = linkedlist.node()
            self.tail = self.tail.next
            self.tail.value = temp.value
            if i % self.len == self.len - 1:
                temp = self.head
            else:
                temp = temp.next
        self.tail.next = None
        self.len += self.len * val  
        return self
    def append(self, value):
        if self.len == 0:
            self.head = self.tail = linkedlist.node()
            self.head.value = value
            self.head.next = None
        else:
            self.tail.next = linkedlist.node()
            self.tail = self.tail.next
            self.tail.value = value
            self.tail.next = None
        self.len += 1
    def push(self, value):
        if self.len == 0:
            self.head = self.tail = linkedlist.node()
            self.head.value = value
            self.head.next = None
        else:
            temp = linkedlist.node()
            temp.value = value
            temp.next = self.head
            self.head = temp
        self.len += 1
    def insert(self, index, value):
        if self.len == 0:
            self.head = self.tail = linkedlist.node()
            self.head.value = value
            self.head.next = None
        elif index == 0 or index <= -self.len:
            self.push(value)
            return
        elif index >= self.len:
            self.append(value)
            return
        else:
            if index < 0:
                index += self.len
            n = self.head
            l = None
            for i in range(index):
                l = n
                n = n.next
            temp = linkedlist.node()
            temp.value = value
            temp.next = n
            l.next = temp
        self.len += 1
    def pop(self, index = -1):
        if self.head == None:
            raise IndexError("pop from empty %s" % self.__class__.__name__)
        if index <= -self.len or index >= self.len:
            raise IndexError("pop index out of range")
        if index < 0:
            index += self.len
        n = self.head
        l = None
        for i in range(index):
            l = n
            n = n.next
        l.next = n.next
        if l.next == None: self.tail = l
        return n.value

    def index(self, value, start = 0, end = -1):
        if end < 0: end += self.len
        if start < 0: start += self.len
        if self.len == 0 or start >= end or start >= self.len:
            raise ValueError("%s is not in %s" % (value, self.__class__.__name__))
        temp = self.head
        index = start
        for i in range(start - 1):
            temp = temp.next
        for i in range(end - start):
            if temp.value == value: return index
            index += 1
            temp = temp.next
        raise ValueError("%s is not in %s" % (value, self.__class__.__name__))
    def count(self, value):
        if self.head == None:
            return 0
        temp = self.head
        count = 0
        for i in range(self.len):
            if temp.value == value: count += 1
            temp = temp.next
        return count

    def remove(self, value):
        self.pop(self.index(value))

    def __getitem__(self, index):
        if type(index) == int:
            if index < 0:
                index = self.len + index
            if index >= self.len or index < 0:
                raise IndexError("%s index out of range" % self.__class__.__name__)
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp.value
        elif type(index) == slice:
            if index.start is None:
                start = 0
            elif index.start < 0:
                start = self.len + index.start
            else:
                start = index.start
            if index.stop is None:
                stop = self.len
            elif index.start < 0:
                stop = self.len + index.start
            elif index.stop >= self.len:
                stop = self.len
            else:
                stop = index.stop
            reverse = False;
            if index.step is None:
                step = 1
            elif index.step == 0:
                raise ValueError("slice step cannot be zero")
            elif index.step < 0:
                step = -index.step
                reverse = True
                stop, start = start, stop + 1
            else:
                step = index.step
            out = linkedlist()
            if step > self.len: 
                if self.tail: out.append(self.tail.value)
                return out
            if start > stop: return out
            temp = self.head
            for i in range(start + start % step):
                temp = temp.next
            if start == stop:
                if temp: out.append(temp.value)
                return out
            for i in range(0, stop - 1, step):
                if reverse:
                    out.push(temp.value)
                else:
                    out.append(temp.value)
                for _ in range(step):
                    temp = temp.next
                    return out
        else:
            raise TypeError("%s indices must be integers or slices, not str" % self.__class__.__name__)

    def __setitem__(self, index, value):
        if index >= self.len or index <= -self.len:
            raise IndexError("%s assignment index out of range" % self.__class__.__name__)
        elif index < 0:
            index = self.len + index
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.value = value

    def swap(self, a, b):
        if a < 0: a += self.len
        if b < 0: b += self.len
        if a == b: return
        if b > a:
            # a, b = b, a
            temp = b
            b = a
            a = temp
        if b >= self.len or a < 0:
            raise IndexError("%s index out of range" % self.__class__.__name__)
        temp = self.head
        for i in range(b):
            if i == a:
                a = temp
            temp = temp.next
        b = temp
        # a.value, b.value = b.value, a.value
        temp = b.value
    def reverse(self):
        if self.len <= 1: return
        h = self.tail = self.head
        l = None
        n = h.next
        for i in range(self.len - 1):
            l = h
            h = n
            n = h.next
            h.next = l
        self.head = h
        self.tail.next = None
        

if __name__ == "__main__":

    import os
    global errors, total
    errors = 0
    total = 0
    def test(s, real = False):
        global errors, total
        s = s.strip("\n").strip()
        class testlist(list):
            def push(self, a):
                self.insert(0, a)
        l = testlist(range(1, 11))
        if real:
            exec(s)
            a = str(l)
        else:
            try:
                exec(s)
                a = str(l)
            except Exception as e:
                a = e
        l = linkedlist(range(1, 11))
        if real:
            exec(s)
            b = str(l)
        else:
            try:
                exec(s)
                b = str(l)
            except Exception as e:
                b = e
        s = s.ljust(
            os.get_terminal_size().columns - 12,
            " "
            )
        if (
            (
                str(a) != str(b)[11:-1]
            ) if isinstance(a, str) else (
                isinstance(b, str) or
                str(a).replace("linkedlist", "list") != str(b).replace("linkedlist", "list")
            )
        ):
            print("\033[31m%s       Error" % s)
            print("\texpected : %s" % a)
            print("\tgot      : %s\033[0m" % b)
            errors += 1
        elif isinstance(a, Exception):
            print("\033[32m%s  Good (err)\033[0m" % s)
        else:
            print("\033[32m%s        Good\033[0m" % s)
        total += 1

    """
    Test suite for all implemented functions
    """

    # get length of list
    test("l = len(l)")
    test("l.pop(); l = len(l)")
    test("l.append(5); l = len(l)")
    test("l.insert(-1, 5); l = len(l)")

    # clear list
    test("l.clear()")
    # copy list
    test("l = l.copy()")
    test("l.copy()[1] = 5")
    # extend list
    test("l.extend([])")
    test("l.extend([1, 2, 3, 4, 5])")
    test("l = l + []")
    test("l = l + [1, 2, 3, 4, 5]")
    test("l += []")
    test("l += [1, 2, 3, 4, 5]")
    # multiply list
    test("l = l * 5")
    test("l = l * 1")
    test("l = l * 0")
    test("l = l * -1")
    test("l *= 5")
    test("l *= 1")
    test("l *= 0")
    test("l *= -1")
    # reverse list
    test("l.reverse()")
    test("l.append(11); l.reverse()")
    test("l.clear();  l.reverse()")
    test("l.clear(); l.append(1); l.reverse()")

    # set element by index
    test("l[3] = 50")
    test("l[-3] = 50")
    test("l[50] = 50") # NOTE: error
    test("l[-50] = 50") # NOTE: error

    # get element by index
    test("l = l[0]")
    # get element by negative index
    test("l = l[-1]")
    # get element by slice
    test("l = l[1:5]")
    test("l = l[1:5:2]")
    test("l = l[-1:5:2]")
    test("l = l[-1:-5:2]")
    test("l = l[-5:-1:2]")
    test("l = l[1:5:-1]")
    test("l = l[1:5:-3]")
    test("l = l[-1:2:-3]")
    # cannot out of range
    test("l = l[50]") # NOTE: error
    test("l = l[-50]") # NOTE: error
    test("l = l[-50:1]")
    test("l = l[-50:1:-50]")
    test("l = l[50:1:-50]")
    test("l = l[-50:1:-50]")
    test("l = l[-50:50:-50]")

    # push element
    test("l.push(11)")
    # append element
    test("l.append(11)")
    # insert element
    test("l.insert(0, 11)")
    test("l.insert(-1, 11)")
    test("l.insert(-10, 11)")
    test("l.insert(-50, 11)")
    test("l.insert(50, 11)")
    # pop element
    test("l = l.pop()")
    test("l = l.pop(5)")
    test("l = l.pop(-3)")
    test("l = l.pop(50)") # NOTE: error
    test("l = l.pop(-50)") # NOTE: error

    # find element in list
    test("l = l.index(5)")
    test("l = l.index(50)") # NOTE: error
    test("l = l.index(5, 1, 6)")
    test("l = l.index(8, -5, -1)")
    test("l = l.index(8, 5, 5)") # NOTE: error
    test("l = l.index(8, 7, 5)") # NOTE: error
    # count elements in list
    test("l = l.count(5)")
    test("l = l.count(50)")
    test("l.append(5); l = l.count(5)")

    # iterate over list
    test("for i in range(len(l)): l[i] += 5", True) # NOTE: this is incredibly ineffecient

    print("Testing finished: %s/%s (%s%%)" % (
        total - errors, total,
        round((total - errors) / total * 100)
    ))

