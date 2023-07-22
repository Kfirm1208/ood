from collections import deque
class Queue:
    
    def __init__(self):
        self.__queue = deque()
        
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.popleft() if not self.isEmpty() else None
        
    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.queue)
        
    @property
    def queue(self):
        return self.__queue
    
    @queue.setter
    def setQueue(self, queue):
        self.__queue = queue
    
    def __repr__(self):
        return f'{list(self.queue)}'
    
    
class SearchPortal:
    
    def __init__(self):
        self.queue = Queue()
        self.directions= [(0,-1),(1,0),(0,1),(-1,0)]
                
    
    def findStart(self,room):
        for row in room:
            if "F" in row:
                position = (row.index("F"),room.index(row))
            return position
    
    def search(self,room):
        self.queue.enqueue(self.findStart(room))
        if None in self.queue.queue:
            return 'Invaild map input.'
        
        #main loop
        while not self.queue.isEmpty():
            print(f'Queue: {self.queue}')
            if self.findWay(room):
                return "Found the exit portal."
        
        return "Cannot reach the exit portal."
    
    def findWay(self, room):
        x,y = self.queue.dequeue()
        for dx,dy in self.directions:
            new_x,new_y = x + dx,y + dy
            if  0 <= new_y <len(room) and 0 <= new_x <len(room[0]) and room[new_y][new_x] == 'O' :
                return True
            elif 0 <= new_y <len(room) and 0 <= new_x <len(room[0]) and room[new_y][new_x] == '_':
                self.queue.enqueue((new_x,new_y))
                room[new_y][new_x] = 'X'
                
def checkMap(width,height,room):
    search_portal = SearchPortal()
    
    def check_valid_room(width,height,room):
        for row in room:
            if len(row) != width and len(row) != height:
                return False
        return len(room) == height
    
    if check_valid_room(int(width), int(height), room):
        print(search_portal.search(room))
    else:
        print('Invalid map input.')
        
        
def main():   
    widht , height ,room = input('Enter width, height, and room: ').split()
    room = [list(string) for string in room.split(',')]
    checkMap(widht , height ,room)
    
if __name__ == '__main__':
    main()
    
    
    
