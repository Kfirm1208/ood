class Node :
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def merge_sort(self, head):
        if not head or not head.next:
            return head

        # Split the linked list into two halves
        mid = self.find_middle(head)
        left_half = head
        right_half = mid.next
        mid.next = None

        # Recursively sort both halves
        left_half = self.merge_sort(left_half)
        right_half = self.merge_sort(right_half)

        # Merge the sorted halves
        sorted_list = self.merge(left_half, right_half)
        return sorted_list

    def find_middle(self, head):
        if not head:
            return None

        slow_ptr = head
        fast_ptr = head

        while fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr
    def merge(self, left, right):
        dummy_head = Node(0)
        current = dummy_head

        while left and right:
            if left.val > right.val:  # Change the comparison here
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        if left:
            current.next = left
        if right:
            current.next = right

        return dummy_head.next

    def merge_sort_list(self):
        self.head = self.merge_sort(self.head)

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.val) + "\n"
        while cur.next != None:
            s += str(cur.next.val)
            if cur.next.next is not None:  # Check if the next node exists
                s += "\n"
            cur = cur.next
        return s

class Team:
    def __init__(self,name,win,loss,draw,score,concend):
        self.name = name
        self.win = win
        self.loss = loss
        self.draw = draw
        self.score = score
        self.concend = concend
    def __str__(self) -> str:
        point  = self.win*3 + self.draw
        gdd  = self.score - self.concend
        pt = {'points' : point}
        gd = {'gd' : gdd}
        return f"['{self.name}', {pt}, {gd}]"
    
    def __lt__(self,other):
        score_A = (self.win*3 + self.draw)
        scon_A = self.score - self.concend
        score_B = (other.win*3 + other.draw)
        scon_B = other.score - other.concend

        if score_A == score_B:
            return scon_A < scon_B
        return score_A < score_B

inp = input('Enter Input : ').split('/')

team_stats = {}
list_data = LinkedList()

for data in inp:
    # Split the team's data by ","
    team_info = data.split(",")
            
    # Extract the team name (first element in the split)
    team_name = team_info[0]
            
    # Extract the statistics as integers
    stats = [int(stat) for stat in team_info[1:]]

    # Create a Team object for the team
    team = Team(team_name, stats[0], stats[1], stats[2], stats[3], stats[4])
    
    # Append the Team object to the linked list
    list_data.append(team)

list_data.merge_sort_list()
print('== results ==')
print(list_data)
