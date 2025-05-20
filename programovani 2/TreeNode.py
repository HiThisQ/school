class Node:
    def __init__(self, k, l=None, p=None):
        self.dato = k
        self.l = l
        self.p = p

koren = Node(10)
koren.l = Node(5)
koren.p = Node(15)
koren.l.l = Node(1)
koren.l.p = Node(7)
koren.p.l = Node(6)
koren.p.p = Node(8)

t = Node(10, Node(5, Node(1), Node(7)), Node(20,None,Node(30)))

def traverz(t):
    if t != None:
        print(t.dato)
        traverz(t.l)
        traverz(t.p)

#print(traverz(t))

def traverzPostorder(t):
    if t != None:
        traverzPostorder(t.l)
        traverzPostorder(t.p)
        print(t.dato)

#print(traverzPostorder(t))

def traverzInorder(t):
    if t != None:
        traverzInorder(t.l)
        print(t.dato)
        traverzInorder(t.p)

#print(traverzInorder(t))

def traverzSoucet(t):
    if t != None:
        return traverzSoucet(t.l) + traverzSoucet(t.p) + t.dato
    else:
        return 0

#print(traverzSoucet(t))

def traverzDepth(t, d=0):
    if t != None:
        return max(traverzDepth(t.l, d+1), traverzDepth(t.p, d+1)) -1
    else:
        return d

#print(traverzDepth(t))

# rekurzivne reverse list
def reverse(list):
    if len(list) <= 0:
        return list
    else:
        head = list.pop(0)
        tail = list

        reverse(tail).append(head)
        return tail

#print(reverse([1, 2, 3]))