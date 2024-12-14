# Collection Types
# List
int_list=[1,2,3]
print(int_list)

string_list=['abc','defghi']
print(string_list)

empty_list=[]
print(empty_list)

mixed_list=[1,'abc',True,2.34,None]
print(mixed_list)

nested_list=[['a','b','c'],[1,2,3]]
print(nested_list)

names=['alice','bob','crig','diana','eric']
print(names)
print(names[0])
print(names[2])
print(names[-1])
print(names[-4])

# change value
names[0]='anna'
print(names)

# append add a new object
names.append('sia')
print(names)

# add value in a specific index
names.insert(1,'nikel')
print(names)

# remove value
names.remove("bob")
print(names)

# get index
print(names.index("anna"))


# count length of list
print(len(names))

# count occurence of item
a=[1,2,1,1,3,4]
print(a.count(1))

#reverse
print(a.reverse())

print(a[ : :-1])

names.pop()
print(names)

# Tuple
ip_address=('10.20.30',8080)
print(ip_address)

one_member_tuple=('only member',)
print(one_member_tuple)

one_member_tuple='only member',
print(one_member_tuple)

one_member_tuple=tuple(['only member'])
print(one_member_tuple)

# dictionary
state_capital = {'arkansas':'little rock','colorado':'denver','california':'sacramento'}

#get value
ca_capital=state_capital['california']
print(ca_capital)

for k in state_capital.keys():
    print('{} is the capital of {}'.format (state_capital[k],k))

# set
first_names={'adam','beth','charlie'} 
print(first_names)

my_list=[1,2,3]
my_set=set(my_list)
print(my_set)


