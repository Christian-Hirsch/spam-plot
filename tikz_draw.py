def draw_edges(edges, fname='pamPic.tex', scale=10):
    """Draw edges in tikz
    # Arguments
        edges:list of edges
        fname: name of output file
        scale: scale of tikz picture
    """
    with open(fname,'w') as f:
        f.write('\\begin{tikzpicture}')
        f.write('[scale={}]\n'.format(scale))
        f.write('\\clip (0,0) rectangle (1,1);')

        for p,q in edges:
            f.write("\\draw ({0:.2f},{1:.2f})--({2:.2f},{3:.2f});\n".format(*p,*q))

        f.write('\\end{tikzpicture}')
