from matplotlib import use
import numpy as np
import matplotlib.pyplot as plt

VRATE = 1 # number of new vertex generated at time t
N = 10001 # total number of vertices in the graph

# box in R2 where vertices are restricted to
XLIM = [-3,3]
XRANGE = XLIM[1]-XLIM[0]

YLIM = [-3,3]
YRANGE = YLIM[1]-YLIM[0]

_x = np.random.uniform(XLIM[0],XLIM[1])
_y = np.random.uniform(YLIM[0],YLIM[1])

verts = np.array([[_x,_y]])
adjMatrix = np.zeros((N,N))

for i in range(10000):
    x = np.random.uniform(XLIM[0],XLIM[1])
    y = np.random.uniform(YLIM[0],YLIM[1])

    new_vert = [[x,y]]

    for k in range(len(verts)):
        ux,uy = verts[k]
        vx,vy = new_vert[0]

        deg = np.sum(adjMatrix[k,:])

        tmp = np.random.uniform()
        if deg == 0:
            if tmp <= 0.3:
                adjMatrix[k][len(verts)] = 1
                adjMatrix[len(verts)][k] = 1
        elif deg > 0:
            dx = np.min(np.abs(vx-ux),XRANGE-np.abs(vx-ux))
            dy = np.min(np.abs(vy-uy),YRANGE-np.abs(vy-uy))
            d = np.sqrt(dx**2+dy**2)
            threshold = 

            if tmp <= threshold:
                adjMatrix[k][len(verts)] = 1
                adjMatrix[len(verts)][k] = 1

    verts = np.append(verts,new_vert,axis=0)

def countFreq(arr, n):
     
    # Mark all array elements as not visited
    visited = [False for i in range(n)]
 
    # Traverse through array elements
    # and count frequencies
    for i in range(n):
         
        # Skip this element if already
        # processed
        if (visited[i] == True):
            continue
 
        # Count frequency
        count = 1
        for j in range(i + 1, n, 1):
            if (arr[i] == arr[j]):
                visited[j] = True
                count += 1
         
        print(arr[i], count)

# print(verts)
# print(adjMatrix)
deg = [np.sum(adjMatrix[i,:]) for i in range(len(adjMatrix))]
countFreq(deg,len(deg))
plt.hist(deg,edgecolor='black')
plt.show()


