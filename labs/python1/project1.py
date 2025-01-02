import numpy as np

def nearest_neighbor(array1,array2,norm= 2):
 nearest_pair = []
 for point1 in array1:
  distance=np.linalg.norm((array2 - point1 , ord=norm , axis=1))
  nearest_list = np.argmin(distance)
  nearest_pair.append(point1,array2[nearest_list])

  return nearest_pair
 

 array1 = np.array([[1,2],[3,4],[5,6]])
 array2 = np.array([[2,2],[4,3],[5,5]])


 nearest_neighbors = nearest_neighbor(array1,array2,norm= 2)
 for lists in nearest_neighbors:
  print(f"point  {list[0]} is the closest point to {list[1]} ro array_2")