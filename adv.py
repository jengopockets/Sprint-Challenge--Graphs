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
    #Use a stack to keep track of the path
    path = Stack()
    #Set start to 0
    path.push(0)
    #Set for visited
    visited = set()

    # Check if length of visited is less than length of graph
    while len(visited) < len(graph):
        #Use another stack to keep track of posibble next moves
        next_moves = Stack()
        #Set the current room
        current = path.stack[-1]
        #Add current room to visited
        visited.add(current)
        #Check for possible moves in current room
        possible_moves = graph[current][1]
        
        #Loop through possible moves
        for move, next_room in possible_moves.items():
            #Check if rooms have been visited or not
            if next_room not in visited:
                #If not add to next moves stack
                next_moves.push(next_room)
        #If next move push it to path otherwise remove it from path and set the room traversal
        if next_moves.size() > 0:
            room = next_moves.stack[0]
            path.push(room)
        else:
            room = path.stack[-2]
            path.pop()
        #Loop through rooms if the next room is the traversal room append it to traversal.    
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
