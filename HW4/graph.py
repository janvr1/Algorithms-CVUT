# ............................................................................
#                            N O D E
# ............................................................................

class Node:
    def __init__(self, nodeId):
        self.neighbours = []
        self.id = nodeId

    def print(self):
        print(self.id ,"_ ", end = " ")
        for neigh in self.neighbours:
            print(neigh.id, end = ' ')
        print()

# ............................................................................
#                          G R A P H     ( U N D I R E C T E D )
# ............................................................................


class Graph:
    def __init__(self, n):  # discrete graph with no edges
        self.size = n
        self.nodes = []
        for id in range(n):
            self.nodes.append(Node(id))

    def addedge(self, inode1, inode2):
        node1 = self.nodes[inode1]
        node2 = self.nodes[inode2]
        node1.neighbours.append(node2)
        node2.neighbours.append(node1)

    def print(self):
        for node in self.nodes:
            node.print()

# ............................................................................
#                      S T A C K
# ............................................................................

class Stack:
  def __init__(self):
    self.storage = []

  def isEmpty(self):
    return len(self.storage) == 0

  def push(self, node):
    self.storage.append(node)

  def pop(self):
    return self.storage.pop()

  def top(self):
    return self.storage[-1]

# ............................................................................
#                         Q U E U E
# ............................................................................

class Queue:
    def __init__(self, sizeOfQ):
        self.size = sizeOfQ
        self.q = [None] * sizeOfQ
        self.front = 0
        self. tail = 0

    def isEmpty(self):
        return (self.tail == self.front)

    def Enqueue(self, node):
        if self.tail+1 == self.front or \
        self.tail - self.front == self.size-1:
            pass  # implement overflow fixing here
        self.q[self.tail] = node
        self.tail = (self.tail + 1) % self.size

    def Dequeue(self):
        node = self.q[self.front]
        self.front = (self.front + 1) % self.size
        return node

    def front(self):
        return self.Dequeue()

    def push(self, node):
        self.Enqueue(node)



# ............................................................................
#                      G R A P H   S E A R C H
# ............................................................................


def DFS(graph):
    visited = [False] * graph.size
    stack = Stack()
    stack.push(graph.nodes[0])
    visited[0] = True
    while(not stack.isEmpty()):
        node = stack.pop()
        print(node.id, end = " ")
        for neigh in node.neighbours:
            if not visited[neigh.id] :
                stack.push(neigh)
                visited[neigh.id] = True


def BFS(graph):
    visited = [False] * graph.size
    queue = Queue(200)
    queue.Enqueue(graph.nodes[0])
    visited[0] = True
    while(not queue.isEmpty()):
        node = queue.Dequeue()
        print(node.id, end = " ")              # process node
        for neigh in node.neighbours:
            if not visited[neigh.id] :
                queue.Enqueue(neigh)
                visited[neigh.id] = True


def BFS2(graph, nodeId):
    visited = [False] * graph.size
    queue = Queue(200)
    queue.Enqueue(graph.nodes[nodeId])
    visited[nodeId] = True
    while(not queue.isEmpty()):
        node = queue.Dequeue()
        print(node.id, end = " ")              # process node
        for neigh in node.neighbours:
            if not visited[neigh.id]:
                queue.Enqueue(neigh)
                visited[neigh.id] = True


# ____________________________________________________________________________
# ............................................................................
#                              M A I N
# ____________________________________________________________________________

g = Graph(6)
g.addedge(1, 2)
g.addedge(1, 3)
g.addedge(2, 5)
g.addedge(3, 5)
g.addedge(1, 4)
g.addedge(0, 3)

g.print()

DFS(g); print()
BFS(g); print()
BFS2(g, 4); print()

