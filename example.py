import sys
from spam import create_nodes, spam
from tikz_draw import draw_edges

n = int(sys.argv[1])
seed = int(sys.argv[2])
fname = sys.argv[3]

nodes = create_nodes(n, seed=seed)
edges = spam(*nodes, seed=seed)
draw_edges(edges, fname)
