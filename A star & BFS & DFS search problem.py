#   Developed by : Mustafa Misho
#   2021/11/28  07:38 PM
#   Version 1.2.0
import heapq
class Queue:
    def __init__(self):
        self.cities = []

    def push(self, city, cost):
        list.append(self.cities, (cost,city))

    def pop(self):
        return list.pop(self.cities,0)[1]


    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False

    def check(self):
        print(self.cities)

class Stack:
    def __init__(self):
        self.cities = []

    def push(self, city, cost):
        list.append(self.cities, (cost,city))

    def pop(self):
        return list.pop(self.cities)[1]

    
    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False

    def check(self):
        print(self.cities)


class priorityQueue:
    def __init__(self):
        self.cities = []

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))

    def pop(self):
        return heapq.heappop(self.cities)[1]

    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False

    def check(self):
        print(self.cities)



class ctNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)
    
    def getVal(self):
        return [self.city,self.distance]
    
def makehuristikdict():
    h = {}
    with open("romania_sld.txt", 'r') as file:
        for line in file:
            line = line.strip().split(",")
            node = line[0].strip()
            sld = int(line[1].strip())
            h[node] = sld
    return h

def heuristic(node, values):
    return values[node]


romania = {}

def makedict():
    file = open("romania.txt", 'r')
    for string in file:
        line = string.split(',')
        ct1 = line[0]
        ct2 = line[1]
        dist = int(line[2])
        romania.setdefault(ct1, []).append(ctNode(ct2, dist))
        romania.setdefault(ct2, []).append(ctNode(ct1, dist))


def printoutput_Astar(start, end, path, distance, CLOSED):
    finalpath = []
    i = end

    while (path[i] != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
    print("Astar algorithm program for Romanian problems")
    print("\tArad => Bucharest")
    print("=======================================================")
    print("City to explore  \t\t: " + str(CLOSED))
    print("Number of possible cities  \t\t: " + str(len(CLOSED)))
    print("=======================================================")
    print("The city that is passed by the shortest distance \t: " + str(finalpath))
    print("Number of cities skipped  \t\t\t: " + str(len(finalpath)))
    print("Total distance  \t\t\t\t\t\t: " + str(distance[end]))



def printoutput_BFS(start, end, path, distance, expandedlist):
    finalpath = []
    i = end

    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
    print("BFS algorithm program for Romanian problems")
    print("\tArad => Bucharest")
    print("=======================================================")
    print("City to explore  \t\t: " + str(expandedlist))
    print("Number of possible cities  \t\t: " + str(len(expandedlist)))
    print("=======================================================")

    print("The city that is passed by the shortest distance \t: " + str(finalpath))
    print("Number of cities skipped  \t\t\t: " + str(len(finalpath)))
    print("Total distance  \t\t\t\t\t\t: " + str(distance[end]))

def printoutput_DFS(start, end, path, distance, expandedlist):
    finalpath = []
    i = end

    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
    print("DFS algorithm program for Romanian problems")
    print("\tArad => Bucharest")
    print("=======================================================")
    print("City to explore  \t\t: " + str(expandedlist))
    print("Number of possible cities  \t\t: " + str(len(expandedlist)))
    print("=======================================================")

    print("The city that is passed by the shortest distance \t: " + str(finalpath))
    print("Number of cities skipped  \t\t\t: " + str(len(finalpath)))
    print("Total distance  \t\t\t\t\t\t: " + str(distance[end]))
    
def greedy(start, end):
    path = {}
    distance = {}
    OPEN = priorityQueue()
    h = makehuristikdict()


    OPEN.push(start, 0)
    distance[start] = 0
    path[start] = None
    CLOSED = []

    while (OPEN.isEmpty() == False):
        current = OPEN.pop()
        CLOSED.append(current)

        if (current == end):
            break

        f_cost = heuristic(current, h)
        
        for new in romania[current]:
            g_cost = distance[current] + int(new.distance)
            

            print(new.city, new.distance, "now : " + str(distance[current]), g_cost)

            if (new.city not in distance or f_cost > heuristic(new.city, h)):
                distance[new.city] = g_cost
                f_cost =  heuristic(new.city, h)
                OPEN.push(new.city, g_cost)
                path[new.city] = current
        
    printoutput_Astar(start, end, path, distance, CLOSED)
    
def astar(start, end):
    path = {}
    distance = {}
    q = priorityQueue()
    h = makehuristikdict()

    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []

    while (q.isEmpty() == False):
        current = q.pop()
        expandedList.append(current)

        if (current == end):
            break

        for new in romania[current]:
            g_cost = distance[current] + int(new.distance)

            # print(new.city, new.distance, "now : " + str(distance[current]), g_cost)

            if (new.city not in expandedList or g_cost < distance[new.city]):
                distance[new.city] = g_cost
                f_cost = g_cost + heuristic(new.city, h)
                q.push(new.city, f_cost)
                path[new.city] = current
        
    printoutput_Astar(start, end, path, distance, expandedList)


    
def BFS(start, end):
    path = {}
    distance = {}
    q = Queue()

    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []

    while (q.isEmpty() == False):
        current = q.pop()
        expandedList.append(current)

        if (current == end):
            break

        for new in romania[current]:
            g_cost = distance[current] + int(new.distance)

            # print(new.city, new.distance, "now : " + str(distance[current]), g_cost)

            if (new.city not in distance):
                distance[new.city] = g_cost
                f_cost = g_cost 
                q.push(new.city, f_cost)
                path[new.city] = current
        
    printoutput_BFS(start, end, path, distance, expandedList)

def DFS(start, end):
    path = {}
    distance = {}
    s = Stack()

    s.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []

    while (s.isEmpty() == False):
        current = s.pop()
        expandedList.append(current)

        if (current == end):
            break

        for new in romania[current]:
            g_cost = distance[current] + int(new.distance)

            # print(new.city, new.distance, "now : " + str(distance[current]), g_cost)

            if (new.city not in distance):
                distance[new.city] = g_cost
                f_cost = g_cost 
                s.push(new.city, f_cost)
                path[new.city] = current
        
    printoutput_DFS(start, end, path, distance, expandedList)



def main():
    src = "Arad"
    dst = "Bucharest"
    makedict()
#    BFS(src,dst)
#    DFS(src,dst)
#    astar(src, dst)
    greedy(src , dst)
    #
if __name__ == "__main__":
    main()    