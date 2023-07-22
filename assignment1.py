#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=int(input("Enter any number:"))
n1,n2=0,1
sum=0
if num<=0:
    print('please enter number greater than 0')
else:
        for i in range(0,num):
            print(sum,end=" ")
            n1=n2
            n2=sum
            sum=n1+n2
            
        


# In[8]:


name="swethapriya"
name[::-1]


# In[4]:


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
             count_even+=1
        else:
             count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)


# In[ ]:





# In[ ]:





# In[ ]:




