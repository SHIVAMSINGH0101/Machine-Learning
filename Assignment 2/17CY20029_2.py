#!/usr/bin/env python
# coding: utf-8

# In[1]:


#17CY20029
#SHIVAM SINGH
#assignment2_19

#importing numpy and pandas
import numpy as np
import pandas as pd


# In[2]:


#use this steps to convert comma separated data into different columns

#Highlight the column that contains your list.
#Go to Data > Text to Columns.
#Choose Delimited. Click Next.
#Choose Comma. Click Next.
#Choose General or Text, whichever you prefer.
#Leave Destination as is, or choose another column. Click Finish.

#loading dataset

filename = "data2_19.csv"
train_data = pd.read_csv(filename, sep=',', header = 0)

train_data.head() #to see 5 columns of data


# In[3]:


#split data into dependent and independent variable 

X = train_data.values[:,1:7]
Y = train_data.values[:,0]

length, width = X.shape


# In[4]:


count_class1 = 0
count_class2 = 0

#probabilities of each value(1-5) of each feature(X1-X6) is calculated below

count_X1_1_class1 = 1
count_X1_2_class1 = 1
count_X1_3_class1 = 1
count_X1_4_class1 = 1
count_X1_5_class1 = 1

count_X2_1_class1 = 1
count_X2_2_class1 = 1
count_X2_3_class1 = 1
count_X2_4_class1 = 1
count_X2_5_class1 = 1

count_X3_1_class1 = 1
count_X3_2_class1 = 1
count_X3_3_class1 = 1
count_X3_4_class1 = 1
count_X3_5_class1 = 1

count_X4_1_class1 = 1
count_X4_2_class1 = 1
count_X4_3_class1 = 1
count_X4_4_class1 = 1
count_X4_5_class1 = 1

count_X5_1_class1 = 1
count_X5_2_class1 = 1
count_X5_3_class1 = 1
count_X5_4_class1 = 1
count_X5_5_class1 = 1

count_X6_1_class1 = 1
count_X6_2_class1 = 1
count_X6_3_class1 = 1
count_X6_4_class1 = 1
count_X6_5_class1 = 1

count_X1_1_class2 = 1
count_X1_2_class2 = 1
count_X1_3_class2 = 1
count_X1_4_class2 = 1
count_X1_5_class2 = 1

count_X2_1_class2 = 1
count_X2_2_class2 = 1
count_X2_3_class2 = 1
count_X2_4_class2 = 1
count_X2_5_class2 = 1

count_X3_1_class2 = 1
count_X3_2_class2 = 1
count_X3_3_class2 = 1
count_X3_4_class2 = 1
count_X3_5_class2 = 1

count_X4_1_class2 = 1
count_X4_2_class2 = 1
count_X4_3_class2 = 1
count_X4_4_class2 = 1
count_X4_5_class2 = 1

count_X5_1_class2 = 1
count_X5_2_class2 = 1
count_X5_3_class2 = 1
count_X5_4_class2 = 1
count_X5_5_class2 = 1

count_X6_1_class2 = 1
count_X6_2_class2 = 1
count_X6_3_class2 = 1
count_X6_4_class2 = 1
count_X6_5_class2 = 1

#to calculate probabilities we go through each dataset entry

