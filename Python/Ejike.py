#a = k1, b = k2, c = k3, d = k4
#functions
def fn1 (x, y1,y2,y3):
    return y2
def fn2 (x, y1,y2,y3):
    return y3
def fn3 (x, y1,y2,y3):
    return -0.5*y1*y3

#create list for each solution
xx = [0]
y11 = [0]
y22 = [0]
y33 = [0.33206]

#the boundary conditions
x = 0;
y1 = 0;
y2 = 0;
y3 = 0.33206;

#using 'n' for number of iterations and 'h' for step size
h = 0.2;
n = 50;

#the rungekutta fourth order method
for i in range(n-1):
    #getting the k's
    k1_1 = h * fn1(x, y1, y2, y3);
    k1_2 = h * fn2(x, y1, y2, y3);
    k1_3 = h * fn3(x, y1, y2, y3);
    
    k2_1 = h * fn1(x+h/2, y1+k1_1/2, y2+k1_2/2, y3+k1_3/2);
    k2_2 = h * fn2(x+h/2, y1+k1_1/2, y2+k1_2/2, y3+k1_3/2);
    k2_3 = h * fn3(x+h/2, y1+k1_1/2, y2+k1_2/2, y3+k1_3/2);
    
    k3_1 = h * fn1(x+h/2, y1+k2_1/2, y2+k2_2/2, y3+k2_3/2);
    k3_2 = h * fn2(x+h/2, y1+k2_1/2, y2+k2_2/2, y3+k2_3/2);
    k3_3 = h * fn3(x+h/2, y1+k2_1/2, y2+k2_2/2, y3+k2_3/2);
    
    k4_1 = h * fn1(x+h, y1+k3_1, y2+k3_2, y3+k3_3);
    k4_2 = h * fn2(x+h, y1+k3_1, y2+k3_2, y3+k3_3);
    k4_3 = h * fn3(x+h, y1+k3_1, y2+k3_2, y3+k3_3);
    
    #getting the solution 
    y1 = y1 + 1/6 * (k1_1 + 2*k2_1 + 2*k3_1 + k4_1);
    y2 = y2 + 1/6 * (k1_2 + 2*k2_2 + 2*k3_2 + k4_2);
    y3 = y3 + 1/6 * (k1_3 + 2*k2_3 + 2*k3_3 + k4_3);

    #adding the solutions to the respective lists
    y11.append(round(y1,6))
    y22.append(round(y2,6))
    y33.append(round(y3,6))
    
    #increase in x and add to its list
    x = x + h;
    xx.append(round(x,2))

#creating the .txt file
filename = open("revelocityout.txt", "w");

#heading of the .txt file
filename.write('{} {:>5} {:>5} {:>12} {:>10}\n'.format('teration','Eta', 'F', 'F_Prime', 'F_Prime_Prime'))

#writing the solutions to the .txt file
for i in range(len(xx)):
    a = i, xx[i], y11[i], y22[i], y33[i]
    filename.write('    %.2d      %.2f  %.4f   %.4f   %f\r\n\n' %(i, xx[i], y11[i], y22[i], y33[i]))

#close the file
filename.close()
