import math;
import numpy;

R = 1.65;
P = 0.32;

a = (((R^2 + 1)^0.5)*math.log((1-P)/(1-R*P)) );
b = ((R-1)*math.log((2-P(R+1-((R^2 +1)^0.5)))/(2-P(R+1 - srqt(R^2 +1)))));
ft = a/b;

print(a);
print (b);
print(ft);