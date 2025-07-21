import numpy as np
                                                #  CREATE
# x=np.array([2,3,4,5,6,5])
# print(x)

# a=np.arange(4)
# a=np.arange(-10,-4,1)
# a=np.arange(-10,-4,-1)
# print(a)

# a1=np.random.random(size=(4,3))
# print(a1)

# x1=np.random.randint(50,size=6) #one dimensional
# x2=np.random.randint(10,size=(3,4)) #two dimensional
# x3=np.random.randint(10,size=(3,4,5))    #three dimensional
# print(x1)
# print(x2)
# print(x3)
#                                                 #     READ
# arr=np.array([2,3,4,5,6,5])
# print(arr)
# print('Dimensions:',arr.ndim)

# data2=[[1,2,3,4],[5,6,7,4]]
# arr2=np.array(data2)
# print(arr2)
# print('Dimensions:',arr2.ndim)

# arr3=np.random.randint(50,size=(3,4,5,2))
# print(arr3)
# print('Dimensions:',arr3.ndim)

# arr1=np.arange(10)
# arr2=np.arange(12).reshape(3,4)
# arr3=np.arange(24).reshape(2,4,3)
# print(arr1)
# print(arr2)
# print(arr3)

# arr1=np.arange(10)                        

                                                   # SLICING IN NUMPY ARRAY

# print(arr1)                 # 1d array
# print(arr1[3:8:1])
# print(arr1[::])
# print(arr1[::-1])
# print(arr1[2::2])

# arr2=np.arange(12).reshape(3,4)           # 2d array
# print(arr2)
# print(arr2[-1: :-2,-1::-3])
# print(arr2[1::,::2])
# print(arr2[0,:])
# print(arr2[:,0])
# print(arr2[1:,1:])
# print(arr2[::2,:2:])

# arr3=np.arange(24).reshape(2,4,3)          # 3d array
# print(arr3)
# print(arr3[1,1::2,::2])
# print(arr3[0])
# print(arr3[0,0])
# print(arr3[1,:3])
# print(arr3[0,:2,::2])
# print(arr3[:,::3,0::2])
# print(arr3[::-1,-2::-2,-1::-2])
# print(arr3[::-1,-2::-1,-2::-1])

                                               # ATTRIBUTES
# a1=np.array([1,2,3,4])
# a2=np.array([1.1,2.2,3.3,4.4])

# print(a1.dtype)
# print(a2.dtype)

# print(a1.itemsize)
# print(a2.itemsize)

# print(a1.nbytes)
# print(a2.nbytes)

# a1=np.array([1,2,3,4])
# a2=np.array([[1,2,3,4],[5,6,7,8]])

# print(a1.ndim)
# print(a2.ndim)

# print(a1.shape)
# print(a2.shape)

# print(a1.size)
# print(a2.size)
 
                                                       # FUNCTIONS
                                    # ZEROS
# print(np.zeros(10))
# print(np.zeros((3,6),dtype='int'))
# print(np.zeros((2,3,2)))
 
                                    # ONES
# print(np.ones(10))
# print(np.ones((3,6),dtype='int'))
# print(np.ones((2,3,2)))

                                     # IDENTITY
# print(np.identity(4,dtype='int32'))

                                                     # ARITHMETICAL OPERATION 

# a1=np.array([1,2,3,4,5])
# a2=np.array([1,1,2,3,4.5,6])
# print(a1)
# print(a2)

# print(a1+5)
# print(a1-5)
# print(a1*5)
# print(a1/5)
# print(a1//5)
# print(a1**5)              # a1 to the power 5

                           # DOT PRODUCT

# arr1=np.arange(12).reshape(3,4)
# arr2=np.arange(12).reshape(4,3)
# print(arr1)
# print(arr2)
# print(np.dot(arr1,arr2))
  
                            # STATICAL OPERATION  

# arr1=np.arange(12).reshape(3,4)
# arr2=np.arange(12).reshape(4,3)
# print(np.max(arr1,axis=0))           # column wise
# print(np.min(arr1,axis=1))           # row wise
# print(np.mean(arr2))                 # mean
# print(np.var(arr2))                  # variance(square of arr[]-mean of arr)

# p23=np.percentile(arr1,23)           # percentile
# print(p23)

# a2=np.arange(20).reshape(4,5)          # iteration
# for i in a2:
#     print(i)
 
# add 5,10,15,20 respectively in every row
# print(a2[0]+5)
# print(a2[1]+10)
# print(a2[2]+15)
# print(a2[3]+20)

                                        # STACKING
# s1=np.arange(12).reshape(3,4)
# s2=np.arange(12,24).reshape(3,4)
# print(s1)
# print(s2)
 
# s3=np.hstack((s1,s2))               #horizontal stacking no. of columns and rows are always same 
# print(s3)
# s4=np.vstack((s1,s2))                 #vertical stacking no. of columns and rows are always same 
# print(s4)
 
                                    # SPLTTING
# s3=np.hstack((s1,s2))
# print(s3)
# print(np.hsplit(s3,2))
# print(np.vsplit(s3,3))

# s4=np.vstack((s1,s2))                 
# print(s4)
# a,b=np.hsplit(s4,2)
# print(a,"\n\n")
# print(b)

# a,b=np.vsplit(s4,2)
# print(a,"\n\n")
# print(b)

#WAP which makes an array having corresponding max value out of two given array(a,b)

# a=np.array([6,3,1,5,8])
# b=np.array([3,2,1,7,2])
# print(np.maximum(a,b))

# a=np.array([6,3,1,5,8])
# b=np.array([3,2,1,7,2])
# m=[]
# for i in range(len(a)):
#     m.append(max(a[i],b[i]))
# print(np.array(m))
