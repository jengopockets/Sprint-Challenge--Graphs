from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def find_traversal(graph):
    stack = Stack()
    stack.push(0)
    visited = set()
    # print("graph", graph)
    # print("starting room", world.starting_room)
    while len(visited) < len(graph):
        queue = Queue()
        current = stack.stack[-1]
        visited.add(current)
        possible_moves = graph[current][1]
        
        for move, next_room in possible_moves.items():
            if next_room not in visited:
                queue.enqueue(next_room)
        if queue.size() > 0:
            room = queue.queue[0]
            stack.push(room)
        else:
            room = stack.stack[-2]
            stack.pop()
        for move, next_room in possible_moves.items():
            if next_room == room:
                traversal_path.append(move)
                


        

find_traversal(room_graph)
print("traversal", traversal_path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