for i in range(length):

    if Y[i] == 0: #first calculate counts of class1 which is 0 
    
        count_class1 = count_class1 +1
        
        for j in range(width):   #for each value(X1-X6) of a entry
            if j==0:  #for X1
            
                if X[i,j]==1: 
            
                  count_X1_1_class1 = count_X1_1_class1 + 1  
            
                elif X[i,j]==2: 
            
                  count_X1_2_class1 = count_X1_2_class1 + 1  
            
                elif X[i,j]==3:
            
                  count_X1_3_class1 = count_X1_3_class1 + 1  
            
                elif X[i,j]==4: 
            
                  count_X1_4_class1 = count_X1_4_class1 + 1  
            
                elif X[i,j]==5: 
            
                  count_X1_5_class1 = count_X1_5_class1 + 1 
      
            if j == 1:  #for X2
        
                if X[i,j]==1: 
            
                  count_X2_1_class1 = count_X2_1_class1 + 1  
            
                elif X[i,j]==2: 
            
                  count_X2_2_class1 = count_X2_2_class1 + 1  
            
                elif X[i,j]==3:
            
                  count_X2_3_class1 = count_X2_3_class1 + 1  
            
                elif X[i,j]==4: 
            
                  count_X2_4_class1 = count_X2_4_class1 + 1  
            
                elif X[i,j]==5: 
            
                  count_X2_5_class1 = count_X2_5_class1 + 1 
                  
          
            if j == 2:  #for X3
        
                if X[i,j]==1: 
            
                  count_X3_1_class1 = count_X3_1_class1 + 1  
                
                elif X[i,j]==2: 
            
                  count_X3_2_class1 = count_X3_2_class1 + 1  
            
                elif X[i,j]==3:
            
                  count_X3_3_class1 = count_X3_3_class1 + 1  
            
                elif X[i,j]==4: 
            
                  count_X3_4_class1 = count_X3_4_class1 + 1  
            
                elif X[i,j]==5: 
            
                  count_X3_5_class1 = count_X3_5_class1 + 1 
                
    
            if j == 3:  #for X4
        
                if X[i,j]==1: 
            
                  count_X4_1_class1 = count_X4_1_class1 + 1  
            
                elif X[i,j]==2: 
            
                  count_X4_2_class1 = count_X4_2_class1 + 1  
            
                elif X[i,j]==3:
            
                  count_X4_3_class1 = count_X4_3_class1 + 1  
            
                elif X[i,j]==4: 
            
                  count_X4_4_class1 = count_X4_4_class1 + 1  
            
                elif X[i,j]==5: 
            
                  count_X4_5_class1 = count_X4_5_class1 + 1 
    
       
            if j == 4:  #for X5
        
                if X[i,j]==1: 
            
                  count_X5_1_class1 = count_X5_1_class1 + 1  
            
                elif X[i,j]==2: 
            
                  count_X5_2_class1 = count_X5_2_class1 + 1  
            
                elif X[i,j]==3:
            
                  count_X5_3_class1 = count_X5_3_class1 + 1  
            
                elif X[i,j]==4: 
            
                  count_X5_4_class1 = count_X5_4_class1 + 1  
            
                elif X[i,j]==5: 
            
                  count_X5_5_class1 = count_X5_5_class1 + 1 
        
        
            if j == 5:   #for X6
        
                if X[i,j]==1: 
            
                  count_X6_1_class1 = count_X1_1_class1 + 1  
            
                elif X[i,j]==2: 
            
                  count_X6_2_class1 = count_X1_2_class1 + 1  
            
                elif X[i,j]==3:
            
                  count_X1_3_class1 = count_X1_3_class1 + 1  
            
                elif X[i,j]==4: 
            
                  count_X1_4_class1 = count_X1_4_class1 + 1  
            
                elif X[i,j]==5: 
            
                  count_X1_5_class1 = count_X1_5_class1 + 1 
        
        
        
        
    elif Y[i] == 1: #then calculate counts of class2 which is 1
    
        count_class2 = count_class2 +1
        
        
        for j in range(width):  #for each value(X1-X6) of a entry
            
            if j==0:   #for X1
                if X[i,j]==1: 
            
                  count_X1_1_class2 = count_X1_1_class2 + 1  
            
                elif X[i,j]==2: 

                    count_X1_2_class2 = count_X1_2_class2 + 1  

                elif X[i,j]==3:

                    count_X1_3_class2 = count_X1_3_class2 + 1  

                elif X[i,j]==4: 

                    count_X1_4_class2 = count_X1_4_class2 + 1  

                elif X[i,j]==5: 

                    count_X1_5_class2 = count_X1_5_class2 + 1 

            if j == 1:   #for X2

                if X[i,j]==1: 

                    count_X2_1_class2 = count_X2_1_class2 + 1  

                elif X[i,j]==2: 

                    count_X2_2_class2 = count_X2_2_class2 + 1  

                elif X[i,j]==3:

                    count_X2_3_class2 = count_X2_3_class2 + 1  

                elif X[i,j]==4: 

                    count_X2_4_class2 = count_X2_4_class2 + 1  

                elif X[i,j]==5: 

                    count_X2_5_class2 = count_X2_5_class2 + 1 
                  
          
            if j == 2:   #for X3
        
                if X[i,j]==1: 
            
                  count_X3_1_class2 = count_X3_1_class2 + 1  
            
                elif X[i,j]==2: 
            
                  count_X3_2_class2 = count_X3_2_class2 + 1  
            
                elif X[i,j]==3:
            
                  count_X3_3_class2 = count_X3_3_class2 + 1  
                
                elif X[i,j]==4: 
            
                  count_X3_4_class2 = count_X3_4_class2 + 1  
            
                elif X[i,j]==5: 
            
                  count_X3_5_class2 = count_X3_5_class2 + 1 
                
    
            if j == 3:   #for X4
        
                if X[i,j]==1: 
            
                  count_X4_1_class2 = count_X4_1_class2 + 1  
            
                elif X[i,j]==2: 
            
                  count_X4_2_class2 = count_X4_2_class2 + 1  
            
                elif X[i,j]==3:
            
                  count_X4_3_class2 = count_X4_3_class2 + 1  
            
                elif X[i,j]==4: 
            
                  count_X4_4_class2 = count_X4_4_class2 + 1  
            
                elif X[i,j]==5: 
            
                  count_X4_5_class2 = count_X4_5_class2 + 1 
    
       
            if j == 4:   #for X5
        
                if X[i,j]==1: 
            
                  count_X5_1_class2 = count_X5_1_class2 + 1  
            
                elif X[i,j]==2: 
            
                  count_X5_2_class2 = count_X5_2_class2 + 1  
            
                elif X[i,j]==3:
            
                  count_X5_3_class2 = count_X5_3_class2 + 1  
            
                elif X[i,j]==4: 
            
                  count_X5_4_class2 = count_X5_4_class2 + 1  
            
                elif X[i,j]==5: 
            
                  count_X5_5_class2 = count_X5_5_class2 + 1 
        
        
            if j == 5:   #for X6
        
                if X[i,j]==1: 
            
                  count_X6_1_class2 = count_X1_1_class2 + 1  
            
                elif X[i,j]==2: 
            
                  count_X6_2_class2 = count_X1_2_class2 + 1  
            
                elif X[i,j]==3:
            
                  count_X1_3_class2 = count_X1_3_class2 + 1  
            
                elif X[i,j]==4: 
                
                  count_X1_4_class2 = count_X1_4_class2 + 1  
            
                elif X[i,j]==5: 
            
                  count_X1_5_class2 = count_X1_5_class2 + 1 
            
             

prob_class1 = count_class1/length   #calculate probability of class1 

prob_class2 = count_class2/length   #calculate probability of class2


#calculate conditional probabilities

prob_X1_1_class1 = count_X1_1_class1 / (count_class1)  #probability of X1 = 1 of class 1 i.e. class = 0(unhappy)
prob_X2_1_class1 = count_X2_1_class1 / (count_class1)
prob_X3_1_class1 = count_X3_1_class1 / (count_class1)
prob_X4_1_class1 = count_X4_1_class1 / (count_class1)
prob_X5_1_class1 = count_X5_1_class1 / (count_class1)
prob_X6_1_class1 = count_X6_1_class1 / (count_class1)

prob_X1_2_class1 = count_X1_2_class1 / (count_class1)
prob_X2_2_class1 = count_X2_2_class1 / (count_class1)
prob_X3_2_class1 = count_X3_2_class1 / (count_class1)
prob_X4_2_class1 = count_X4_2_class1 / (count_class1)
prob_X5_2_class1 = count_X5_2_class1 / (count_class1)
prob_X6_2_class1 = count_X6_2_class1 / (count_class1)

prob_X1_3_class1 = count_X1_3_class1 / (count_class1)
prob_X2_3_class1 = count_X2_3_class1 / (count_class1)
prob_X3_3_class1 = count_X3_3_class1 / (count_class1)
prob_X4_3_class1 = count_X4_3_class1 / (count_class1)
prob_X5_3_class1 = count_X5_3_class1 / (count_class1)
prob_X6_3_class1 = count_X6_3_class1 / (count_class1)

prob_X1_4_class1 = count_X1_4_class1 / (count_class1)
prob_X2_4_class1 = count_X2_4_class1 / (count_class1)
prob_X3_4_class1 = count_X3_4_class1 / (count_class1)
prob_X4_4_class1 = count_X4_4_class1 / (count_class1)
prob_X5_4_class1 = count_X5_4_class1 / (count_class1)
prob_X6_4_class1 = count_X6_4_class1 / (count_class1)

prob_X1_5_class1 = count_X1_5_class1 / (count_class1)
prob_X2_5_class1 = count_X2_5_class1 / (count_class1)
prob_X3_5_class1 = count_X3_5_class1 / (count_class1)
prob_X4_5_class1 = count_X4_5_class1 / (count_class1)
prob_X5_5_class1 = count_X5_5_class1 / (count_class1)
prob_X6_5_class1 = count_X6_5_class1 / (count_class1)




