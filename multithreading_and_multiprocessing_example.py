"""
Multithreading performs multiple functions  simultaneously
"""

import time
import threading
import multiprocessing

def cal_square(numbers):
	for num in numbers:
		time.sleep(0.5)
		print(num, 'squred is %s' %(num**2))

def cal_cube(numbers):
	for num in numbers:
		time.sleep(0.5)
		print(num, 'cubed is %s' %(num**3))

tit=time.time()
alist = list(range(10))
cal_square(alist)
cal_cube(alist)
tat=time.time()
print('Time taken in plain mode is %s' %(tat-tit)) #10.052264213562012 sec

tit = time.time()
thread1 = threading.Thread(target = cal_square, args = (alist,))
thread2 = threading.Thread(target = cal_cube, args = (alist,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
tat=time.time()
print('Time taken with multithreading is %s' %(tat-tit)) #5.034847021102905

if __name__=='__main__':
	tit = time.time()
	p1 = multiprocessing.Process(target = cal_square, args = (alist,))
	p2 = multiprocessing.Process(target = cal_cube, args = (alist,))
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	tat=time.time()
	print('Time taken with multiprocessing is %s' %(tat-tit)) #5.034847021102905

