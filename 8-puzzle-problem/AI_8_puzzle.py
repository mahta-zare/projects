'''
Mahta A. Zare


Enter the start puzzle:
1 2 3
_ 4 6
7 5 8
Enter the goal puzzle:
1 2 3
4 5 6
7 8 _
'''
import time

class Node:

    def __init__(self,data,level,fvalue,parent):
        self.data = data
        self.fvalue = fvalue
        self.level = level
        self.parent = parent

    def generate_child(self):
        x, y = self.find(self.data, '_')
        value_list = [[x , y-1],[x , y+1], [x-1 , y], [x+1 , y]]
        children = []
        for i in value_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0 ,Node(self.data,self.level,self.fvalue,self.parent))
                children.append(child_node)
        return children


    def find(self,puz,x):
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if puz[i][j] == x:
                    return i,j


    def shuffle(self, puz, x1, y1, x2, y2):
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None


    def copy(self, root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp




class Puzzle:

    def __init__(self,size):
        self.size = size
        self.open_list = []
        self.closed_list = []
        self.nodes_generated = 0
        self.nodes_visited = 0
        self.steps = 0

    def accept_puzzle(self):
        puzzle = []
        for i in range(self.size):
            temp = input().split(" ")
            puzzle.append(temp)
        return puzzle

    def f1(self,start,goal):
        return self.misplaced_h(start.data,goal) + start.level

    def f2(self,start,goal):
        return self.manhattan_h(start.data,goal) + start.level


    def misplaced_h(self,start,goal):
        temp = 0
        for i in range(self.size):
            for j in range(self.size):
                if start[i][j] != goal[i][j] and start[i][j] != "_":
                    temp += 1
        return temp

    def manhattan_h(self,start,goal):
        temp = 0
        for i1 in range(self.size):
            for j1 in range(self.size):
                if start[i1][j1] != "_":
                    flag = 0
                    for i2 in range(self.size):
                        for j2 in range(self.size):
                            if start[i1][j1] == goal[i2][j2]:
                                temp += abs(i1 - i2)
                                temp += abs(j1 - j2)
                                flag = 1
                                break
                            else:
                                continue
                        if flag == 1:
                            break
                        else:
                            continue
        return temp


    def process(self):

        print("Enter the start puzzle: ")
        start = self.accept_puzzle()
        print("Enter the goal puzzle: ")
        goal = self.accept_puzzle()

        print("Enter 1 for misplaced tiles and 2 for manhattan distance: ")
        func = int(input())

        start = Node(start,0,0,None)
        if func == 1:
            start.fvalue = self.f1(start,goal)
        elif func == 2:
            start.fvalue = self.f2(start, goal)
        self.open_list.append(start)
        print("\n")

        t0 = time.time()
        if func == 1:
                while True:
                    current = self.open_list[0]
                    self.nodes_visited += 1
                    if (self.misplaced_h(current.data,goal) == 0):
                        founded = current
                        break
                    for i in current.generate_child():
                        if current.parent != None:
                            flag = 0
                            for i1 in range(self.size):
                                for j1 in range(self.size):
                                    if i.data[i1][j1] == current.parent.data[i1][j1]:
                                           pass
                                    else:
                                        flag = 1
                                        break
                                if flag == 1:
                                    break
                            if flag == 1:
                                i.fvalue = self.f1(i, goal)
                                self.nodes_generated += 1
                                self.open_list.append(i)
                        else:
                            i.fvalue = self.f1(i, goal)
                            self.nodes_generated += 1
                            self.open_list.append(i)
                    self.closed_list.append(current)
                    del self.open_list[0]
                    self.open_list.sort(key = lambda x: x.fvalue, reverse = False)

        if func == 2:
            while True:
                current = self.open_list[0]
                self.nodes_visited += 1
                if (self.manhattan_h(current.data, goal) == 0):
                    founded = current
                    break
                for i in current.generate_child():
                    if current.parent != None:
                        flag = 0
                        for i1 in range(self.size):
                            for j1 in range(self.size):
                                if i.data[i1][j1] == current.parent.data[i1][j1]:
                                    pass
                                else:
                                    flag = 1
                                    break
                            if flag == 1:
                                break
                        if flag == 1:
                            i.fvalue = self.f2(i, goal)
                            self.nodes_generated += 1
                            self.open_list.append(i)
                    else:
                        i.fvalue = self.f2(i, goal)
                        self.nodes_generated += 1
                        self.open_list.append(i)
                self.closed_list.append(current)
                del self.open_list[0]
                self.open_list.sort(key=lambda x: x.fvalue, reverse=False)

        t1 = time.time()

        self.print_path(start,founded)
        print("")
        print("Nodes generated: ", self.nodes_generated)
        print("Nodes visited: ", self.nodes_visited)
        print("Steps to reach goal: ",self.steps)
        print("Wall time: ",t1-t0)

    def print_path(self, start, founded):
        if start.data == founded.data:
            print("---------------------")
            for i in start.data:
                for j in i:
                    print(j, end=" ")
                print("")
        elif founded.parent == None:
            print("No parent")
        else:
            self.steps += 1
            self.print_path(start, founded.parent)
            print("---------------------")
            for i in founded.data:
                for j in i:
                    print(j, end=" ")
                print("")



puzzle = Puzzle(3)
founded = puzzle.process()

