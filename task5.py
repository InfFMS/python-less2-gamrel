#Найдите все пятизначные числа, которые при делении на 133 дают
# в остатке 125, а при делении на 134 дают в остатке 111.
# XXXXX/133 = YYY+125
# XXXXX/134 = ZZZ+111
c=int(133)
C=int(134)
n=int(10000)
N=int(100000)
while (n < N):
    if (n%c == 125) and (n%C == 111): print (n)
    n += 1