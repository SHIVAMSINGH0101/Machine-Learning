#!/usr/bin/env python
# coding: utf-8

# In[454]:


#17CY20029
#SHIVAM SINGH
#assignment4_19

#importing numpy and pandas
import numpy as np
import pandas as pd


# In[455]:


#loading dataset

data = pd.read_csv('D:\IIT KGP\ML\CS60050\data4_19.csv')

data.head() #to see 5 rows of data


# In[456]:


#before shuffling the data we will store the three clusters we have from the given ground truth labels
cluster_Iris_setosa = []
cluster_Iris_versicolor = []
cluster_Iris_virginica = []

## Convert our dataset into a numpy array
data = np.array(data)

#to store the dimention of data...
length, width = data.shape

for x in data:
    if(x[4] == 'Iris-setosa'):
        cluster_Iris_setosa.append(x)
    elif(x[4] == 'Iris-versicolor'):
        cluster_Iris_versicolor.append(x)
    else:
        cluster_Iris_virginica.append(x)



#considering only the firts 4 columns

cluster_Iris_setosa = np.array(cluster_Iris_setosa)
cluster_Iris_setosa = cluster_Iris_setosa[:,0:4]

cluster_Iris_versicolor = np.array(cluster_Iris_versicolor)
cluster_Iris_versicolor = cluster_Iris_versicolor[:,0:4]

cluster_Iris_virginica = np.array(cluster_Iris_virginica)
cluster_Iris_virginica = cluster_Iris_virginica[:,0:4]


# In[457]:



#shuffling the data
np.random.shuffle(data)


# In[458]:


#Only first four columns to be considered

new_data = data[:,0:4]
cluster_name = data[:,4]

train_data =new_data


# In[459]:


# Randomly select 3 points as centrods as K=3

#generate of list of 120 number from 0 to 119
numbers = [i for i in range(120)]

#randomly select 3 numbers from the list of numbers
list_of_nums = np.random.choice(numbers, 3, replace=False)

#Randomly place the centroids of the three clusters 
c1 = train_data[list_of_nums[0]]
c2 = train_data[list_of_nums[1]]
c3 = train_data[list_of_nums[2]]
print(c1)
print(c2)
print(c3)


# In[460]:


#number of iterations you want to run 
iteration = 1

while(iteration <= 10):
    cluster_set_1 = []
    cluster_set_2 = []
    cluster_set_3 = []
    for x in train_data:
        #converting from string to float values to perform mathematical operations
        x = x.astype(np.float)
        c1 = [float(i) for i in c1]
        c2 = [float(i) for i in c2]
        c3 = [float(i) for i in c3]
        
        #calculate the eucledian distance between all points the centroid
        x_to_c1 = ((c1[0]-x[0])**2 + (c1[1]-x[1])**2 + (c1[2]-x[2])**2 + (c1[3]-x[3])**2)**0.5
        x_to_c2 = ((c2[0]-x[0])**2 + (c2[1]-x[1])**2 + (c2[2]-x[2])**2 + (c2[3]-x[3])**2)**0.5
        x_to_c3 = ((c3[0]-x[0])**2 + (c3[1]-x[1])**2 + (c3[2]-x[2])**2 + (c3[3]-x[3])**2)**0.5
        x_distances = [x_to_c1, x_to_c2, x_to_c3]
        
        #Now we find the closest centroid to the points and assign the point to that cluster
        pos = x_distances.index(min(x_distances)) #returns index of min distance
        if(pos == 0):
            cluster_set_1.append(x)
        elif(pos == 1):
            cluster_set_2.append(x)
        else:
            cluster_set_3.append(x)
            
    ## Store the centroid values to calculate new centroid values 
    prev_c1 = c1
    prev_c2 = c2
    prev_c3 = c3
    cluster_set_1 = np.array(cluster_set_1)
    cluster_set_2 = np.array(cluster_set_2)
    cluster_set_3 = np.array(cluster_set_3)
    
    # now for each cluster j = 1..k
    # new centroid = mean of all points assigned to that cluster
    #so we find mean of all points within a cluster and make it as the centroid 
    if(len(cluster_set_1) != 0):
        c1 = [sum(cluster_set_1[:,0])/float(len(cluster_set_1)),
              sum(cluster_set_1[:,1])/float(len(cluster_set_1)),
              sum(cluster_set_1[:,2])/float(len(cluster_set_1)),
              sum(cluster_set_1[:,3])/float(len(cluster_set_1))]
    if(len(cluster_set_2) != 0):
        c2 = [sum(cluster_set_2[:,0])/float(len(cluster_set_2)),
              sum(cluster_set_2[:,1])/float(len(cluster_set_2)),
              sum(cluster_set_2[:,2])/float(len(cluster_set_2)),
              sum(cluster_set_2[:,3])/float(len(cluster_set_2))]
    if(len(cluster_set_3) != 0):
        c3 = [sum(cluster_set_3[:,0])/float(len(cluster_set_3)),
              sum(cluster_set_3[:,1])/float(len(cluster_set_3)),
              sum(cluster_set_3[:,2])/float(len(cluster_set_3)),
              sum(cluster_set_3[:,3])/float(len(cluster_set_3))]
        
    #now either no. of iterations are over or if centroid values hasn't changed, algorithm has convereged 
        if(prev_c1 == c1 and prev_c2 == c2 and prev_c3 == c3):
            print("Converged")
        break
    print(iteration)
    iteration += 1


# In[461]:


#print cluster 1
print("Cluster 1: ")
print(cluster_set_1)


# In[462]:


#print cluster 2
print("Cluster 2: ")
print(cluster_set_2)


# In[463]:


#print cluster 3
print("Cluster 3: ")
print(cluster_set_3)


