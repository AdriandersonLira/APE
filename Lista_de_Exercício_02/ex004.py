v1 = int(input())
h = v1//3600
r = v1%3600
m = r//60
r = r%60
s = r
print('{}:{}:{}'.format(h,m,s))
