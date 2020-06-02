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

def multi_thread():
	draw_circle_thread = threading.Thread(target=draw_circle, args=(1,))
	draw_square_thread = threading.Thread(target=draw_square, args=(2,))
	draw_circle_thread.start()
	draw_square_thread.start()
	draw_circle_thread.join()
	draw_square_thread.join()

if __name__ == '__main__':
	print("start ", time.ctime())
	multi_thread()
	print("end ", time.ctime())
