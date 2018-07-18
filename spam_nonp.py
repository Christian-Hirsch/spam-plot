import random

def create_nodes(n=300, seed=None):
    """Sample $n$ nodes uniformly at random in the unit square. Each of
    the nodes comes with a random time sampled uniformly from [0, n].
    # Arguments
        n: number of nodes to be sampled
        seed: seed for the randomness
    # Result
        lists ts, xs, ys of time-coordinates x-coordinates and y-coordinates.
        Sorted increasingly in time
    """
    random.seed(seed)
    xs, ys, ts = [[random.random() for _ in range(n)] for _ in range(3)]
    ts = [n * t for t in ts]
    return list(zip(*[[t,x,y] for t,x,y in sorted(zip(ts,xs,ys))]))

def power_prof(delta=5):
    """Power profile function
    # Arguments
        delta: exponent in the power profile
    #Result
        Returns a power profile function of exponent delta
        and total integral .5
    """
    return lambda arg: (1 + arg)**(-delta) * 0.5 * (delta - 1)

def torus_dist(p1, p2):
    """Distance on unit torus
    # Arguments
        p1: coordinates of first point
        p2: coordinates of second point
    #Result
        Returns d^2,[p1_shift,p2_shift], where p1 and p2 are shifted
        version of p1 and p2 such that
        d = |p1 - p2_shift| = |p1_shift - p2|
    """

    shifts = [0, 1, -1]
    pts =[p1, p2]
    pos_xy = [[(abs(c0 - c1 + shift))<.5 for shift in shifts] for c0, c1 in zip(pts[0], pts[1])] 
    
    shift_pts = [[sum([(coord + sign * shift) * pos for shift, pos in zip(shifts, pos_z)])
                  for coord,pos_z in zip(p, pos_xy)]
                for sign, p in zip([1, -1], pts)]
    d = sum([(c0 - c1)**2 for c0, c1  in zip(pts[0], shift_pts[1])] )
    return d, shift_pts


def spam(ts, xs, ys, gamma=.5, profile=power_prof(), seed=None):
    """Spatial preferential attachment model
    # Arguments
        ts: sorted time-coordinates of nodes
        xs: x-coords of nodes
        ys: y-coords of nodes
        gamma: reinforcement parameter
        profile: connection profile function
        seed: seed for the randomness
    #Result
        list of edges defined by endpoints
    """
    random.seed(seed)

    nnn = len(xs)
    edges = []
    xys = [xs, ys]
    degs = [1 for _ in range(nnn)]
    uij = [[random.random() for _ in range(nnn)]
           for _ in range(nnn)]

    for i in range(nnn):
        for j in range(i):

            #compute distance
            pts = [[zs[k] for zs in xys] for k in [i,j]]
            d, shift_pts =  torus_dist(*pts)
            arg = (d * ts[i]) / (gamma * degs[j])

            #is edge drawn?
            if  uij[i][j] > profile(arg):continue
            
            #increase degree
            degs[j] = degs[j] + 1

            #create edges
            [edges.append([pts[i], shift_pts[j]])
             for i, j in zip([0,1], [1,0])]
            
    return edges
