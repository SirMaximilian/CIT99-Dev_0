import cv2

def write_raw_frame(path, frame, index):
    filename = F'img_raw.{index}.jpg'
    status = cv2.imwrite(path + '/' + filename, frame)
    return

def write_frame(path, frame, index, x_cord_label, y_cord_label):
    filename = F'img.{index}.{x_cord_label}.{y_cord_label}.jpg'
    status = cv2.imwrite(path + '/' + filename, frame)
    return

def imgcrop224(frame):
    # crops given image frame to be 224 by 224
    y = frame.shape[0]
    x = frame.shape[1]
    cy = y - 224
    cx = x - 224
    print 
    return frame[int(cy/2):int(cy/2)+224, int(cx/2):int(cx/2)+224]

def label_parser(filename, label_num = 3, delimiter = '.'):
    # parses filename and returns list of labels seprated by delimiter
    temp = 0
    indexs = []
    for i in range(label_num):
        indexs.append(filename.find(delimiter,temp) + 1)
        temp = filename.find(delimiter,temp) + 1
    indexs.append(len(filename)+1)
    return [int(filename[indexs.pop(0):indexs[0]-1]) for i in range(label_num) ]

def counter(start_index=0):
    n=0+start_index
    while True:
        yield n
        n+=1