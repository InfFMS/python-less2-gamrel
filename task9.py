x = int(input())
y = int(input())
z = int(input())
u = int(input())
if (abs(x-z)<3 and abs(u-y)<3):
    if (abs(x-z)==(2*(abs(u-y)))): print('Yes')
    elif (2*(abs(x-z))==(abs(u-y))): print('Yes')
    else: print('No')
else: print('No')