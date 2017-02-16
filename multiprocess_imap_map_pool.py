from multiprocessing import Pool
import time
from functools import partial


def func(x):
	time.sleep(0.001)
	#print ''
	return x**2


if __name__ == '__main__':

	start = time.time()

	pool = Pool(5)

	res_final = []
	#for i in xrange(10):
	#	res  = pool.apply_async(func, (i,))
	#	res_final.append( res.get() )
	
	#res_final = [x.get() for x in [pool.apply_async(func, (y,)) for y in xrange(10)]]

	#res_final = pool.map(func, xrange(10))
	
	#res_final = pool.imap(func, [2,3,4,10,5,10,2,0,1,2,4])

	for x in pool.imap(func, xrange(1000)):
		res_final.append(x)
		print x
		

	#res_final = [ x for x in pool.imap(func, xrange(1000)) ]


	#print res_final

	pool.close()
	pool.join()

	print 'main process'

	print time.time() - start


