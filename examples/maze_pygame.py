import pampa_search as ps
import copy
import pampa_search.problems as problems

record_gif = True

#strategy = "depth-first"
#strategy = "breadth-first"
strategy = "a-star"
#strategy = "dijkstra"  # in case the problem has all edges with uniform costs, it will perform the same as the breadth-first algorithm

#maze_name = "maze_20_20"   # ./maps/maze_20_20.txt"
#maze_name = "maze_20_20_b"   # ./maps/maze_20_20.txt"
maze_name = "maze_50_50"   # ./maps/maze_20_20.txt"

record_name = strategy+"-"+maze_name   
game = problems.maze("./maps/"+maze_name+".txt",use_pygame=True,record_gif=True,record_name=record_name+".gif")

game.print_board()

test_tree = ps.tree(game,cross_revisit_allowed=False,strategy=strategy)

# decision
next_node = test_tree.root_node
visited_nodes = 0
solved = False
while not(solved):
    test_tree.current_node = next_node
    test_tree.populate_actions_and_children()

    next_node, solved = test_tree.navigate_node(test_tree.current_node)    # also removes current node from nodes_to_visit
    visited_nodes += 1
    game.print_board_from_node(test_tree,next_node)    

    print("Visited nodes: %d \t Nodes to visit: %d"%(visited_nodes,len(test_tree.nodes_to_visit)))
    

game.print_board_from_node(test_tree,test_tree.current_node,final=True)
