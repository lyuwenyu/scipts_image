from skimage import io,color,transform
import glob
import random
import matplotlib.pyplot as plt



def label2new_map(labels):
        label_map = {}
        new_label = 0
        for key in sorted(labels.keys()):
                label_map[key] = new_label
                new_label +=1
        return label_map


def remove_small_class(labelNum, smallnum=0):
        x = 0
        for key in labelNum.keys():
                if labelNum[key] < smallnum:
                        x+=labelNum.pop(key)
        return labelNum


def read_imagename(imagedir, smallnum=0):
        ll = glob.glob(imagedir+'/'+ '*.jpg')
        for i in range(len(ll)):
                tmp = ll[i].strip().split('/')
                ll[i] = tmp[-1]
        classNum = {}
        for name in ll:
                if name[:3] in classNum.keys():  # int( ll[:3] )
                        classNum[name[:3]] += 1
                else:
                        classNum[name[:3]] = 1
        classNum = remove_small_class(classNum, smallnum)
        return ll, classNum



def convert1(f):
        img = io.imread(f)
        return transform.rotate(img,90)


def augument(imagedir, classNum, low=0, high=1000):
        i = 0
        for key in classNum.keys():
                if high>classNum[key]>=low:
                        coll = io.ImageCollection(imagedir+'/'+str(key).rjust(3,'0')+'*.jpg', load_func=convert1)
                        for i in range(len(coll)):
                                name = coll.files[i].strip().split('/')[-1]
                                io.imsave('xxxxxx'+'/'+name+'_new2.jpg',coll[i])


def save2file(imagenames, newclass, filename):

        with open(filename,'w+') as fn:
                for ii in imagenames:
                        if ii[:3] in newclass.keys():
                                line = str(ii) +' '+ str( newclass[ ii[:3] ] ) +'\n'
                                fn.write(line)



def sample_train_test(imagenames, newclass, per):
        ftrain = open('sampled_train.txt','w+')
        ftest = open('sampled_test.txt','w+')
        random.shuffle(imagenames)
        per = len(imagenames)*per
        for i,name in enumerate(imagenames):
                if name[:3] in newclass.keys():
                        if i < per:
                                ftest.write( name+' ' +str( newclass[name[:3]] ) + '\n' )
                        else:
                                ftrain.write( name+' ' +str( newclass[name[:3]] ) + '\n' )
        ftrain.close()
        ftest.close()


def main():
        imageset_dir = 'final_train_image'
        imagenames, classNum = read_imagename(imageset_dir, 100)

#       augument(imageset_dir, classNum, 100, 200)
#       imagenames, classNum = read_imagename(imageset_dir,100)

        newclass = label2new_map(classNum)

#       save2file(imagenames, newclass, 'data.txt')
#       sample_train_test(imagenames, newclass, 0.01)


#       for value in sorted(classNum.values()):
#               print value,

        plt.figure()
        plt.plot( classNum.values(),'ro' )
        plt.show()

if __name__ == '__main__':

        main()
                                                                                                                                      104,1-8       Bot



