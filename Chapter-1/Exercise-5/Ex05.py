import matplotlib as plt
from pylab import *
import pickle

x = []
t = []
v = 0
dt = 0
n = 0

def initialize(x, t, _v, _dt, _n):
	global v, dt, n
	print 'Input initial displacement ->',
	x.append(float(raw_input()))
	print 'Input velocity ->',
        v = float(raw_input())
	print 'Input time step ->',
	dt = float(raw_input())
	print 'Input total time ->',
	time = float(raw_input())
	t.append(0)
	n = int(time / dt)+1
	return 0


def calculate(x, t, v, dt, n):
	print v
        print dt
	print n 
        for i in range(1, n):
		x.append(x[i - 1] + v * dt)
		t.append(t[i - 1] + dt)  
	print x
	print t        
	
        return 0

def store(x, t, n):
	mfile = open('notes_ex5.txt', 'a')
	for i in range(n):
		print >> mfile, t[i], x[i]
	mfile.close()

	pickle_file = open("pickled_data_ex5.pkl", "w")
    	pickle.dump(t, pickle_file)
    	pickle.dump(x, pickle_file)

    	return 0
	
def read():
	pickle_file = open("pickled_data_ex5.pkl", "r")
	t = pickle.load(pickle_file)
	x = pickle.load(pickle_file)

initialize(x, t, v, dt, n)
calculate(x, t, v, dt, n)
store(x, t, n)

#plot
plt.figure(1)
plt.subplot(211)
plt.plot(t, x,"v-", linewidth=1.0)
plt.scatter(t, x)
plt.title('The Displacement of an Uniform Moving Object')
plt.xlabel('Time($t$)', fontsize=12)
plt.ylabel('Displacement($m$)', fontsize=12)
plt.text(3,0,r'v='+str(v)+'$m/s$', fontsize=16)
plt.grid(True)

plt.show()
plt.savefig("ex5.jpg")
read()
