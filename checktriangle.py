#Language: Python
print('Enter sides of a triangle')
s1=int(input('side 1: '))
s2=int(input('side 2: '))
s3=int(input('side 3: '))
if (s1>(s2+s3) or s2>(s1+s3) or s3>(s1+s2)):
    print('INVALID')
else:
    print('valid')
