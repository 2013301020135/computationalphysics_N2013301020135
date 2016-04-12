import matplotlib as plt
from pylab import *
import pickle

v = []
s = []
t = []
g = 9.8
dt = 0
n = 0

def initialize(v, s, t, _dt, _n):
	global dt, n
	print 'Input initial velocity ->',
	v.append(float(raw_input()))
	print 'g = 9.8 m/s^2'
	print 'Input time step ->',
	dt = float(raw_input())
	print 'Input total time ->',
	time = float(raw_input())
	t.append(0)
	s.append(0)
	n = int(time / dt)+1
	return 0


def calculate(v, s, t, dt, n):
	print g
	print dt
	print n 
        for i in range(1, n):
		s.append(s[i - 1] + v[i - 1] * dt)
		v.append(v[i - 1] - g * dt)
		t.append(t[i - 1] + dt)
        print v    
	print s
	print t
	        
	return 0

def store(v, t, n):
	mfile = open('notes_ex4.txt', 'a')
	for i in range(n):
		print >> mfile, t[i], v[i]
	mfile.close()

	pickle_file = open("pickled_data_ex4.pkl", "w")
    	pickle.dump(t, pickle_file)
    	pickle.dump(v, pickle_file)

    	return 0
	
def read():
	pickle_file = open("pickled_data_ex4.pkl", "r")
	t = pickle.load(pickle_file)
	v = pickle.load(pickle_file)
	print t
	print v

initialize(v, s, t, dt, n)
calculate(v, s, t, dt, n)
store(v, t, n)

#plot
plt.figure(1)
plt.subplot(211)
plt.plot(t, v,"g-", linewidth=1.0)
plt.scatter(t, v)
plt.title('The Velocity of a Free Falling Object')
#plt.xlabel('Time($t$)', fontsize=12) (cancel because words overlap)
plt.ylabel('Velocity($m/s$)', fontsize=12)
plt.text(3,0,r'$g = 9.8 m/s^2$', fontsize=16)
plt.grid(True)

plt.subplot(212)
plt.plot(t, s,"g-", linewidth=1.0)
plt.scatter(t, s)
plt.title('The Displacement of a Free Falling Object')
plt.xlabel('Time($t$)', fontsize=12)
plt.ylabel('Displacement($m$)', fontsize=12)
plt.text(3,0,r'$g = 9.8 m/s^2$', fontsize=16)
plt.grid(True)

plt.show()
plt.savefig("ex4.jpg")
read()
