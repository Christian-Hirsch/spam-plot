# Spatial preferential attachment model
<img src="spam.png" width="500px"/>

This project provides a python script to plot the [spatial preferential attachment model](https://projecteuclid.org/euclid.aoap/1424355126). This model embeds the classical preferential attachment model into a Euclidean space, thereby making it possible to create clustering effects. More precisely, the nodes <img src="http://latex.codecogs.com/gif.latex?$X_1,&space;X_2,&space;\ldots,&space;X_n$" title="$X_1, X_2, \ldots, X_n$" /></a> are uniformly distributed on the unit torus and as a new node <img src="http://latex.codecogs.com/gif.latex?$X_i$" title="$X_i$" /></a> is born at time <img src="http://latex.codecogs.com/gif.latex?$T_i$" title="$T_i$" />, it connects to any older node <img src="http://latex.codecogs.com/gif.latex?$X_j,j<i$" title="$X_j,j<i$" /> independently with probability

<img src="http://latex.codecogs.com/gif.latex?$$\phi\Big(\frac{T_i\,&space;|X_i&space;-&space;X_j|^2}{\gamma&space;\,\mathsf{deg}_{T_i-}(X_j)}\Big),$$" title="$$\phi\Big(\frac{T_i\, |X_i - X_j|^2}{\gamma \,\mathsf{deg}_{T_i-}(X_j)}\Big),$$" /></a>
<!--$$\phi\Big(\frac{T_i\,  |X_i - X_j|^2}{\gamma \,\mathsf{deg}_{T_i-}(X_j)}\Big),$$-->

where <img src="http://latex.codecogs.com/gif.latex?$\deg_{T_i-}(X_j)$" />  denotes the in-degree of <img src="http://latex.codecogs.com/gif.latex?$X_j$" /> at time <img src="http://latex.codecogs.com/gif.latex?$T_i-$" />. The birth times are uniformly on the interval <img src="http://latex.codecogs.com/gif.latex?$[0, n]$" /> and the parameter <img src="http://latex.codecogs.com/gif.latex?$\gamma>0$" /> controls the strength of the bias towards . Moreover, <img src="http://latex.codecogs.com/gif.latex?$\phi:[0,\infty)&space;\to&space;[0,1]$" /> is a decreasing *profile function* whose integral is normalized to 1/2. For the plotting, we choose a power-law decay with exponent <img src="http://latex.codecogs.com/gif.latex?$\delta>1$" />: 

<img src="http://latex.codecogs.com/gif.latex?$$\phi(x)&space;=&space;0.5&space;(\delta&space;-&space;1)&space;(1&plus;x)^{-\delta}$$" title="$$\phi(x) = 0.5 (\delta - 1) (1+x)^{-\delta}$$" /></a>
<!--$$\varphi(x) = 0.5 (\delta - 1)  (1+x)^{-\delta}$$-->

## Tikz output
The script ``example.py`` allows you to generate a TikZ picture for the spatial preferential attachment model with <img src="http://latex.codecogs.com/gif.latex?$\gamma=2$" /> and <img src="http://latex.codecogs.com/gif.latex?$\delta=5$" />.
To save a realization with 400 nodes and seed 48 into the 'pamPic.tex' run
```sh
python3 example.py 400 48 pamPic.tex
```
