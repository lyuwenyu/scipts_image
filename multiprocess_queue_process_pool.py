#import multiprocessing
#from multiprocessing import Pool
import time 
from multiprocessing import Queue, Pool, Process
import random

def func(msg):
	print 'func1' + msg
	time.sleep(3)
	print 'func1 done'

def writer(q):
	while True:
		time.sleep(1)
		q.put( random.randint(0,10) )
		

def read(q):
	while not q.empty():
		time.sleep(1)
		print q.get()
		

class Fetcher(Process):
	"""docstring for Fetcher"""
	def __init__(self, queue):
		super(Fetcher, self).__init__()
		self._queue = queue
		
	def run(self):
		while True:
			time.sleep(5)
			self._queue.put( random.randint(0,10) )


if __name__ == '__main__':
	
	#pool = multiprocessing.Pool(processes = 4)
	#for i in xrang(4):
	#	msg = 'hello %d' %(i)
	#	pool.apply_async(func, (msg))
	#print 'hhhhhhhh'
	#pool.close()
	#pool.join()
	#print 'over'


	q_tmp = Queue(10)
	#pw = Process(target=writer, args=(q_tmp, ))
	#pr = Process(target=read, args=(q_tmp, ))
	#pw.start()
	#pr.start()

	#fetcher_process1 = Fetcher(q_tmp)
	#fetcher_process2 = Fetcher(q_tmp)
	#fetcher_process1.start()
	#fetcher_process2.start()

	fetcher_process = Fetcher(q_tmp)
	fetcher_process.start()

	while True:
		st = time.time()
		print q_tmp.get()
		time.sleep(2)
		print time.time()- st



	def clearup():
		fetcher_process.terminate()
		fetcher_process.join()
	import atexit
	atexit.register(clearup)

