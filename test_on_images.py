from PIL import Image
from pylab import *
from numpy import *
import os

data_dir = '/Users/xcbfreedom/projects/data/formula_images/user_images'
#data_dir = '/Users/xcbfreedom/projects/data/formula_images/standard_images'

output_dir = 'test_result' 

def get_imlist(path):
    t = []
    for f in os.listdir(path):
        if f.endswith('.jpg') or f.endswith('.gif') or f.endswith('.png'):
            t.append(os.path.join(path,f))    
    return t


def convert_to_gray(imlist):
    """    Compute the average of a list of images. """
    # open first image and make into array of type float
    skipped = 0
    for file_parth in imlist[1:]:
        try: 
            img = Image.open(file_parth).convert('L')
            outfile = os.path.splitext(os.path.basename(file_parth))[0]+'.png'
            outfile_parth = os.path.join(output_dir,outfile)
            img.save(outfile_parth)
        except e:
            print file_parth + "...skipped"  
            skipped += 1
    print 'total skipped: ', skipped

if __name__=='__main__':
    if 2==len(sys.argv):
        output_dir = sys.argv[1]

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    else:
        print "warning: %s exists!" % output_dir

    print 'process results are in %s' % output_dir
    file_list = get_imlist(data_dir)
    convert_to_gray(file_list)
    #print file_list