prob_X1_1_class2 = count_X1_1_class2 / (count_class2)
prob_X2_1_class2 = count_X2_1_class2 / (count_class2)
prob_X3_1_class2 = count_X3_1_class2 / (count_class2)
prob_X4_1_class2 = count_X4_1_class2 / (count_class2)
prob_X5_1_class2 = count_X5_1_class2 / (count_class2)
prob_X6_1_class2 = count_X6_1_class2 / (count_class2)

prob_X1_2_class2 = count_X1_2_class2 / (count_class2)
prob_X2_2_class2 = count_X2_2_class2 / (count_class2)
prob_X3_2_class2 = count_X3_2_class2 / (count_class2)
prob_X4_2_class2 = count_X4_2_class2 / (count_class2)
prob_X5_2_class2 = count_X5_2_class2 / (count_class2)
prob_X6_2_class2 = count_X6_2_class2 / (count_class2)

prob_X1_3_class2 = count_X1_3_class2 / (count_class2)
prob_X2_3_class2 = count_X2_3_class2 / (count_class2)
prob_X3_3_class2 = count_X3_3_class2 / (count_class2)
prob_X4_3_class2 = count_X4_3_class2 / (count_class2)
prob_X5_3_class2 = count_X5_3_class2 / (count_class2)
prob_X6_3_class2 = count_X6_3_class2 / (count_class2)

prob_X1_4_class2 = count_X1_4_class2 / (count_class2)
prob_X2_4_class2 = count_X2_4_class2 / (count_class2)
prob_X3_4_class2 = count_X3_4_class2 / (count_class2)
prob_X4_4_class2 = count_X4_4_class2 / (count_class2)
prob_X5_4_class2 = count_X5_4_class2 / (count_class2)
prob_X6_4_class2 = count_X6_4_class2 / (count_class2)

prob_X1_5_class2 = count_X1_5_class2 / (count_class2)
prob_X2_5_class2 = count_X2_5_class2 / (count_class2)
prob_X3_5_class2 = count_X3_5_class2 / (count_class2)
prob_X4_5_class2 = count_X4_5_class2 / (count_class2)
prob_X5_5_class2 = count_X5_5_class2 / (count_class2)
prob_X6_5_class2 = count_X6_5_class2 / (count_class2)


# In[5]:


#loading the test dataset

filename = "test2_19.csv"
test_data = pd.read_csv(filename, sep=',', header = 0)

test_data.head()


# In[6]:


#split test data into dependent and independent variable 

X_test = test_data.values[:,1:7]
Y_test = test_data.values[:,0]

test_length, test_width = X_test.shape


# In[7]:


#to calculate our predictions and accuracy

pred = list()  #list to store the predictions

prob_class1 = 1
prob_class2 = 1

class_prob_1 = count_class1/length
class_prob_2 = count_class2/length

