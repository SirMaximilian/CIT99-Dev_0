import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import LabelDataHelper as dH
import os

data = os.scandir(os.getcwd() + '/raw_datasets')
path_labeled = os.getcwd() + '/labeled_datasets'

try: os.mkdir(path_labeled)
except OSError: pass

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
start_idx = next(data).name
[idx] = dH.label_parser(start_idx,1)
img = mpimg.imread('./raw_datasets/' + start_idx)
imgplot = plt.imshow(img)

Done = False

def onclick(event):
    global img, idx, Done
    if Done:
        return
    try:
        dH.write_frame(path_labeled, img, idx, int(event.xdata), int(event.ydata))
        img = mpimg.imread('./raw_datasets/' + next(data).name)
        imgplot.set_data(img)
        fig.canvas.draw()
        idx += 1
        print(' xdata=%d, ydata=%d' %(int(event.xdata), int(event.ydata)))
    except StopIteration:
        print('Done!')
        Done = True
        return
    except TypeError:
        pass
    
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

