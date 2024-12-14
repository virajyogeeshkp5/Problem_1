# string data types

a_str='hello world'
print(a_str)
print(a_str[0])
print(a_str[0:5])

# set data types

basket = {'apple','orange','apple','pear','orange','banana'}
print(basket)

a=set('abracadabra')
print(a)

a.add('z')
print(a)

b=frozenset('asdfagsa')
print(b)

cities=frozenset(["frankfurt",'basel',"freiburg"])
print(cities)

# numbers data types

int_num=10
print(int_num)
float_num=10.2
print(float_num)
complex_num=3.14j
print(complex_num)
long_num=123456
print(long_num)

# list data types

list=[123,'abcd',10.2,'d']
list1=['hello','world']
print(list)
print(list[0:2])
print(list1*2)
print(list+list1)

# dictionary data types

dic={'name':'red','age':10}
print(dic)
print(dic['name'])
print(dic.values())
print(dic.keys())

# tuple data type
tuple=(123,'hello')
tuple1=('world')
print(tuple)
print(tuple[0])

