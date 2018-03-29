import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as error
import csv

x = []
a1 = []
a2 = []
a3 = []
a4 = []
az=[]
al=[]
x1=[]
y1=[]
##############
with open('test1.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		x.append(int(row[0]))
		a1.append(int(row[1]))
		a2.append(int(row[2]))
		a3.append(int(row[3]))
		a4.append(int(row[4]))
		az.append(float(row[6]))
		al.append(float(row[7]))
		
#plt.plot(x,a1,'r-',x,a2,'g-',x,a3,'b-',x,a4,'y-',label='A1')
plt.plot(x,a1,'r-',label='A1')
plt.plot(x,a2,'g-',label='A2')
plt.plot(x,a3,'b-',label='A3')
plt.plot(x,a4,'y-',label='A4')
plt.xlabel('samples')
plt.ylabel('Adc values')
plt.title('30nsec, with filtering, with 16 count subtract from ADC2, with complete gain switching')
plt.legend()
plt.show()


error.plot(x,az,'r-',x,al,'b-')
error.xlabel('samples')
error.ylabel('error')
error.title('Error with 40nsec')
error.legend()
error.show()

#
# with open('ldts.csv','r') as csvfile2:
	# plots1 = csv.reader(csvfile2, delimiter=',')
	# for row1 in plots1:
		# x1.append(float(row1[5]))
		# y1.append(int(row1[2]))
		
# plt1.plot(x1,y1,'r-')
# plt1.xlabel('x')
# plt1.ylabel('y')
# plt1.legend()
# plt1.show()