import matplotlib.pyplot as plt
import cv2

def write_frame(path, frame, index, x_cord_label, y_cord_label):
    filename = F'img.{index}.{x_cord_label}.{y_cord_label}.jpg'
    status = plt.imsave(path + '/' + filename, frame)
    return


def label_parser(filename, label_num = 3, delimiter = '.', ext = True):
    # parses filename and returns list of labels seprated by delimiter
    if ext:
        filename = filename[:filename.rfind('.')]
    
    temp = 0
    indexs = []
    for i in range(label_num):
        indexs.append(filename.find(delimiter,temp) + 1)
        temp = filename.find(delimiter,temp) + 1
    indexs.append(len(filename)+1)
    return [int(filename[indexs.pop(0):indexs[0]-1]) for i in range(label_num) ]
