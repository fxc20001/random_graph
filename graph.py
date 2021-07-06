from matplotlib import use
import numpy as np
import matplotlib.pyplot as plt

VRATE = 1 # number of new vertex generated at time t
N = 1000 # total number of vertices in the graph

# box in R2 where vertices are restricted to
XLIM = [-5,5]
XRANGE = XLIM[1]-XLIM[0]

YLIM = [-5,5]
YRANGE = YLIM[1]-YLIM[0]

for num in range(10):
	_x = np.random.uniform(XLIM[0],XLIM[1])
	_y = np.random.uniform(YLIM[0],YLIM[1])

	verts = np.array([[_x,_y]])
	adjMatrix = np.zeros((N,N))

	for i in range(999):
		x = np.random.uniform(XLIM[0],XLIM[1])
		y = np.random.uniform(YLIM[0],YLIM[1])

		new_vert = [[x,y]]

		for k in range(len(verts)):
			ux,uy = verts[k]
			vx,vy = new_vert[0]

			deg = np.sum(adjMatrix[k,:])

			tmp = np.random.uniform()

			dx = min(np.abs(vx-ux),XRANGE-np.abs(vx-ux))
			dy = min(np.abs(vy-uy),YRANGE-np.abs(vy-uy))
			d = np.sqrt(dx**2+dy**2)

			if d <= 2:
				threshold = np.exp(-0.2*d)
			else:
				degfac = 1-1/((1.1**5+deg)**0.2)
				dfac = np.exp(-0.2*d)
	
				threshold = degfac*dfac

			if tmp <= threshold:
				adjMatrix[k][len(verts)] = 1
				adjMatrix[len(verts)][k] = 1

		verts = np.append(verts,new_vert,axis=0)

	#def countFreq(arr, n):
	 
	# Mark all array elements as not visited
	#visited = [False for i in range(n)]

	# Traverse through array elements
	# and count frequencies
	#for i in range(n):
		 
		# Skip this element if already
		# processed
		#if (visited[i] == True):
		    #continue

		# Count frequency
		#count = 1
		#for j in range(i + 1, n, 1):
		    #if (arr[i] == arr[j]):
		        #visited[j] = True
		        #count += 1
		 
		#print(arr[i], count)

	# print(verts)
	# print(adjMatrix)
	deg = [np.sum(adjMatrix[i,:]) for i in range(len(adjMatrix))]
	#countFreq(deg,len(deg))
	plt.figure()
	plt.hist(deg,edgecolor='black')
	plt.savefig('n1000_prod_'+str(num+1)+'.png')



