from collections import deque

class Stack(list):
    def __init__(self) -> None:
        self.main = deque()
        self.new_main = deque([('yellow'), ('blue'), ('yellow'), ('blue'), ('red')])

    def is_empty(self):
        return len(self.new_main) == 0
    
    def push(self, i):
        self.new_main.append(i)
        while self.main:
            self.main.append(self.new_main.popleft())
        self.main, self.new_main = self.new_main, self.main
    
    def pop(self):
        return self.main.popleft()
    
    def peek(self):
         return self.main[0]

    def size(self):
        return self.main.count(0)
    
def balanced(exp):
    balanced_main = tuple('({[')
    unbalanced = tuple(')}]')
    map = dict(zip(balanced_main, unbalanced))
    st = []
    for i in exp:
        if i in balanced_main:
            st.append(map[i])
        elif i in unbalanced:
            if not st or i != st.pop():
                return ' не сбалансированный'
    if not st:
        return 'сбалансрованный'
    else:
        return 'не сбалансированный' 

balanced_string = '[([])((([[[]]])))]{()}'
print(balanced_string, "-", balanced(balanced_string))

unbalanced_string = '{{[(])]}}'
print(unbalanced_string, "-", balanced(unbalanced_string))

stack = Stack()
print('Stack is_empty:', stack.is_empty())
print('Stack push:', stack.push(1))
print('Stsck pop:', stack.pop())
print('Stack peek:', stack.peek())
print('Stacksize:', stack.size())