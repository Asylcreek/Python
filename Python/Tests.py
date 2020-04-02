import math;
# import numpy;

Th1 = 400;
Th2 = 170;
Tc1 = 110;
Tc2 = 190;
N = 2;
# R = 0.8333;
# P = 0.4615;

P = (Tc2-Tc1)/(Th1-Tc1);
R = (Th1-Th2)/(Tc2-Tc1);

# P = 0.32;
# R = 1.65;

aa = 1 - ((R*P - 1)/(P-1))**(1/N);
bb = R - ((R*P - 1)/(P-1))**(1/N);
X = aa/bb

a = ((math.sqrt(R*R +1)/(R-1))*math.log((1-X)/(1-R*X)));
b = math.log(((2/X)-1-R+math.sqrt(R*R +1))/((2/X)-1-R-math.sqrt(R*R +1)))
F = a/b


# a = (((P*P + 1)**0.5)*math.log((1-R)/(1 - (P*R))));
# b = ((P-1)*math.log((2-R*((P+1)-((P*P +1)**0.5)))/(2-R*(P+1 - math.sqrt(P*P +1)))));
# c = 2-R*(P+1 - math.sqrt(P*P +1));
# d = 2-R*(P+1 - math.sqrt(P*P +1));
# b = (P-1)*math.log(c/d)
# ft = a/b;

print(aa);
print(bb);
print(X);
print()
print(P);
print(R);
print()
print(a);
print(b);
print(F);
