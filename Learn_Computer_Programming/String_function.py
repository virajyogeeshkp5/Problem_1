# String Function
st='we are learning'
y=st.islower()
print(y)

st='We Are'
y=st.islower()
print(y)

st='PYTHON'
y=st.isupper()
print(y)

st='PYTHON'
y=st.isspace()
print(y)

k=" ".isspace()
print(k)

st='432'
k=st.isdigit()
print(k)

st='432abc'
k=st.isdigit()
print(k)

str='learn python programming online'
k=str.isalpha()
print(k)

st='$currency'
k=st.isalpha()
print(k)

l='123.5'
k=l.isdigit()
print(k)

st='abc123'
j=st.isalnum()
print(j)

str1='we are learning computer program'
k=str.istitle()
print(k)

str2='We Are Learning Computer Program'
k=str.istitle()
print(k)

print(str1.endswith('ram'))
print(str1.startswith('we'))
print(str1.replace('we','go'))

j='Rno'
k=j.join('123')
print(k)

# operators
st1='world'
st2='power'
print(st1+st2)

print(st1*3)

print(st1==st2)

# Slicing
s1='Interface windows'
print(s1[9:13])
print(s1[:9])
print(s1[10:])