# In[464]:


#calcualting jaccard distance = (union - intersection)/union

#jaccard distance between cluster_set_1 and cluster_Iris_setosa
intersection = []
l1, w1 = cluster_set_1.shape
l2, w2 = cluster_Iris_setosa.shape
for i in range(l1):
    for j in range(l2):
        if(np.array_equal(cluster_set_1[i], cluster_Iris_setosa[j])):
            intersection.append(cluster_set_1[i])

intersection_size = len(intersection)
union_size = l1 + l2 - intersection_size
jaccard_dist_1 = (union_size - intersection_size)/union_size
print("Jaccard distance of cluster 1 with Iris-setosa : %f " %(jaccard_dist_1) )

#jaccard distance between cluster_set_2 and cluster_Iris_setosa
intersection = []
l1, w1 = cluster_set_2.shape
l2, w2 = cluster_Iris_setosa.shape
for i in range(l1):
    for j in range(l2):
        if(np.array_equal(cluster_set_2[i], cluster_Iris_setosa[j])):
            intersection.append(cluster_set_2[i])

intersection_size = len(intersection)
union_size = l1 + l2 - intersection_size
jaccard_dist_2 = (union_size - intersection_size)/union_size
print("Jaccard distance of cluster 2 with Iris-setosa : %f " %(jaccard_dist_2) )      

#jaccard distance between cluster_set_3 and cluster_Iris_setosa
intersection = []
l1, w1 = cluster_set_3.shape
l2, w2 = cluster_Iris_setosa.shape
for i in range(l1):
    for j in range(l2):
        if(np.array_equal(cluster_set_3[i], cluster_Iris_setosa[j])):
            intersection.append(cluster_set_3[i])

intersection_size = len(intersection)
union_size = l1 + l2 - intersection_size
jaccard_dist_3 = (union_size - intersection_size)/union_size
print("Jaccard distance of cluster 3 with Iris-setosa : %f " %(jaccard_dist_3) )

#jaccard distance between cluster_set_1 and cluster_Iris_versicolor
intersection = []
l1, w1 = cluster_set_1.shape
l2, w2 = cluster_Iris_versicolor.shape
for i in range(l1):
    for j in range(l2):
        if(np.array_equal(cluster_set_1[i], cluster_Iris_versicolor[j])):
            intersection.append(cluster_set_1[i])

intersection_size = len(intersection)
union_size = l1 + l2 - intersection_size
jaccard_dist_4 = (union_size - intersection_size)/union_size
print("Jaccard distance of cluster 1 with Iris-versicolor : %f " %(jaccard_dist_4) )  

#jaccard distance between cluster_set_2 and cluster_Iris_versicolor
intersection = []
l1, w1 = cluster_set_2.shape
l2, w2 = cluster_Iris_versicolor.shape
for i in range(l1):
    for j in range(l2):
        if(np.array_equal(cluster_set_2[i], cluster_Iris_versicolor[j])):
            intersection.append(cluster_set_2[i])

intersection_size = len(intersection)
union_size = l1 + l2 - intersection_size
jaccard_dist_5 = (union_size - intersection_size)/union_size
print("Jaccard distance of cluster 2 with Iris-versicolor : %f " %(jaccard_dist_5) ) 

#jaccard distance between cluster_set_3 and cluster_Iris_versicolor
intersection = []
l1, w1 = cluster_set_3.shape
l2, w2 = cluster_Iris_versicolor.shape
for i in range(l1):
    for j in range(l2):
        if(np.array_equal(cluster_set_3[i], cluster_Iris_versicolor[j])):
            intersection.append(cluster_set_3[i])

intersection_size = len(intersection)
union_size = l1 + l2 - intersection_size
jaccard_dist_6 = (union_size - intersection_size)/union_size
print("Jaccard distance of cluster 3 with Iris-versicolor : %f " %(jaccard_dist_6) )   

#jaccard distance between cluster_set_1 and cluster_Iris_virginica

intersection = []
l1, w1 = cluster_set_1.shape
l2, w2 = cluster_Iris_virginica.shape
for i in range(l1):
    for j in range(l2):
        if(np.array_equal(cluster_set_1[i], cluster_Iris_virginica[j])):
            intersection.append(cluster_set_1[i])

intersection_size = len(intersection)
union_size = l1 + l2 - intersection_size
jaccard_dist_7 = (union_size - intersection_size)/union_size
print("Jaccard distance of cluster 1 with Iris-virginica : %f " %(jaccard_dist_7) )   

#jaccard distance between cluster_set_2 and cluster_Iris_virginica
intersection = []
l1, w1 = cluster_set_2.shape
l2, w2 = cluster_Iris_virginica.shape
for i in range(l1):
    for j in range(l2):
        if(np.array_equal(cluster_set_2[i], cluster_Iris_virginica[j])):
            intersection.append(cluster_set_2[i])

intersection_size = len(intersection)
union_size = l1 + l2 - intersection_size
jaccard_dist_8 = (union_size - intersection_size)/union_size
print("Jaccard distance of cluster 2 with Iris-virginica : %f " %(jaccard_dist_8) )   

#jaccard distance between cluster_set_3 and cluster_Iris_virginica
intersection = []
l1, w1 = cluster_set_3.shape
l2, w2 = cluster_Iris_virginica.shape
for i in range(l1):
    for j in range(l2):
        if(np.array_equal(cluster_set_3[i], cluster_Iris_virginica[j])):
            intersection.append(cluster_set_3[i])

intersection_size = len(intersection)
union_size = l1 + l2 - intersection_size
jaccard_dist_9 = (union_size - intersection_size)/union_size
print("Jaccard distance of cluster 3 with Iris-virginica : %f " %(jaccard_dist_9) ) 

