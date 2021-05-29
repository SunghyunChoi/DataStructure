#Fixed스택 직접 구현해보기
from typing import Any

class FixedStack:
    ##Stack Pointer는 미리 다음 빈 공간을 가리키고 있다.

    class Empty(Exception):
        pass
    class Full(Exception):
        pass

    def __init__(self , c : int) -> None:
        ## 변수 초기화 함수.
        ## stack의 크기를 생성 시 전달받는다.
        self.ptr = 0
        self.capacity = c
        self.stk = [None] * c

    def __len__(self) -> int:
        ## Stack의 길이를 반환하는 함수
        ## ptr은 다음 빈 공간을 가리키고 있기 때문에 길이와 같다.
        return self.ptr

    def is_empty(self) -> bool:
        ## Stack이 비었는지 확인하는 함수
        return self.ptr <= 0

    def is_full(self) -> bool:
        ## Stack이 가득 찼는지 확인하는 함수
        return self.ptr >= self.capacity

    def push(self, data: int) -> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = data
        self.ptr += 1
    
    def pop(self) -> any:
        ## Stack의 가장 바깥에 쌓여있는 데이터를 Stack에서 빼는 함수.
        ## 비었는지 확인하고 data를 return한다. 이 때 ptr만 하나 줄여주면 된다.
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self):
        ## 가장 바깥에 쌓여있는 데이터를 읽어오는 함수
        ## 비어있는지 확인 후 data를 return한다.
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]

    def clear(self):
        ## Stack을 초기화하는 함수
        self.ptr = 0
    
    def find(self, value: Any) -> Any:
        ## 전달받은 값을 찾는 함수.
        ## 찾으면 index를 반환한다.
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value : Any) -> int:
        ## Stack 안에 찾고자 하는 값이 몇개인지 찾는다.
        count = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                count += 1
        return count

    def __contains__(self, value: Any) -> bool:
        ## Stack이 특정 값을 포함하고 있는지 확인하는 함수
        return self.count(value)

    def dump(self) -> None:
        ## 데이터를 바닥부터 꼭대기까지 출력한다.
        ## ptr까지 출력해야 하는 이유는 그 뒤에 삭제하지 않고 남은 데이터가 있을 수도 있기 때문!
        if self.is_empty():
            raise FixedStack.Empty
        else:
            print(self.stk[:self.ptr])
        