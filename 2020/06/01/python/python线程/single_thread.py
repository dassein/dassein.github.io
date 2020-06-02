import time
import threading

def draw_circle(cost):
	print("start draw a circle ", time.ctime())
	time.sleep(cost)
	print("draw a circle ", time.ctime())

def draw_square(cost):
	print("start draw a square ", time.ctime())
	time.sleep(cost)
	print("draw a square ", time.ctime())

def single_thread():
	draw_circle(1)
	draw_square(2)

if __name__ == '__main__':
	print("start single_thread ", time.ctime())
	single_thread()
	print("end single_thread ", time.ctime())