for k in range(test_length):
    prob_class1 = 1
    prob_class2 = 1
    
    for l in range(test_width):
        
        if l == 0:
            
            if X_test[k,l]==1:
                prob_class1 = prob_class1*prob_X1_1_class1
                prob_class2 = prob_class2*prob_X1_1_class2
            
            elif X_test[k,l]==2:
                prob_class1 = prob_class1*prob_X1_2_class1
                prob_class2 = prob_class2*prob_X1_2_class2
            
            elif X_test[k,l]==3:
                prob_class1 = prob_class1*prob_X1_3_class1
                prob_class2 = prob_class2*prob_X1_3_class2
            
            elif X_test[k,l]==4:
                prob_class1 = prob_class1*prob_X1_4_class1
                prob_class2 = prob_class2*prob_X1_4_class2
            
            elif X_test[k,l]==5:
                prob_class1 = prob_class1*prob_X1_5_class1
                prob_class2 = prob_class2*prob_X1_5_class2
               
            
        elif l == 1:
            
            if X_test[k,l]==1:
                prob_class1 = prob_class1*prob_X2_1_class1
                prob_class2 = prob_class2*prob_X2_1_class2
            
            elif X_test[k,l]==2:
                prob_class1 = prob_class1*prob_X2_2_class1
                prob_class2 = prob_class2*prob_X2_2_class2
            
            elif X_test[k,l]==3:
                prob_class1 = prob_class1*prob_X2_3_class1
                prob_class2 = prob_class2*prob_X2_3_class2
            
            elif X_test[k,l]==4:
                prob_class1 = prob_class1*prob_X2_4_class1
                prob_class2 = prob_class2*prob_X2_4_class2
            
            elif X_test[k,l]==5:
                prob_class1 = prob_class1*prob_X2_5_class1
                prob_class2 = prob_class2*prob_X2_5_class2
  
            
        elif l == 2:
            if X_test[k,l]==1:
                prob_class1 = prob_class1*prob_X3_1_class1
                prob_class2 = prob_class2*prob_X3_1_class2
            
            elif X_test[k,l]==2:
                prob_class1 = prob_class1*prob_X3_2_class1
                prob_class2 = prob_class2*prob_X3_2_class2
            
            elif X_test[k,l]==3:
                prob_class1 = prob_class1*prob_X3_3_class1
                prob_class2 = prob_class2*prob_X3_3_class2
            
            elif X_test[k,l]==4:
                prob_class1 = prob_class1*prob_X3_4_class1
                prob_class2 = prob_class2*prob_X3_4_class2
            
            elif X_test[k,l]==5:
                prob_class1 = prob_class1*prob_X3_5_class1
                prob_class2 = prob_class2*prob_X3_5_class2 
  
            
        elif l == 3:
            
            if X_test[k,l]==1:
                prob_class1 = prob_class1*prob_X4_1_class1
                prob_class2 = prob_class2*prob_X4_1_class2
            
            elif X_test[k,l]==2:
                prob_class1 = prob_class1*prob_X4_2_class1
                prob_class2 = prob_class2*prob_X4_2_class2
            
            elif X_test[k,l]==3:
                prob_class1 = prob_class1*prob_X4_3_class1
                prob_class2 = prob_class2*prob_X4_3_class2
            
            elif X_test[k,l]==4:
                prob_class1 = prob_class1*prob_X4_4_class1
                prob_class2 = prob_class2*prob_X4_4_class2
            
            elif X_test[k,l]==5:
                prob_class1 = prob_class1*prob_X4_5_class1
                prob_class2 = prob_class2*prob_X4_5_class2
  
            
        elif l == 4:
            if X_test[k,l]==1:
                prob_class1 = prob_class1*prob_X5_1_class1
                prob_class2 = prob_class2*prob_X5_1_class2
            
            elif X_test[k,l]==2:
                prob_class1 = prob_class1*prob_X5_2_class1
                prob_class2 = prob_class2*prob_X5_2_class2
            
            elif X_test[k,l]==3:
                prob_class1 = prob_class1*prob_X5_3_class1
                prob_class2 = prob_class2*prob_X5_3_class2
            
            elif X_test[k,l]==4:
                prob_class1 = prob_class1*prob_X5_4_class1
                prob_class2 = prob_class2*prob_X5_4_class2
            
            elif X_test[k,l]==5:
                prob_class1 = prob_class1*prob_X5_5_class1
                prob_class2 = prob_class2*prob_X5_5_class2
  
            
        elif l == 5:
            
            if X_test[k,l]==1:
                prob_class1 = prob_class1*prob_X6_1_class1
                prob_class2 = prob_class2*prob_X6_1_class2
            
            elif X_test[k,l]==2:
                prob_class1 = prob_class1*prob_X6_2_class1
                prob_class2 = prob_class2*prob_X6_2_class2
            
            elif X_test[k,l]==3:
                prob_class1 = prob_class1*prob_X6_3_class1
                prob_class2 = prob_class2*prob_X6_3_class2
            
            elif X_test[k,l]==4:
                prob_class1 = prob_class1*prob_X6_4_class1
                prob_class2 = prob_class2*prob_X6_4_class2
            
            elif X_test[k,l]==5:
                prob_class1 = prob_class1*prob_X6_5_class1
                prob_class2 = prob_class2*prob_X6_5_class2
      

    
    prob_class1 = prob_class1*class_prob_1
    prob_class2 = prob_class2*class_prob_2
    
    tot = prob_class1 + prob_class2
    
    prob_class1 = prob_class1/tot
    
    prob_class2 = prob_class2/tot
    
   
    if prob_class1>prob_class2:
        pred.append(0)
    if prob_class1<prob_class2:
        pred.append(1)   

print(pred)


# In[8]:


#to calculate accuracy

count = 0

for m in range(test_length):
    
    if Y_test[m]==pred[m]:
        
        count = count + 1
        
accuracy = (count/test_length)*100

print("Accuracy : ",accuracy, "%")

