class FixedQueue:
    
    class Full(Exception):
        pass

    class Empty(Exception):
        pass

    def __init__(self, c : int):
        self.capacity = c
        self.front = 0
        self.rear = 0
        self.no = 0
        self.queue = [None] * self.capacity

    def is_full(self) -> bool:
        if self.no >= self.capacity:
            return True
        else:
            return False

    def is_empty(self) -> bool:
        if self.no <= 0:
            return True
        else:
            return False

    def enque(self, data):
        if self.is_full():
            raise FixedQueue.Full
        self.queue[self.rear] = data
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self):
        if self.is_empty():
            raise FixedQueue.Empty
        r_data = self.queue[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return r_data
        
    def __len__(self):
        return self.no

    def dump(self):
        if self.is_empty():
            print('큐가 비었습니다.')
        else:
            for i in range(self.no):
                print(self.queue[(i + self.front)%self.capacity])

    def peek(self):
        if self.is_empty():
            raise FixedQueue.Empty
        return self.queue[self.front]

    def find(self, value):
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.queue[idx] == value:
                return idx
        return -1

    def count(self, value):
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.queue[idx] == value:
                c += 1
        return c

    def contains(self, value):
        return self.count(value)

    def clear(self):
        self.no = 0
        self.front = 0
        self.rear = 0

