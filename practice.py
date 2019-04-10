import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,8],[4,7,6],[5,5,6]])
rand_index=np.random.choice(len(a),3, replace=False)
rand_a=a[rand_index]
print(rand_a)
print(np.transpose(rand_a))



b=np.random.normal(1,0.1,10)
print(b)
rand_index=np.random.choice(len(b),3, replace=False)
rand_b=b[rand_index]
print(rand_b)
print(np.transpose(rand_b))
print(np.shape(rand_b))
print(np.shape(np.transpose(rand_b)))
b_expand=rand_b[:, np.newaxis]
print(b_expand)


c=np.random.normal(1,0.1,10)
d=np.random.normal(1,0.1,10)
e=np.concatenate((c,d))
print(e)
print(np.shape(e))


f=np.matrix(c)
print(f)
print(np.shape(f))

g=np.array([i[0] for i in a ])
print('g:',g)

print(np.shape(a[0]))
print(np.shape(a[0][0]))


h=np.array([[1,2,3],[4,5,6],[7,8,8],[4,7,6],[5,5,6]])
i=h[np.random.choice(4,2)]

print(np.random.choice(4,2))
print('i',i)
