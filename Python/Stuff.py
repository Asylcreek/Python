import math;

# R = 1.65;
# P = 0.32;

# a = (((R**2 + 1)**0.5)*math.log((1-P)/(1 - (R*P))));
# b = ((R-1)*math.log((2- (P*(R+1-((R**2 +1)**0.5)))/(2-(P*(R+1 - math.sqrt(R**2 +1)))))));

# ft = a/b;
t_hot_in = 400;
t_hot_out = 170;
t_cold_in = 110;
t_cold_out = 190;

a = (t_hot_in - t_cold_out) - (t_hot_out - t_cold_in)
b = math.log((t_hot_in - t_cold_out)/t_hot_out - t_cold_in)
lmtd = a/b

p = (t_cold_out- t_cold_in)/(t_hot_out - t_cold_in)
r = (t_hot_in - t_hot_out)/(t_cold_out - t_cold_in)


print(a);
print (b);
print(ft);