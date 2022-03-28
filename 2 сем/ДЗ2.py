import re

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()


check_tags = ['<div>', '<h1>', '<p>', '</div>', '</h1>', '</p>']
open_tags = ['<div>', '<h1>', '<p>']


def append_tags(open_file, list_):
    with open(open_file, 'r') as file:
        f = file.read()
        tags = re.findall(r'<[^>]+>', f)
        for a in tags:
            if a in check_tags:
                list_.append(a)


def HTMLCheck(newfile):
    stack = Stack()
    line1 = []
    append_tags(newfile, line1)
    for ch in line1:
        if ch in open_tags:
            stack.push(ch)
        else:
            curr_char = stack.pop()
            if curr_char == '<div>':
                if ch != "</div>":
                    return False
            if curr_char == '<p>':
                if ch != "</p>":
                    return False
            if curr_char == '<h1>':
                if ch != "</h1>":
                    return False

    if stack.is_empty():
        return True
    return False


print(HTMLCheck('test.html'))