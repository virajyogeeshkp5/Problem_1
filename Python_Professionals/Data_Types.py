#numbers
# int
a=2
print('int:',a)

# float
b=2.0
print('float:',a)

#complex
c=2+1j
print('complex:',c)

# string
d='hello'
print('string:',d)

a=(1,2,3)
b=('a',1,'py',(1,2))
print(b[2])


a=[1,2,3]
b=['a',1,'py',[1,2],[1,2]]
print(b[2])

# set
a={1,2,'a'}
print(a)

#dict
d={'a':[1,2,3],'b':'string'}
print(d)

# Testing the type of value
a='123'
print(type(a))

b=123
print(type(b))

print(issubclass(bool,int))
print(isinstance(True,bool))
print(isinstance(False,bool))

i=7
if isinstance(i,int):
    i+=1
elif isinstance(i,str):
    i=int(i)
    i+=1

x=None
if x is None:
    print('is none x:',x)

a='123'
b=int(a)
print(b)

a='123.456'
b=float(a)
print(a)

a='hello'
print(list(a))
print(set(a))
print(tuple(a))


