class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_list:
    def __init__(self, value):
        self.head = None
        current = None
        for x in value:
            node = Node(x)
            if not self.head:
                self.head = node
                current = self.head
            else:
                current.next = node
                current = current.next
    def to_list(self):
        list = []
        current = self.head
        while current is not None:
            list.append(current.value)
            current = current.next
        return list

    def len(self):
        c = 0
        current = self.head
        while current is not None:
            c += 1
            current = current.next
        return c

    def get_n(self, n):
        current = self.head
        for x in range(n):
            current = current.next
        return current.value

    def has_x(self, x):
        current = self.head
        while current is not None:
            if current.value == x:
                return True
            current = current.next
        return False

    def delete_x(self, x):
        current = self.head
        if self.head == x:
            self.head = self.head.next
            return
        while current.next is not None:
            if current.next == x:
                current.next = current.next.next
            current = current.next
        return

    def rotate(self):
        if self.len() <= 1:
            return
        previous = None
        current = self.head
        while current.next is not None:
            previous = current
            current = current.next
        previous.next = None
        current.next = self.head
        self.head = current
        return
    def starts(self, p, q):
        while p is not None and q is not None:
            if p.value != q.value:
                return False
            p = p.next
            q = q.next
        if q is not None:
            return False
        else:
            return True

    def starts_with_m(self, m):
        list1 = self.head
        list2 = m.head
        if self.starts(list1, list2) is True:
            return True
        else:
            return False

    def contains_m(self, m):
        current = self.head
        list2 = m.head
        while current is not None:
            if self.starts(current, list2) is True:
                return True
            else:
                current = current.next
        return False

    def ends_with_m(self, m):
        len_self = self.len()
        len_m = m.len()
        current = self.head
        list2 = m.head
        difference = len_self - len_m
        if len_self < len_m:
            return False
        for x in range(difference):
            current = current.next
        if self.starts(current, list2) is True:
            return True
        else:
            return False



























