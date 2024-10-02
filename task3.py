c = int(input())
if (5<c<21): print (c, 'лет')
elif (c%10 == 1): print (c, 'год'),
elif (c%10 < 5): print (c, 'года'),
else: print (c, 'лет')