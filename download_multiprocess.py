import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import urllib2
import glob
import urllib

def get_image(item):
	prefix, urlx = item.strip().split(',') 
	path2save =  '{}/{}.{}'.format('./images', prefix, 'jpg')
	# content = urllib2.urlopen(tmp).read()
	#with open('path2save', 'wb+') as f:
	#	f.write(urllib2.urlopen(urlx).read())
	urllib.urlretrieve(urlx, path2save)
	time.sleep(1)

def need_down_idx_image():
	img_pairs = {}
	with open('./photos/photos.txt', 'r') as f:
		urls = f.readlines()
		for item in urls:
			img_pairs[item.strip().split(',')[0]] = item.strip().split(',')[1]

	exist_imgs = glob.glob('./images/*')
	exist_idx = [ img.split('\\')[-1].split('.')[0] for img in exist_imgs ]
	need_down_idx = list(set(img_pairs.keys()) ^ set(exist_idx))

	need_down_url = [idx+','+img_pairs[idx] for idx in need_down_idx]

	print len(need_down_url), len(exist_imgs), len(img_pairs)
	return need_down_url

if __name__ == '__main__':
	start = time.clock()

	need_down_urls = need_down_idx_image()
	#pool = Pool(64)
	pool = ThreadPool(64)
	pool.map(get_image, need_down_urls)
	pool.close()
	pool.join()

	print time.clock() - start